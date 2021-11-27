import glob
import os

from src.components.multithreading import pool
from src.utils.logger import Logger

log = Logger(__name__)


def run(cmd):
    log.info(cmd)
    os.system(cmd)


def prettify():
    run("isort ./src")
    run("black ./src --target-version py310")


def get_ui():
    for file in glob.glob(".\\src\\ui\\*.ui"):
        run(f'pyside6-uic -o "{file[:-3]}_ui.py" "{file}"')


def get_ts():
    def get_files(arr):
        files = ["".join(f"./public/i18n/{lang}.ts") for lang in arr]
        return " ".join(files)

    ts_files = get_files(["ru_RU", "en_US"])

    includes = [
        "./src",
        "./public/i18n/errors.py",
        "./public/i18n/translations.py",
        "./src/config/consts.py",
    ]

    run(f"pyside6-lupdate {' '.join(includes)} -ts {ts_files} -noobsolete")
    run(f"pyside6-lrelease {ts_files}")


def entry():
    prettify()
    get_ui()
    get_ts()

    from src.main import main

    log.debug(f"app is running under pid {os.getpid()}")
    log.debug(f"available threads: {pool.get_thread_count()}")

    main()


if __name__ == "__main__":
    entry()
