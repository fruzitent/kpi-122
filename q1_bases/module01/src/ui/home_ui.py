# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QTableView,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1280, 693)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        Form.setFont(font)
        Form.setWindowTitle("Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QTabWidget(Form)
        self.container.setObjectName("container")
        font1 = QFont()
        font1.setPointSize(12)
        self.container.setFont(font1)
        self.container.setTabPosition(QTabWidget.West)
        self.container.setDocumentMode(True)
        self.container.setTabBarAutoHide(False)
        self.container_home = QWidget()
        self.container_home.setObjectName("container_home")
        self.verticalLayout_2 = QVBoxLayout(self.container_home)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 0, 25, 0)
        self.container_home_header = QWidget(self.container_home)
        self.container_home_header.setObjectName("container_home_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.container_home_header.sizePolicy().hasHeightForWidth()
        )
        self.container_home_header.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(48)
        self.container_home_header.setFont(font2)
        self.gridLayout = QGridLayout(self.container_home_header)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.spacer_header = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.spacer_header, 0, 4, 1, 1)

        self.label_home_lastname = QLabel(self.container_home_header)
        self.label_home_lastname.setObjectName("label_home_lastname")
        sizePolicy1.setHeightForWidth(
            self.label_home_lastname.sizePolicy().hasHeightForWidth()
        )
        self.label_home_lastname.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(48)
        font3.setBold(True)
        self.label_home_lastname.setFont(font3)
        self.label_home_lastname.setText("lastname")

        self.gridLayout.addWidget(self.label_home_lastname, 0, 3, 1, 1)

        self.label_home_firstname = QLabel(self.container_home_header)
        self.label_home_firstname.setObjectName("label_home_firstname")
        sizePolicy1.setHeightForWidth(
            self.label_home_firstname.sizePolicy().hasHeightForWidth()
        )
        self.label_home_firstname.setSizePolicy(sizePolicy1)
        self.label_home_firstname.setFont(font3)
        self.label_home_firstname.setText("firstname")

        self.gridLayout.addWidget(self.label_home_firstname, 0, 2, 1, 1)

        self.hr_header = QFrame(self.container_home_header)
        self.hr_header.setObjectName("hr_header")
        self.hr_header.setFrameShape(QFrame.HLine)
        self.hr_header.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.hr_header, 2, 0, 2, 5)

        self.label_home_username = QLabel(self.container_home_header)
        self.label_home_username.setObjectName("label_home_username")
        sizePolicy1.setHeightForWidth(
            self.label_home_username.sizePolicy().hasHeightForWidth()
        )
        self.label_home_username.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(24)
        self.label_home_username.setFont(font4)
        self.label_home_username.setText("username")

        self.gridLayout.addWidget(self.label_home_username, 1, 0, 1, 5)

        self.label_home_welcome = QLabel(self.container_home_header)
        self.label_home_welcome.setObjectName("label_home_welcome")
        sizePolicy1.setHeightForWidth(
            self.label_home_welcome.sizePolicy().hasHeightForWidth()
        )
        self.label_home_welcome.setSizePolicy(sizePolicy1)
        self.label_home_welcome.setFont(font3)

        self.gridLayout.addWidget(self.label_home_welcome, 0, 0, 1, 2)

        self.verticalLayout_2.addWidget(self.container_home_header)

        self.container_home_body = QHBoxLayout()
        self.container_home_body.setSpacing(0)
        self.container_home_body.setObjectName("container_home_body")
        self.container_home_body.setContentsMargins(-1, -1, -1, 15)
        self.container_home_stats = QWidget(self.container_home)
        self.container_home_stats.setObjectName("container_home_stats")
        sizePolicy.setHeightForWidth(
            self.container_home_stats.sizePolicy().hasHeightForWidth()
        )
        self.container_home_stats.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.container_home_stats)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_home_calories_data = QLabel(self.container_home_stats)
        self.label_home_calories_data.setObjectName("label_home_calories_data")
        font5 = QFont()
        font5.setPointSize(14)
        self.label_home_calories_data.setFont(font5)
        self.label_home_calories_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_calories_data, 9, 1, 1, 1)

        self.label_home_goal = QLabel(self.container_home_stats)
        self.label_home_goal.setObjectName("label_home_goal")
        self.label_home_goal.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_goal, 6, 0, 1, 1)

        self.label_home_carbohydrate_data = QLabel(self.container_home_stats)
        self.label_home_carbohydrate_data.setObjectName("label_home_carbohydrate_data")
        self.label_home_carbohydrate_data.setFont(font5)
        self.label_home_carbohydrate_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_carbohydrate_data, 12, 1, 1, 1)

        self.label_home_protein = QLabel(self.container_home_stats)
        self.label_home_protein.setObjectName("label_home_protein")
        self.label_home_protein.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_protein, 10, 0, 1, 1)

        self.label_home_category = QLabel(self.container_home_stats)
        self.label_home_category.setObjectName("label_home_category")
        self.label_home_category.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_category, 7, 0, 1, 1)

        self.label_home_bmr_data = QLabel(self.container_home_stats)
        self.label_home_bmr_data.setObjectName("label_home_bmr_data")
        self.label_home_bmr_data.setFont(font5)
        self.label_home_bmr_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_bmr_data, 8, 1, 1, 1)

        self.label_home_carbohydrate = QLabel(self.container_home_stats)
        self.label_home_carbohydrate.setObjectName("label_home_carbohydrate")
        self.label_home_carbohydrate.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_carbohydrate, 12, 0, 1, 1)

        self.label_home_bmi = QLabel(self.container_home_stats)
        self.label_home_bmi.setObjectName("label_home_bmi")
        self.label_home_bmi.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_bmi, 5, 0, 1, 1)

        self.label_home_calories = QLabel(self.container_home_stats)
        self.label_home_calories.setObjectName("label_home_calories")
        self.label_home_calories.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_calories, 9, 0, 1, 1)

        self.label_home_activity_data = QLabel(self.container_home_stats)
        self.label_home_activity_data.setObjectName("label_home_activity_data")
        self.label_home_activity_data.setFont(font5)
        self.label_home_activity_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_activity_data, 4, 1, 1, 1)

        self.label_home_bmr = QLabel(self.container_home_stats)
        self.label_home_bmr.setObjectName("label_home_bmr")
        self.label_home_bmr.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_bmr, 8, 0, 1, 1)

        self.label_home_weight_data = QLabel(self.container_home_stats)
        self.label_home_weight_data.setObjectName("label_home_weight_data")
        self.label_home_weight_data.setFont(font5)
        self.label_home_weight_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_weight_data, 0, 1, 1, 1)

        self.label_home_age = QLabel(self.container_home_stats)
        self.label_home_age.setObjectName("label_home_age")
        self.label_home_age.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_age, 2, 0, 1, 1)

        self.label_home_fat = QLabel(self.container_home_stats)
        self.label_home_fat.setObjectName("label_home_fat")
        self.label_home_fat.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_fat, 11, 0, 1, 1)

        self.label_home_activity = QLabel(self.container_home_stats)
        self.label_home_activity.setObjectName("label_home_activity")
        self.label_home_activity.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_activity, 4, 0, 1, 1)

        self.label_home_sex = QLabel(self.container_home_stats)
        self.label_home_sex.setObjectName("label_home_sex")
        self.label_home_sex.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_sex, 3, 0, 1, 1)

        self.label_home_height = QLabel(self.container_home_stats)
        self.label_home_height.setObjectName("label_home_height")
        self.label_home_height.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_height, 1, 0, 1, 1)

        self.label_home_height_data = QLabel(self.container_home_stats)
        self.label_home_height_data.setObjectName("label_home_height_data")
        self.label_home_height_data.setFont(font5)
        self.label_home_height_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_height_data, 1, 1, 1, 1)

        self.label_home_bmi_data = QLabel(self.container_home_stats)
        self.label_home_bmi_data.setObjectName("label_home_bmi_data")
        self.label_home_bmi_data.setFont(font5)
        self.label_home_bmi_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_bmi_data, 5, 1, 1, 1)

        self.label_home_weight = QLabel(self.container_home_stats)
        self.label_home_weight.setObjectName("label_home_weight")
        self.label_home_weight.setFont(font5)

        self.gridLayout_3.addWidget(self.label_home_weight, 0, 0, 1, 1)

        self.label_home_fat_data = QLabel(self.container_home_stats)
        self.label_home_fat_data.setObjectName("label_home_fat_data")
        self.label_home_fat_data.setFont(font5)
        self.label_home_fat_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_fat_data, 11, 1, 1, 1)

        self.label_home_sex_data = QLabel(self.container_home_stats)
        self.label_home_sex_data.setObjectName("label_home_sex_data")
        self.label_home_sex_data.setFont(font5)
        self.label_home_sex_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_sex_data, 3, 1, 1, 1)

        self.label_home_protein_data = QLabel(self.container_home_stats)
        self.label_home_protein_data.setObjectName("label_home_protein_data")
        self.label_home_protein_data.setFont(font5)
        self.label_home_protein_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_protein_data, 10, 1, 1, 1)

        self.label_home_category_data = QLabel(self.container_home_stats)
        self.label_home_category_data.setObjectName("label_home_category_data")
        self.label_home_category_data.setFont(font5)
        self.label_home_category_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_category_data, 7, 1, 1, 1)

        self.label_home_goal_data = QLabel(self.container_home_stats)
        self.label_home_goal_data.setObjectName("label_home_goal_data")
        self.label_home_goal_data.setFont(font5)
        self.label_home_goal_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_goal_data, 6, 1, 1, 1)

        self.label_home_age_data = QLabel(self.container_home_stats)
        self.label_home_age_data.setObjectName("label_home_age_data")
        self.label_home_age_data.setFont(font5)
        self.label_home_age_data.setText("")

        self.gridLayout_3.addWidget(self.label_home_age_data, 2, 1, 1, 1)

        self.container_home_body.addWidget(self.container_home_stats)

        self.hr_body = QFrame(self.container_home)
        self.hr_body.setObjectName("hr_body")
        self.hr_body.setFrameShape(QFrame.VLine)
        self.hr_body.setFrameShadow(QFrame.Raised)

        self.container_home_body.addWidget(self.hr_body)

        self.container_home_update = QWidget(self.container_home)
        self.container_home_update.setObjectName("container_home_update")
        sizePolicy.setHeightForWidth(
            self.container_home_update.sizePolicy().hasHeightForWidth()
        )
        self.container_home_update.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.container_home_update)
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_home_update = QLabel(self.container_home_update)
        self.label_home_update.setObjectName("label_home_update")
        font6 = QFont()
        font6.setPointSize(36)
        self.label_home_update.setFont(font6)
        self.label_home_update.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_home_update)

        self.container_update_inputs = QWidget(self.container_home_update)
        self.container_update_inputs.setObjectName("container_update_inputs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.container_update_inputs.sizePolicy().hasHeightForWidth()
        )
        self.container_update_inputs.setSizePolicy(sizePolicy2)
        self.gridLayout_2 = QGridLayout(self.container_update_inputs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(100, -1, 100, -1)
        self.label_update_weight = QLabel(self.container_update_inputs)
        self.label_update_weight.setObjectName("label_update_weight")
        self.label_update_weight.setFont(font5)

        self.gridLayout_2.addWidget(self.label_update_weight, 0, 0, 1, 1)

        self.spinbox_update_weight = QSpinBox(self.container_update_inputs)
        self.spinbox_update_weight.setObjectName("spinbox_update_weight")
        sizePolicy1.setHeightForWidth(
            self.spinbox_update_weight.sizePolicy().hasHeightForWidth()
        )
        self.spinbox_update_weight.setSizePolicy(sizePolicy1)
        self.spinbox_update_weight.setMaximum(250)

        self.gridLayout_2.addWidget(self.spinbox_update_weight, 0, 1, 1, 1)

        self.label_update_height = QLabel(self.container_update_inputs)
        self.label_update_height.setObjectName("label_update_height")
        self.label_update_height.setFont(font5)

        self.gridLayout_2.addWidget(self.label_update_height, 1, 0, 1, 1)

        self.spinbox_update_height = QSpinBox(self.container_update_inputs)
        self.spinbox_update_height.setObjectName("spinbox_update_height")
        self.spinbox_update_height.setMaximum(250)

        self.gridLayout_2.addWidget(self.spinbox_update_height, 1, 1, 1, 1)

        self.label_update_activity = QLabel(self.container_update_inputs)
        self.label_update_activity.setObjectName("label_update_activity")
        self.label_update_activity.setFont(font5)

        self.gridLayout_2.addWidget(self.label_update_activity, 2, 0, 1, 1)

        self.combobox_update_activity = QComboBox(self.container_update_inputs)
        self.combobox_update_activity.addItem("")
        self.combobox_update_activity.addItem("")
        self.combobox_update_activity.addItem("")
        self.combobox_update_activity.addItem("")
        self.combobox_update_activity.addItem("")
        self.combobox_update_activity.setObjectName("combobox_update_activity")

        self.gridLayout_2.addWidget(self.combobox_update_activity, 2, 1, 1, 1)

        self.verticalLayout_3.addWidget(self.container_update_inputs)

        self.container_update_footer = QHBoxLayout()
        self.container_update_footer.setObjectName("container_update_footer")
        self.container_update_footer.setContentsMargins(-1, 0, -1, -1)
        self.button_update_submit = QPushButton(self.container_home_update)
        self.button_update_submit.setObjectName("button_update_submit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.button_update_submit.sizePolicy().hasHeightForWidth()
        )
        self.button_update_submit.setSizePolicy(sizePolicy3)
        # if QT_CONFIG(shortcut)
        self.button_update_submit.setShortcut("Ctrl+R")
        # endif // QT_CONFIG(shortcut)
        self.button_update_submit.setCheckable(False)

        self.container_update_footer.addWidget(self.button_update_submit)

        self.verticalLayout_3.addLayout(self.container_update_footer)

        self.spacer_update = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.spacer_update)

        self.container_home_body.addWidget(self.container_home_update)

        self.verticalLayout_2.addLayout(self.container_home_body)

        self.container.addTab(self.container_home, "")
        self.container_wiki = QWidget()
        self.container_wiki.setObjectName("container_wiki")
        self.layout_wiki = QGridLayout(self.container_wiki)
        self.layout_wiki.setSpacing(0)
        self.layout_wiki.setObjectName("layout_wiki")
        self.layout_wiki.setContentsMargins(0, 0, 0, 0)
        self.table_wiki = QTableView(self.container_wiki)
        self.table_wiki.setObjectName("table_wiki")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.table_wiki.sizePolicy().hasHeightForWidth())
        self.table_wiki.setSizePolicy(sizePolicy4)
        self.table_wiki.setLineWidth(1)
        self.table_wiki.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_wiki.setAlternatingRowColors(True)
        self.table_wiki.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_wiki.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_wiki.setSortingEnabled(True)
        self.table_wiki.verticalHeader().setMinimumSectionSize(50)
        self.table_wiki.verticalHeader().setProperty("showSortIndicator", False)

        self.layout_wiki.addWidget(self.table_wiki, 0, 0, 1, 5)

        self.container_wiki_footer = QHBoxLayout()
        self.container_wiki_footer.setSpacing(15)
        self.container_wiki_footer.setObjectName("container_wiki_footer")
        self.spacer_wiki = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.container_wiki_footer.addItem(self.spacer_wiki)

        self.button_wiki_add = QPushButton(self.container_wiki)
        self.button_wiki_add.setObjectName("button_wiki_add")
        # if QT_CONFIG(shortcut)
        self.button_wiki_add.setShortcut("Ctrl+N")
        # endif // QT_CONFIG(shortcut)

        self.container_wiki_footer.addWidget(self.button_wiki_add)

        self.button_wiki_remove = QPushButton(self.container_wiki)
        self.button_wiki_remove.setObjectName("button_wiki_remove")
        # if QT_CONFIG(shortcut)
        self.button_wiki_remove.setShortcut("Del")
        # endif // QT_CONFIG(shortcut)

        self.container_wiki_footer.addWidget(self.button_wiki_remove)

        self.layout_wiki.addLayout(self.container_wiki_footer, 2, 0, 1, 1)

        self.container.addTab(self.container_wiki, "")
        self.container_diary = QWidget()
        self.container_diary.setObjectName("container_diary")
        self.layout_dairy = QGridLayout(self.container_diary)
        self.layout_dairy.setSpacing(0)
        self.layout_dairy.setObjectName("layout_dairy")
        self.layout_dairy.setContentsMargins(0, 0, 0, 0)
        self.table_dairy = QTableView(self.container_diary)
        self.table_dairy.setObjectName("table_dairy")
        self.table_dairy.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_dairy.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_dairy.setSortingEnabled(True)
        self.table_dairy.verticalHeader().setMinimumSectionSize(50)

        self.layout_dairy.addWidget(self.table_dairy, 0, 0, 1, 1)

        self.container_dairy_footer = QHBoxLayout()
        self.container_dairy_footer.setSpacing(15)
        self.container_dairy_footer.setObjectName("container_dairy_footer")
        self.container_dairy_footer.setContentsMargins(-1, 0, -1, -1)
        self.label_dairy_calories = QLabel(self.container_diary)
        self.label_dairy_calories.setObjectName("label_dairy_calories")

        self.container_dairy_footer.addWidget(self.label_dairy_calories)

        self.label_dairy_calories_data = QLabel(self.container_diary)
        self.label_dairy_calories_data.setObjectName("label_dairy_calories_data")
        self.label_dairy_calories_data.setText("")

        self.container_dairy_footer.addWidget(self.label_dairy_calories_data)

        self.label_dairy_protein = QLabel(self.container_diary)
        self.label_dairy_protein.setObjectName("label_dairy_protein")

        self.container_dairy_footer.addWidget(self.label_dairy_protein)

        self.label_dairy_protein_data = QLabel(self.container_diary)
        self.label_dairy_protein_data.setObjectName("label_dairy_protein_data")
        self.label_dairy_protein_data.setText("")

        self.container_dairy_footer.addWidget(self.label_dairy_protein_data)

        self.label_dairy_fat = QLabel(self.container_diary)
        self.label_dairy_fat.setObjectName("label_dairy_fat")

        self.container_dairy_footer.addWidget(self.label_dairy_fat)

        self.label_dairy_fat_data = QLabel(self.container_diary)
        self.label_dairy_fat_data.setObjectName("label_dairy_fat_data")
        self.label_dairy_fat_data.setText("")

        self.container_dairy_footer.addWidget(self.label_dairy_fat_data)

        self.label_dairy_carbohydrate = QLabel(self.container_diary)
        self.label_dairy_carbohydrate.setObjectName("label_dairy_carbohydrate")

        self.container_dairy_footer.addWidget(self.label_dairy_carbohydrate)

        self.label_dairy_carbohydrate_data = QLabel(self.container_diary)
        self.label_dairy_carbohydrate_data.setObjectName(
            "label_dairy_carbohydrate_data"
        )
        self.label_dairy_carbohydrate_data.setText("")

        self.container_dairy_footer.addWidget(self.label_dairy_carbohydrate_data)

        self.spacer_dairy = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.container_dairy_footer.addItem(self.spacer_dairy)

        self.button_dairy_refresh = QPushButton(self.container_diary)
        self.button_dairy_refresh.setObjectName("button_dairy_refresh")
        # if QT_CONFIG(shortcut)
        self.button_dairy_refresh.setShortcut("Ctrl+R")
        # endif // QT_CONFIG(shortcut)
        self.button_dairy_refresh.setAutoRepeat(False)

        self.container_dairy_footer.addWidget(self.button_dairy_refresh)

        self.button_dairy_add = QPushButton(self.container_diary)
        self.button_dairy_add.setObjectName("button_dairy_add")
        # if QT_CONFIG(shortcut)
        self.button_dairy_add.setShortcut("Ctrl+N")
        # endif // QT_CONFIG(shortcut)

        self.container_dairy_footer.addWidget(self.button_dairy_add)

        self.button_dairy_remove = QPushButton(self.container_diary)
        self.button_dairy_remove.setObjectName("button_dairy_remove")
        # if QT_CONFIG(shortcut)
        self.button_dairy_remove.setShortcut("Del")
        # endif // QT_CONFIG(shortcut)

        self.container_dairy_footer.addWidget(self.button_dairy_remove)

        self.layout_dairy.addLayout(self.container_dairy_footer, 1, 0, 1, 1)

        self.container.addTab(self.container_diary, "")

        self.verticalLayout.addWidget(self.container)

        self.retranslateUi(Form)

        self.container.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        self.label_home_welcome.setText(
            QCoreApplication.translate("Form", "welcome,", None)
        )
        self.label_home_goal.setText(QCoreApplication.translate("Form", "goal", None))
        self.label_home_protein.setText(
            QCoreApplication.translate("Form", "protein", None)
        )
        self.label_home_category.setText(
            QCoreApplication.translate("Form", "category", None)
        )
        self.label_home_carbohydrate.setText(
            QCoreApplication.translate("Form", "carbohydrate", None)
        )
        self.label_home_bmi.setText(QCoreApplication.translate("Form", "bmi", None))
        self.label_home_calories.setText(
            QCoreApplication.translate("Form", "calories", None)
        )
        self.label_home_bmr.setText(QCoreApplication.translate("Form", "bmr", None))
        self.label_home_age.setText(QCoreApplication.translate("Form", "age", None))
        self.label_home_fat.setText(QCoreApplication.translate("Form", "fat", None))
        self.label_home_activity.setText(
            QCoreApplication.translate("Form", "activity", None)
        )
        self.label_home_sex.setText(QCoreApplication.translate("Form", "sex", None))
        self.label_home_height.setText(
            QCoreApplication.translate("Form", "height", None)
        )
        self.label_home_weight.setText(
            QCoreApplication.translate("Form", "weight", None)
        )
        self.label_home_update.setText(
            QCoreApplication.translate("Form", "update profile", None)
        )
        self.label_update_weight.setText(
            QCoreApplication.translate("Form", "weight", None)
        )
        self.label_update_height.setText(
            QCoreApplication.translate("Form", "height", None)
        )
        self.label_update_activity.setText(
            QCoreApplication.translate("Form", "activity", None)
        )
        self.combobox_update_activity.setItemText(
            0, QCoreApplication.translate("Form", "low", None)
        )
        self.combobox_update_activity.setItemText(
            1, QCoreApplication.translate("Form", "moderate", None)
        )
        self.combobox_update_activity.setItemText(
            2, QCoreApplication.translate("Form", "average", None)
        )
        self.combobox_update_activity.setItemText(
            3, QCoreApplication.translate("Form", "high", None)
        )
        self.combobox_update_activity.setItemText(
            4, QCoreApplication.translate("Form", "abnormal", None)
        )

        self.button_update_submit.setText(
            QCoreApplication.translate("Form", "submit", None)
        )
        self.container.setTabText(
            self.container.indexOf(self.container_home),
            QCoreApplication.translate("Form", "home", None),
        )
        self.button_wiki_add.setText(QCoreApplication.translate("Form", "add", None))
        self.button_wiki_remove.setText(
            QCoreApplication.translate("Form", "remove", None)
        )
        self.container.setTabText(
            self.container.indexOf(self.container_wiki),
            QCoreApplication.translate("Form", "wiki", None),
        )
        self.label_dairy_calories.setText(
            QCoreApplication.translate("Form", "calories", None)
        )
        self.label_dairy_protein.setText(
            QCoreApplication.translate("Form", "protein", None)
        )
        self.label_dairy_fat.setText(QCoreApplication.translate("Form", "fat", None))
        self.label_dairy_carbohydrate.setText(
            QCoreApplication.translate("Form", "carbohydrate", None)
        )
        self.button_dairy_refresh.setText(
            QCoreApplication.translate("Form", "refresh", None)
        )
        self.button_dairy_add.setText(QCoreApplication.translate("Form", "add", None))
        self.button_dairy_remove.setText(
            QCoreApplication.translate("Form", "remove", None)
        )
        self.container.setTabText(
            self.container.indexOf(self.container_diary),
            QCoreApplication.translate("Form", "diary", None),
        )
        pass

    # retranslateUi
