# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("la calorie")
        self.action_file_exit = QAction(MainWindow)
        self.action_file_exit.setObjectName("action_file_exit")
        # if QT_CONFIG(shortcut)
        self.action_file_exit.setShortcut("Ctrl+Q")
        # endif // QT_CONFIG(shortcut)
        self.action_language_russian = QAction(MainWindow)
        self.action_language_russian.setObjectName("action_language_russian")
        self.action_language_russian.setText(
            "\u0440\u0443\u0441\u0441\u043a\u0438\u0439"
        )
        self.action_language_english = QAction(MainWindow)
        self.action_language_english.setObjectName("action_language_english")
        self.action_language_english.setText("english")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QStackedWidget(self.centralwidget)
        self.container.setObjectName("container")

        self.verticalLayout.addWidget(self.container)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 27))
        font1 = QFont()
        font1.setPointSize(12)
        self.menubar.setFont(font1)
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_view_language = QMenu(self.menu_view)
        self.menu_view_language.setObjectName("menu_view_language")
        self.menu_view_theme = QMenu(self.menu_view)
        self.menu_view_theme.setObjectName("menu_view_theme")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menu_file.addAction(self.action_file_exit)
        self.menu_view.addAction(self.menu_view_language.menuAction())
        self.menu_view.addAction(self.menu_view_theme.menuAction())
        self.menu_view_language.addAction(self.action_language_english)
        self.menu_view_language.addAction(self.action_language_russian)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        self.action_file_exit.setText(
            QCoreApplication.translate("MainWindow", "exit", None)
        )
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", "file", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", "view", None))
        self.menu_view_language.setTitle(
            QCoreApplication.translate("MainWindow", "language", None)
        )
        self.menu_view_theme.setTitle(
            QCoreApplication.translate("MainWindow", "theme", None)
        )
        pass

    # retranslateUi
