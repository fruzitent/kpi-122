from time import time_ns

from PySide6.QtCore import QEvent
from PySide6.QtSql import QSqlRelation
from PySide6.QtWidgets import QHeaderView, QWidget

from src.components.database import db
from src.components.multithreading import Worker, pool
from src.components.qtable_model import DairyDelegate, QTableModel
from src.components.user_stats import UserStats
from src.config import consts
from src.ui.home_ui import Ui_Form
from src.utils.error_handlers import qt_error_handler
from src.utils.logger import Logger
from src.utils.verifier import verify_profile

log = Logger(__name__)


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._user = None
        self._interval = consts.SECONDS_IN_DAY * 1e9  # noqa: WPS432

        self.ui.button_update_submit.clicked.connect(self.update_profile)
        self.ui.button_dairy_refresh.clicked.connect(self._get_left_calories)

        self.ui.table_wiki.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_dairy.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_wiki.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.table_dairy.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def changeEvent(self, event):
        if event.type() == QEvent.LanguageChange and self._user:
            return self.refresh()

        return super().changeEvent(event)

    def on_reject(self, err_msg):
        qt_error_handler(self, err_msg)

    def refresh(self, user=None):
        log.warning("refresh")

        if self._user:
            self.ui.button_wiki_add.clicked.disconnect()
            self.ui.button_dairy_add.clicked.disconnect()
            self.ui.button_wiki_remove.clicked.disconnect()
            self.ui.button_dairy_remove.clicked.disconnect()

        if user is not None:
            self._user = UserStats(**user)

        self.home()
        self.wiki()
        self.dairy()

    def update_profile(self):
        try:
            profile = verify_profile(
                weight=self.ui.spinbox_update_weight,
                height=self.ui.spinbox_update_height,
                activity=self.ui.combobox_update_activity,
            )
        except ValueError as err:
            return qt_error_handler(self, err.args[0])

        worker = Worker(db.update_user, self._user.username, *profile.values())
        worker.signals.resolve.connect(self.refresh)
        worker.signals.reject.connect(self.on_reject)
        pool.run(worker)

    def home(self):
        sex = consts.sexes[self._user.sex]["type"]()
        activity = consts.activities[self._user.activity]["type"]()
        goal = consts.goals[self._user.goal]["type"]()
        category = consts.categories[self._user.category]["type"]()

        self.ui.label_home_firstname.setText(self._user.firstname.capitalize())
        self.ui.label_home_lastname.setText(self._user.lastname.capitalize())
        self.ui.label_home_username.setText(self._user.username)
        self.ui.label_home_weight_data.setText(str(self._user.weight))
        self.ui.label_home_height_data.setText(str(self._user.height))
        self.ui.label_home_age_data.setText(str(self._user.age))
        self.ui.label_home_sex_data.setText(sex)
        self.ui.label_home_activity_data.setText(activity)
        self.ui.label_home_bmi_data.setText(str(self._user.bmi))
        self.ui.label_home_goal_data.setText(goal)
        self.ui.label_home_category_data.setText(category)
        self.ui.label_home_bmr_data.setText(str(self._user.bmr))
        self.ui.label_home_calories_data.setText(str(self._user.calories))
        self.ui.label_home_protein_data.setText(str(self._user.protein))
        self.ui.label_home_fat_data.setText(str(self._user.fat))
        self.ui.label_home_carbohydrate_data.setText(str(self._user.carbohydrate))

        self.ui.spinbox_update_weight.setValue(self._user.weight)
        self.ui.spinbox_update_height.setValue(self._user.height)
        self.ui.combobox_update_activity.setCurrentIndex(self._user.activity)

    def wiki(self):
        def on_resolve(table):
            self.ui.table_wiki.setModel(table.model)
            self.ui.table_wiki.setColumnHidden(5, True)  # noqa: WPS425
            self.ui.table_wiki.setColumnHidden(6, True)  # noqa: WPS425

            table.signals.on_update.connect(self.refresh)

            self.ui.button_wiki_add.clicked.connect(
                lambda: table.add_row([6, self._user.username])
            )
            self.ui.button_wiki_remove.clicked.connect(table.remove_row)

        worker = Worker(
            QTableModel,
            view=self.ui.table_wiki,
            db=db.qt_db,
            table="products",
            query=f"products.owner = '{self._user.username}'",  # noqa: WPS237
        )
        worker.signals.resolve.connect(on_resolve)
        worker.signals.reject.connect(self.on_reject)
        pool.run(worker)

    def _get_left_calories(self):
        def normalize(product, prop):
            return product[prop] * product["weight"] / 100

        def prettify(num):
            return str(round(num, 2))

        def on_resolve(eaten):
            calories = self._user.calories
            protein = self._user.protein
            fat = self._user.fat
            carbohydrate = self._user.carbohydrate

            for product in eaten:
                calories -= normalize(product, "calories")
                protein -= normalize(product, "protein")
                fat -= normalize(product, "fat")
                carbohydrate -= normalize(product, "carbohydrate")

            if min([calories, protein, fat, carbohydrate]) > 0:
                self.ui.button_dairy_add.setEnabled(True)
            else:
                self.ui.button_dairy_add.setDisabled(True)

            self.ui.label_dairy_calories_data.setText(prettify(calories))
            self.ui.label_dairy_protein_data.setText(prettify(protein))
            self.ui.label_dairy_fat_data.setText(prettify(fat))
            self.ui.label_dairy_carbohydrate_data.setText(prettify(carbohydrate))

        worker = Worker(db.get_eaten_products, self._user.username, self._interval)
        worker.signals.resolve.connect(on_resolve)
        worker.signals.reject.connect(self.on_reject)
        pool.run(worker)

    def dairy(self):
        self._get_left_calories()

        def on_resolve(table):
            self.ui.table_dairy.setModel(table.model)
            self.ui.table_dairy.setColumnHidden(3, True)  # noqa: WPS425
            self.ui.table_dairy.setColumnHidden(4, True)  # noqa: WPS425

            delegate = DairyDelegate(
                parent=self.ui.table_dairy,
                query=f"products.owner = '{self._user.username}'",  # noqa: WPS237
            )
            self.ui.table_dairy.setItemDelegate(delegate)

            table.signals.on_update.connect(self._get_left_calories)
            delegate.signals.on_update.connect(self._get_left_calories)

            self.ui.button_dairy_add.clicked.connect(
                lambda: table.add_row([2, time_ns()], [4, self._user.username])
            )
            self.ui.button_dairy_remove.clicked.connect(table.remove_row)

        worker = Worker(
            QTableModel,
            view=self.ui.table_dairy,
            db=db.qt_db,
            table="users_ate_products",
            query=f"""
                users_ate_products.user_username = '{self._user.username}'
                and users_ate_products.date > {time_ns() - self._interval}
                """,  # noqa: WPS237
            relations=[[0, QSqlRelation("products", "id", "name")]],
        )
        worker.signals.resolve.connect(on_resolve)
        worker.signals.reject.connect(self.on_reject)
        pool.run(worker)
