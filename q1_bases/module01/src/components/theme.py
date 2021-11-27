import darkdetect
from PySide6.QtGui import QFontDatabase, QIcon
from qt_material import apply_stylesheet

from src.config import config
from src.utils.logger import Logger

log = Logger(__name__)


class Theme:
    def __init__(self, app):
        self.app = app
        self.pref_mode = darkdetect.theme().lower() or "dark"

        QFontDatabase.addApplicationFont(config.FONT_PATH)

        self.app.setStyle("fusion")
        self.set_theme(f"{self.pref_mode}_amber.xml")

    def set_theme(self, theme, font=config.FONT):
        invert = "light" in theme
        apply_stylesheet(self.app, theme=theme, invert_secondary=invert)
        log.debug(f"app theme is set to {theme}")

        icon = config.LOGO_LIGHT_PATH  # if invert else config.LOGO_DARK_PATH
        self.app.setWindowIcon(QIcon(icon))
        log.debug(f"app icon is set to {icon}")

        self.app.setFont(font)
        log.debug(f"app font is set to {config.FONT}")
