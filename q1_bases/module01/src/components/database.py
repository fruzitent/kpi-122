import sqlite3
from time import time_ns

from PySide6.QtSql import QSqlDatabase

from public.i18n import errors
from src.config import config
from src.utils.error_handlers import sqlite_error_handler
from src.utils.logger import Logger

log = Logger(__name__)


class Database:
    def __init__(self):
        self.con = sqlite3.connect(config.DB_PATH, check_same_thread=False)
        self.con.row_factory = sqlite3.Row

        self.qt_db = QSqlDatabase.addDatabase("QSQLITE")
        self.qt_db.setDatabaseName(config.DB_PATH)

        if self.qt_db.open():
            self.qt_db.exec("""pragma foreign_keys = on""")
        else:
            raise LookupError(errors.db_no_connection())

        self._create_tables()
        self.con.commit()
        self.backup()

    def backup(self):
        def progress(status, remaining, total):
            current = total - remaining
            log.debug(f"copied {current}/{total} pages, status: {status}")

        backup = sqlite3.connect(config.DB_BACKUP_PATH)
        self.con.backup(backup, pages=1, progress=progress)
        backup.close()

    def exit(self):
        self.qt_db.close()
        self.con.close()

    def _create_tables(self):
        self.con.execute(
            """
            create table if not exists users(
                firstname text check(length(firstname) <= 63) not null,
                lastname text check(length(lastname) <= 63) not null,
                username text check(length(username) <= 63) primary key,
                password text not null,
                weight int check(weight > 0) not null,
                height int check(height > 0) not null,
                birthday text check(length(birthday) = 19) not null,
                sex int check(sex between 0 and 1) not null,
                activity int check(activity between 0 and 4) not null
            )
            """
        )

        self.con.execute(
            """
            create table if not exists products(
                name text check(length(name) <= 255) not null,
                calories float check(calories > 0) not null,
                protein float check(protein > 0) not null,
                fat float check(fat > 0) not null,
                carbohydrate float check(carbohydrate > 0) not null,
                id integer primary key autoincrement,
                owner text,
                constraint product_owner
                    foreign key (owner)
                    references users(username)
                    on delete cascade,
                unique (name, owner)
            )
            """
        )

        self.con.execute(
            """
            create table if not exists users_ate_products(
                product_id integer not null,
                weight integer check(weight >= 0) not null,
                date integer check(date > 0) not null,
                id integer primary key autoincrement,
                user_username text not null,
                constraint ate_id
                    foreign key (product_id)
                    references products(id)
                    on delete cascade,
                constraint ate_user
                    foreign key (user_username)
                    references users(username)
                    on delete cascade
            )
            """
        )

    def get_user(self, username):
        user = self.con.execute(
            """
            select *
            from users
            where username = ?
            """,
            [username],
        ).fetchone()

        if not user:
            raise LookupError(errors.user_not_found())

        log.info(f"found user {user['username']}")
        return dict(user)

    @sqlite_error_handler
    def add_user(self, user):
        username = user["username"]

        self.con.execute(
            """
            insert into users
            values (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [*user.values()],  # noqa: WPS356
        )

        self._add_default_products_to_user(username)
        self.con.commit()
        log.info(f"added user {username}")

    def _add_default_products_to_user(self, username):
        self.con.execute("attach database ? as dp", [config.PRODUCTS_DB_PATH])
        self.con.execute("insert into products select * from default_products")
        self.con.execute(
            """
            update products
            set owner = ?
            where owner is null
            """,
            [username],
        )

    @sqlite_error_handler
    def update_user(self, username, weight, height, activity):
        self.con.execute(
            """
            update users
            set weight = ?, height = ?, activity = ?
            where username = ?
            """,
            [weight, height, activity, username],
        )

        self.con.commit()
        log.info(f"updated user {username}")
        return self.get_user(username)

    def get_eaten_products(self, username, interval):
        log.info(f"getting user {username}'s eaten products in last {interval} ns")
        return self.con.execute(
            """
            select *
            from products
            inner join users_ate_products
            on products.id = users_ate_products.product_id
            where user_username = ?
            and date > ?
            """,
            [username, time_ns() - interval],
        ).fetchall()


db = Database()
