# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QGridLayout,
    QHBoxLayout, QHeaderView, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, CheckBox, HyperlinkLabel,
    LineEdit, ListWidget, PrimaryPushButton, ProgressBar,
    PushButton, SimpleCardWidget, StrongBodyLabel, SubtitleLabel,
    SwitchButton, TableWidget, TextEdit, ToggleButton,
    ToolButton)
import src.templates.resourse_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1299, 797)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QMenuBar{\n"
"	\n"
"	background-color: rgb(212, 212, 212);\n"
"	\n"
"}\n"
"QMenuBar::item{\n"
"	padding: 6px;\n"
"	margin:4px;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QMenuBar::item::selected {\n"
"	\n"
"	background-color: rgb(181, 181, 181);\n"
"	\n"
"}")
        self.about_project_reference = QAction(MainWindow)
        self.about_project_reference.setObjectName(u"about_project_reference")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.navigation_bar = QWidget(self.centralwidget)
        self.navigation_bar.setObjectName(u"navigation_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navigation_bar.sizePolicy().hasHeightForWidth())
        self.navigation_bar.setSizePolicy(sizePolicy)
        self.navigation_bar.setMaximumSize(QSize(750, 16777215))
        self.navigation_bar.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.verticalLayout = QVBoxLayout(self.navigation_bar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.collect_results_item = QPushButton(self.navigation_bar)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.collect_results_item)
        self.collect_results_item.setObjectName(u"collect_results_item")
        self.collect_results_item.setCursor(QCursor(Qt.PointingHandCursor))
        self.collect_results_item.setStyleSheet(u"QPushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    outline: none;\n"
"padding:10px;\n"
"text-align: left;\n"
"\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"QPushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 0px;\n"
"}\n"
"\n"
"QPushButton[hasIcon=true] {\n"
"    padding: 6px 0px 6px 6px;\n"
"\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5px 31px 6px 36px;\n"
"}\n"
"\n"
"\n"
"\n"
"ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    back\n"
"      "
                        "                  ground: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"QPushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked ,\n"
"QPushButton:checked {\n"
"    color: black;\n"
"	\n"
"	background-color: rgb(212, 212, 212);\n"
"    border: 1px solid  rgb(165, 165, 165);\n"
"    border-bottom: 1px solid  rgb(165, 165, 165);\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover,{\n"
"    color: black;\n"
"	background-color: rgb(217, 220, 234);\n"
"    border: 1px solid  rgb(217, 220, 234);\n"
"    border-bottom: 1px solid  rgb(217, 220, 234);\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed,QPushBut"
                        "ton:pressed {\n"
"\n"
"                            color: black;\n"
"\n"
"	background-color: rgb(219, 222, 236);\n"
"    border: 1px solid  rgb(217, 220, 234);\n"
"    border-bottom: 1px solid  rgb(217, 220, 234);\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled,QPushButton:disabled{\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
""
                        "}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"\n"
"                            border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=false] {\n"
"    padding: 6px 12px 6px 12px;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=true] {\n"
"    padding: 6px 12px 6px 36px;\n"
"}\n"
"\n"
"HyperlinkButton:hover {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
""
                        "HyperlinkButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.43);\n"
"    back\n"
"                        ground-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"RadioButton {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    background-color: transparent;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"    color: black;\n"
"}\n"
"\n"
"RadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #999999;\n"
"    background-color: rgba(0, 0, 0, 5);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"RadioButton::indicator:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"RadioButton::indicator:pressed {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(225, 224, 223),\n"
"            stop:1 rgb(225, 224, 2"
                        "23));\n"
"}\n"
"\n"
"RadioButton::indicator:checked {\n"
"    height: 22px;\n"
"    width: 22px;\n"
"   \n"
"                         border: none;\n"
"    border-radius: 11px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"        "
                        "    stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"RadioButton::indicator:d\n"
"                        isabled {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RadioButton::indicator:disabled:checked {\n"
"    border: none;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
"            stop:1 rgba(0, 0, 0, 0.2169));\n"
"}\n"
"\n"
"TransparentToolButton,\n"
"TransparentToggleToolButton,\n"
"TransparentDropDownToolButton,\n"
"TransparentPushButton,\n"
"TransparentDropDownPushButton,\n"
"TransparentTogglePushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"TransparentToolButton:hover,\n"
"TransparentToggleToolButton:hover,\n"
"TransparentDropDownToo"
                        "lButton:hover,\n"
"TransparentPushButton:hover,\n"
"TransparentDropDownPushButton:hover,\n"
"TransparentTogglePushButton:hover {\n"
"    background-color: rgba(0,\n"
"                         0, 0, 9);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:pressed,\n"
"TransparentToggleToolButton:pressed,\n"
"TransparentDropDownToolButton:pressed,\n"
"TransparentPushButton:pressed,\n"
"TransparentDropDownPushButton:pressed,\n"
"TransparentTogglePushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:disabled,\n"
"TransparentToggleToolButton:disabled,\n"
"TransparentDropDownToolButton:disabled,\n"
"TransprentPushButton:disabled,\n"
"TransparentDropDownPushButton:disabled,\n"
"TransprentTogglePushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"PillPushButton,\n"
"PillPushButton:hover,\n"
"PillPushButton:pressed,\n"
"PillPushButton:disabled,\n"
"PillPushButton:checked,\n"
"PillPushButton:chec"
                        "ked:hover,\n"
"PillPushButton:checked:pressed,\n"
"PillPushButton:disabled:checked,\n"
"PillToolButton,\n"
"PillToolButton:hover,\n"
"PillToolButton:pressed,\n"
"PillToolButton:disabled,\n"
"\n"
"                        PillToolButton:checked,\n"
"PillToolButton:checked:hover,\n"
"PillToolButton:checked:pressed,\n"
"PillToolButton:disabled:checked {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/images/copy-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.collect_results_item.setIcon(icon)
        self.collect_results_item.setIconSize(QSize(20, 20))
        self.collect_results_item.setCheckable(True)
        self.collect_results_item.setChecked(True)

        self.verticalLayout.addWidget(self.collect_results_item)

        self.preview_item = QPushButton(self.navigation_bar)
        self.buttonGroup.addButton(self.preview_item)
        self.preview_item.setObjectName(u"preview_item")
        self.preview_item.setCursor(QCursor(Qt.PointingHandCursor))
        self.preview_item.setStyleSheet(u"QPushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    outline: none;\n"
"padding:10px;\n"
"text-align: left;\n"
"\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"QPushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 0px;\n"
"}\n"
"\n"
"QPushButton[hasIcon=true] {\n"
"    padding: 6px 0px 6px 6px;\n"
"\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5px 31px 6px 36px;\n"
"}\n"
"\n"
"\n"
"\n"
"ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    back\n"
"      "
                        "                  ground: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"QPushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked ,\n"
"QPushButton:checked {\n"
"    color: black;\n"
"	\n"
"	background-color: rgb(212, 212, 212);\n"
"    border: 1px solid  rgb(165, 165, 165);\n"
"    border-bottom: 1px solid  rgb(165, 165, 165);\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover,{\n"
"    color: black;\n"
"	background-color: rgb(217, 220, 234);\n"
"    border: 1px solid  rgb(217, 220, 234);\n"
"    border-bottom: 1px solid  rgb(217, 220, 234);\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed,QPushBut"
                        "ton:pressed {\n"
"\n"
"                            color: black;\n"
"\n"
"	background-color: rgb(219, 222, 236);\n"
"    border: 1px solid  rgb(217, 220, 234);\n"
"    border-bottom: 1px solid  rgb(217, 220, 234);\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled,QPushButton:disabled{\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
""
                        "}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"\n"
"                            border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=false] {\n"
"    padding: 6px 12px 6px 12px;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=true] {\n"
"    padding: 6px 12px 6px 36px;\n"
"}\n"
"\n"
"HyperlinkButton:hover {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
""
                        "HyperlinkButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.43);\n"
"    back\n"
"                        ground-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"RadioButton {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    background-color: transparent;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"    color: black;\n"
"}\n"
"\n"
"RadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #999999;\n"
"    background-color: rgba(0, 0, 0, 5);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"RadioButton::indicator:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"RadioButton::indicator:pressed {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(225, 224, 223),\n"
"            stop:1 rgb(225, 224, 2"
                        "23));\n"
"}\n"
"\n"
"RadioButton::indicator:checked {\n"
"    height: 22px;\n"
"    width: 22px;\n"
"   \n"
"                         border: none;\n"
"    border-radius: 11px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"        "
                        "    stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"RadioButton::indicator:d\n"
"                        isabled {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RadioButton::indicator:disabled:checked {\n"
"    border: none;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
"            stop:1 rgba(0, 0, 0, 0.2169));\n"
"}\n"
"\n"
"TransparentToolButton,\n"
"TransparentToggleToolButton,\n"
"TransparentDropDownToolButton,\n"
"TransparentPushButton,\n"
"TransparentDropDownPushButton,\n"
"TransparentTogglePushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"TransparentToolButton:hover,\n"
"TransparentToggleToolButton:hover,\n"
"TransparentDropDownToo"
                        "lButton:hover,\n"
"TransparentPushButton:hover,\n"
"TransparentDropDownPushButton:hover,\n"
"TransparentTogglePushButton:hover {\n"
"    background-color: rgba(0,\n"
"                         0, 0, 9);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:pressed,\n"
"TransparentToggleToolButton:pressed,\n"
"TransparentDropDownToolButton:pressed,\n"
"TransparentPushButton:pressed,\n"
"TransparentDropDownPushButton:pressed,\n"
"TransparentTogglePushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:disabled,\n"
"TransparentToggleToolButton:disabled,\n"
"TransparentDropDownToolButton:disabled,\n"
"TransprentPushButton:disabled,\n"
"TransparentDropDownPushButton:disabled,\n"
"TransprentTogglePushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"PillPushButton,\n"
"PillPushButton:hover,\n"
"PillPushButton:pressed,\n"
"PillPushButton:disabled,\n"
"PillPushButton:checked,\n"
"PillPushButton:chec"
                        "ked:hover,\n"
"PillPushButton:checked:pressed,\n"
"PillPushButton:disabled:checked,\n"
"PillToolButton,\n"
"PillToolButton:hover,\n"
"PillToolButton:pressed,\n"
"PillToolButton:disabled,\n"
"\n"
"                        PillToolButton:checked,\n"
"PillToolButton:checked:hover,\n"
"PillToolButton:checked:pressed,\n"
"PillToolButton:disabled:checked {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/prevlooked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.preview_item.setIcon(icon1)
        self.preview_item.setIconSize(QSize(20, 20))
        self.preview_item.setCheckable(True)
        self.preview_item.setChecked(False)

        self.verticalLayout.addWidget(self.preview_item)

        self.convert_item = QPushButton(self.navigation_bar)
        self.buttonGroup.addButton(self.convert_item)
        self.convert_item.setObjectName(u"convert_item")
        self.convert_item.setCursor(QCursor(Qt.PointingHandCursor))
        self.convert_item.setStyleSheet(u"QPushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    outline: none;\n"
"padding:10px;\n"
"text-align: left;\n"
"\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"QPushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 0px;\n"
"}\n"
"\n"
"QPushButton[hasIcon=true] {\n"
"    padding: 6px 0px 6px 6px;\n"
"\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5px 31px 6px 36px;\n"
"}\n"
"\n"
"\n"
"\n"
"ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    back\n"
"      "
                        "                  ground: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"QPushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked ,\n"
"QPushButton:checked {\n"
"    color: black;\n"
"	\n"
"	background-color: rgb(212, 212, 212);\n"
"    border: 1px solid  rgb(165, 165, 165);\n"
"    border-bottom: 1px solid  rgb(165, 165, 165);\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover,{\n"
"    color: black;\n"
"	background-color: rgb(217, 220, 234);\n"
"    border: 1px solid  rgb(217, 220, 234);\n"
"    border-bottom: 1px solid  rgb(217, 220, 234);\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed,QPushBut"
                        "ton:pressed {\n"
"\n"
"                            color: black;\n"
"\n"
"	background-color: rgb(219, 222, 236);\n"
"    border: 1px solid  rgb(217, 220, 234);\n"
"    border-bottom: 1px solid  rgb(217, 220, 234);\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled,QPushButton:disabled{\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
""
                        "}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"\n"
"                            border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=false] {\n"
"    padding: 6px 12px 6px 12px;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=true] {\n"
"    padding: 6px 12px 6px 36px;\n"
"}\n"
"\n"
"HyperlinkButton:hover {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
""
                        "HyperlinkButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.43);\n"
"    back\n"
"                        ground-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"RadioButton {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    background-color: transparent;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"    color: black;\n"
"}\n"
"\n"
"RadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #999999;\n"
"    background-color: rgba(0, 0, 0, 5);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"RadioButton::indicator:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"RadioButton::indicator:pressed {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(225, 224, 223),\n"
"            stop:1 rgb(225, 224, 2"
                        "23));\n"
"}\n"
"\n"
"RadioButton::indicator:checked {\n"
"    height: 22px;\n"
"    width: 22px;\n"
"   \n"
"                         border: none;\n"
"    border-radius: 11px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"        "
                        "    stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"RadioButton::indicator:d\n"
"                        isabled {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RadioButton::indicator:disabled:checked {\n"
"    border: none;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
"            stop:1 rgba(0, 0, 0, 0.2169));\n"
"}\n"
"\n"
"TransparentToolButton,\n"
"TransparentToggleToolButton,\n"
"TransparentDropDownToolButton,\n"
"TransparentPushButton,\n"
"TransparentDropDownPushButton,\n"
"TransparentTogglePushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"TransparentToolButton:hover,\n"
"TransparentToggleToolButton:hover,\n"
"TransparentDropDownToo"
                        "lButton:hover,\n"
"TransparentPushButton:hover,\n"
"TransparentDropDownPushButton:hover,\n"
"TransparentTogglePushButton:hover {\n"
"    background-color: rgba(0,\n"
"                         0, 0, 9);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:pressed,\n"
"TransparentToggleToolButton:pressed,\n"
"TransparentDropDownToolButton:pressed,\n"
"TransparentPushButton:pressed,\n"
"TransparentDropDownPushButton:pressed,\n"
"TransparentTogglePushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:disabled,\n"
"TransparentToggleToolButton:disabled,\n"
"TransparentDropDownToolButton:disabled,\n"
"TransprentPushButton:disabled,\n"
"TransparentDropDownPushButton:disabled,\n"
"TransprentTogglePushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"PillPushButton,\n"
"PillPushButton:hover,\n"
"PillPushButton:pressed,\n"
"PillPushButton:disabled,\n"
"PillPushButton:checked,\n"
"PillPushButton:chec"
                        "ked:hover,\n"
"PillPushButton:checked:pressed,\n"
"PillPushButton:disabled:checked,\n"
"PillToolButton,\n"
"PillToolButton:hover,\n"
"PillToolButton:pressed,\n"
"PillToolButton:disabled,\n"
"\n"
"                        PillToolButton:checked,\n"
"PillToolButton:checked:hover,\n"
"PillToolButton:checked:pressed,\n"
"PillToolButton:disabled:checked {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/excel-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.convert_item.setIcon(icon2)
        self.convert_item.setIconSize(QSize(20, 20))
        self.convert_item.setCheckable(True)
        self.convert_item.setChecked(False)

        self.verticalLayout.addWidget(self.convert_item)

        self.verticalSpacer = QSpacerItem(20, 631, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.navigation_bar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.copy_page = QWidget()
        self.copy_page.setObjectName(u"copy_page")
        self.gridLayout_2 = QGridLayout(self.copy_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.StrongBodyLabel = StrongBodyLabel(self.copy_page)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.gridLayout_2.addWidget(self.StrongBodyLabel, 0, 0, 1, 1)

        self.copy_from_path_le = LineEdit(self.copy_page)
        self.copy_from_path_le.setObjectName(u"copy_from_path_le")

        self.gridLayout_2.addWidget(self.copy_from_path_le, 0, 1, 1, 1)

        self.copy_from_path_btn = ToolButton(self.copy_page)
        self.copy_from_path_btn.setObjectName(u"copy_from_path_btn")
        self.copy_from_path_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/dots-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copy_from_path_btn.setIcon(icon3)
        self.copy_from_path_btn.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.copy_from_path_btn, 0, 2, 1, 1)

        self.StrongBodyLabel_2 = StrongBodyLabel(self.copy_page)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.gridLayout_2.addWidget(self.StrongBodyLabel_2, 1, 0, 1, 1)

        self.copy_to_path_le = LineEdit(self.copy_page)
        self.copy_to_path_le.setObjectName(u"copy_to_path_le")

        self.gridLayout_2.addWidget(self.copy_to_path_le, 1, 1, 1, 1)

        self.copy_to_path_btn = ToolButton(self.copy_page)
        self.copy_to_path_btn.setObjectName(u"copy_to_path_btn")
        self.copy_to_path_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_to_path_btn.setIcon(icon3)
        self.copy_to_path_btn.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.copy_to_path_btn, 1, 2, 1, 1)

        self.SimpleCardWidget = SimpleCardWidget(self.copy_page)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.gridLayout = QGridLayout(self.SimpleCardWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.copy_prefix_cb = CheckBox(self.SimpleCardWidget)
        self.copy_prefix_cb.setObjectName(u"copy_prefix_cb")
        self.copy_prefix_cb.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.copy_prefix_cb, 0, 0, 1, 1)

        self.copy_prefix_le = LineEdit(self.SimpleCardWidget)
        self.copy_prefix_le.setObjectName(u"copy_prefix_le")
        self.copy_prefix_le.setEnabled(False)

        self.gridLayout.addWidget(self.copy_prefix_le, 0, 1, 1, 1)

        self.copy_prefix_datenow_cb = CheckBox(self.SimpleCardWidget)
        self.copy_prefix_datenow_cb.setObjectName(u"copy_prefix_datenow_cb")
        self.copy_prefix_datenow_cb.setEnabled(False)
        self.copy_prefix_datenow_cb.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.copy_prefix_datenow_cb, 0, 2, 1, 1)

        self.copy_postfix_cb = CheckBox(self.SimpleCardWidget)
        self.copy_postfix_cb.setObjectName(u"copy_postfix_cb")
        self.copy_postfix_cb.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.copy_postfix_cb, 1, 0, 1, 1)

        self.copy_postfix_le = LineEdit(self.SimpleCardWidget)
        self.copy_postfix_le.setObjectName(u"copy_postfix_le")
        self.copy_postfix_le.setEnabled(False)

        self.gridLayout.addWidget(self.copy_postfix_le, 1, 1, 1, 1)

        self.copy_postfix_datenow_cb = CheckBox(self.SimpleCardWidget)
        self.copy_postfix_datenow_cb.setObjectName(u"copy_postfix_datenow_cb")
        self.copy_postfix_datenow_cb.setEnabled(False)
        self.copy_postfix_datenow_cb.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.copy_postfix_datenow_cb, 1, 2, 1, 1)

        self.copy_cutmode_cb = CheckBox(self.SimpleCardWidget)
        self.copy_cutmode_cb.setObjectName(u"copy_cutmode_cb")
        self.copy_cutmode_cb.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.copy_cutmode_cb, 2, 0, 1, 2)


        self.gridLayout_2.addWidget(self.SimpleCardWidget, 2, 0, 1, 3)

        self.copy_output_te = TextEdit(self.copy_page)
        self.copy_output_te.setObjectName(u"copy_output_te")
        self.copy_output_te.setReadOnly(True)

        self.gridLayout_2.addWidget(self.copy_output_te, 3, 0, 1, 3)

        self.copy_progress_bar = ProgressBar(self.copy_page)
        self.copy_progress_bar.setObjectName(u"copy_progress_bar")
        self.copy_progress_bar.setStyleSheet(u"")
        self.copy_progress_bar.setValue(50)

        self.gridLayout_2.addWidget(self.copy_progress_bar, 4, 0, 1, 3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.copy_run_btn = PrimaryPushButton(self.copy_page)
        self.copy_run_btn.setObjectName(u"copy_run_btn")
        self.copy_run_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.copy_run_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 0, 1, 3)

        self.stackedWidget.addWidget(self.copy_page)
        self.preview_page = QWidget()
        self.preview_page.setObjectName(u"preview_page")
        self.verticalLayout_2 = QVBoxLayout(self.preview_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SimpleCardWidget_3 = SimpleCardWidget(self.preview_page)
        self.SimpleCardWidget_3.setObjectName(u"SimpleCardWidget_3")
        self.gridLayout_3 = QGridLayout(self.SimpleCardWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.BodyLabel = BodyLabel(self.SimpleCardWidget_3)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.gridLayout_3.addWidget(self.BodyLabel, 0, 0, 1, 1)

        self.preview_review_btn = ToolButton(self.SimpleCardWidget_3)
        self.preview_review_btn.setObjectName(u"preview_review_btn")
        self.preview_review_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.preview_review_btn.setIcon(icon3)
        self.preview_review_btn.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.preview_review_btn, 0, 1, 1, 3)

        self.preview_current_file_label = BodyLabel(self.SimpleCardWidget_3)
        self.preview_current_file_label.setObjectName(u"preview_current_file_label")

        self.gridLayout_3.addWidget(self.preview_current_file_label, 0, 4, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(817, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 6, 1, 1)

        self.StrongBodyLabel_10 = StrongBodyLabel(self.SimpleCardWidget_3)
        self.StrongBodyLabel_10.setObjectName(u"StrongBodyLabel_10")

        self.gridLayout_3.addWidget(self.StrongBodyLabel_10, 1, 0, 1, 2)

        self.current_column_label = BodyLabel(self.SimpleCardWidget_3)
        self.current_column_label.setObjectName(u"current_column_label")

        self.gridLayout_3.addWidget(self.current_column_label, 1, 2, 1, 3)

        self.reset_link = HyperlinkLabel(self.SimpleCardWidget_3)
        self.reset_link.setObjectName(u"reset_link")

        self.gridLayout_3.addWidget(self.reset_link, 1, 5, 1, 2)

        self.set_params_link = PushButton(self.SimpleCardWidget_3)
        self.set_params_link.setObjectName(u"set_params_link")

        self.gridLayout_3.addWidget(self.set_params_link, 2, 0, 2, 3)

        self.map_btn = PushButton(self.SimpleCardWidget_3)
        self.map_btn.setObjectName(u"map_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.map_btn.sizePolicy().hasHeightForWidth())
        self.map_btn.setSizePolicy(sizePolicy1)
        self.map_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.map_btn, 2, 3, 2, 2)

        self.StrongBodyLabel_4 = StrongBodyLabel(self.SimpleCardWidget_3)
        self.StrongBodyLabel_4.setObjectName(u"StrongBodyLabel_4")

        self.gridLayout_3.addWidget(self.StrongBodyLabel_4, 2, 5, 1, 1)

        self.min_link = HyperlinkLabel(self.SimpleCardWidget_3)
        self.min_link.setObjectName(u"min_link")
        self.min_link.setStyleSheet(u"HyperlinkLabel {\n"
"	color: rgb(131, 131, 131);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"   \n"
"	color: rgb(56, 56, 56);\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"  \n"
"	color: rgb(165, 165, 165);\n"
"}")

        self.gridLayout_3.addWidget(self.min_link, 2, 6, 1, 1)

        self.StrongBodyLabel_5 = StrongBodyLabel(self.SimpleCardWidget_3)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")

        self.gridLayout_3.addWidget(self.StrongBodyLabel_5, 3, 5, 1, 1)

        self.max_link = HyperlinkLabel(self.SimpleCardWidget_3)
        self.max_link.setObjectName(u"max_link")
        self.max_link.setStyleSheet(u"HyperlinkLabel {\n"
"	color: rgb(131, 131, 131);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"   \n"
"	color: rgb(56, 56, 56);\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"  \n"
"	color: rgb(165, 165, 165);\n"
"}")

        self.gridLayout_3.addWidget(self.max_link, 3, 6, 1, 1)

        self.SwitchButton = SwitchButton(self.SimpleCardWidget_3)
        self.SwitchButton.setObjectName(u"SwitchButton")

        self.gridLayout_3.addWidget(self.SwitchButton, 4, 0, 1, 6)


        self.verticalLayout_2.addWidget(self.SimpleCardWidget_3)

        self.preview_table = TableWidget(self.preview_page)
        self.preview_table.setObjectName(u"preview_table")
        self.preview_table.setStyleSheet(u"QTableView {\n"
"    background: transparent;\n"
"    outline: none;\n"
"    border: none;\n"
"    /* font: 13px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    selection-background-color: transparent;\n"
"    alternate-background-color: transparent;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    background: transparent;\n"
"    border: 0px;\n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    height: 35px;\n"
"}\n"
"QTableWidget::item:selected{ \n"
"	border-radius:5px;\n"
"	background-color: rgb(93, 93, 93);\n"
"	color: rgb(255, 255, 255);\n"
" }\n"
"\n"
"\n"
"QTableView::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 0.48);\n"
"    background-color: rgba(0, 0, 0, 0.022);\n"
"}\n"
"\n"
"QTableView::indicator:hover {\n"
"    border: 1px solid rgba(0, 0, 0, 0.56);\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"}\n"
"\n"
"QTableView::indicator:pressed {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: rgba(0,"
                        " 0, 0, 0.12);\n"
"}\n"
"\n"
"QTableView::indicator:checked,\n"
"QTableView::indicator:indeterminate {\n"
"    border: 1px solid #009faa;\n"
"    background-color: #009faa;\n"
"}\n"
"\n"
"QTableView::indicator:checked {\n"
"    image: url(:/qfluentwidgets/images/check_box/Accept_white.svg);\n"
"}\n"
"\n"
"QTableView::indicator:indeterminate {\n"
"    image: url(:/qfluentwidgets/images/check_box/PartialAccept_white.svg);\n"
"}\n"
"\n"
"QTableView::indicator:checked:hover,\n"
"QTableView::indicator:indeterminate:hover {\n"
"    border: 1px solid #00a7b3;\n"
"    background-color: #00a7b3;\n"
"}\n"
"\n"
"QTableView::indicator:checked:pressed,\n"
"QTableView::indicator:indeterminate:pressed {\n"
"    border: 1px solid #3eabb3;\n"
"    background-color: #3eabb3;\n"
"}\n"
"\n"
"QTableView::indicator:disabled {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableView::indicator:checked:disabled,\n"
"QTableView::indicator:indeterminate:disabled {\n"
"    border: 1p"
                        "x solid rgb(199, 199, 199);\n"
"    background-color: rgb(199, 199, 199);\n"
"}\n"
"\n"
"\n"
"QHeaderView {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: transparent;\n"
"    color: black;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 19);\n"
"    font: 13px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 7);\n"
"    border-left: none;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:last {\n"
"    border-right: none;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    border-top: none;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;\n"
"    image: url(:/qfluentwidgets/images/table_view/Down_black.svg);\n"
"}\n"
""
                        "\n"
"QHeaderView::up-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;\n"
"    image: url(:/qfluentwidgets/images/table_view/Up_black.svg);\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgba(0, 0, 0, 19);\n"
"}\n"
"\n"
"QTableCornerButton::section:pressed {\n"
"    background-color: rgba(0, 0, 0, 12);\n"
"}")
        self.preview_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.preview_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.preview_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.preview_table.setTextElideMode(Qt.ElideNone)
        self.preview_table.setShowGrid(True)
        self.preview_table.setGridStyle(Qt.DashLine)
        self.preview_table.setSortingEnabled(False)
        self.preview_table.setWordWrap(False)
        self.preview_table.setCornerButtonEnabled(False)
        self.preview_table.setRowCount(0)
        self.preview_table.setColumnCount(0)
        self.preview_table.horizontalHeader().setStretchLastSection(True)
        self.preview_table.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.preview_table)

        self.stackedWidget.addWidget(self.preview_page)
        self.convert_page = QWidget()
        self.convert_page.setObjectName(u"convert_page")
        self.gridLayout_5 = QGridLayout(self.convert_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.convert_findpath_le = LineEdit(self.convert_page)
        self.convert_findpath_le.setObjectName(u"convert_findpath_le")

        self.gridLayout_5.addWidget(self.convert_findpath_le, 0, 0, 1, 5)

        self.convert_review_btn = ToolButton(self.convert_page)
        self.convert_review_btn.setObjectName(u"convert_review_btn")
        self.convert_review_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.convert_review_btn.setIcon(icon3)
        self.convert_review_btn.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.convert_review_btn, 0, 5, 1, 1)

        self.convert_find_btn = ToolButton(self.convert_page)
        self.convert_find_btn.setObjectName(u"convert_find_btn")
        self.convert_find_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/lupa-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.convert_find_btn.setIcon(icon4)
        self.convert_find_btn.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.convert_find_btn, 0, 6, 1, 1)

        self.convert_listwidget = ListWidget(self.convert_page)
        self.convert_listwidget.setObjectName(u"convert_listwidget")
        self.convert_listwidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.convert_listwidget.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_5.addWidget(self.convert_listwidget, 1, 0, 1, 7)

        self.StrongBodyLabel_9 = StrongBodyLabel(self.convert_page)
        self.StrongBodyLabel_9.setObjectName(u"StrongBodyLabel_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.StrongBodyLabel_9.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_9.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.StrongBodyLabel_9, 2, 0, 1, 1)

        self.convert_count_selected_row_label = BodyLabel(self.convert_page)
        self.convert_count_selected_row_label.setObjectName(u"convert_count_selected_row_label")
        sizePolicy2.setHeightForWidth(self.convert_count_selected_row_label.sizePolicy().hasHeightForWidth())
        self.convert_count_selected_row_label.setSizePolicy(sizePolicy2)
        self.convert_count_selected_row_label.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_5.addWidget(self.convert_count_selected_row_label, 2, 1, 1, 1)

        self.many_to_one_tbtn = ToggleButton(self.convert_page)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.many_to_one_tbtn)
        self.many_to_one_tbtn.setObjectName(u"many_to_one_tbtn")
        sizePolicy1.setHeightForWidth(self.many_to_one_tbtn.sizePolicy().hasHeightForWidth())
        self.many_to_one_tbtn.setSizePolicy(sizePolicy1)
        self.many_to_one_tbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.many_to_one_tbtn, 2, 2, 1, 1)

        self.many_to_many_tbtn = ToggleButton(self.convert_page)
        self.buttonGroup_2.addButton(self.many_to_many_tbtn)
        self.many_to_many_tbtn.setObjectName(u"many_to_many_tbtn")
        sizePolicy1.setHeightForWidth(self.many_to_many_tbtn.sizePolicy().hasHeightForWidth())
        self.many_to_many_tbtn.setSizePolicy(sizePolicy1)
        self.many_to_many_tbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.many_to_many_tbtn.setChecked(True)

        self.gridLayout_5.addWidget(self.many_to_many_tbtn, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(781, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 4, 1, 3)

        self.SimpleCardWidget_2 = SimpleCardWidget(self.convert_page)
        self.SimpleCardWidget_2.setObjectName(u"SimpleCardWidget_2")
        self.gridLayout_4 = QGridLayout(self.SimpleCardWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.SubtitleLabel = SubtitleLabel(self.SimpleCardWidget_2)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.gridLayout_4.addWidget(self.SubtitleLabel, 0, 0, 1, 1)

        self.BodyLabel_2 = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.gridLayout_4.addWidget(self.BodyLabel_2, 1, 0, 1, 1)

        self.convert_pathsave_le = LineEdit(self.SimpleCardWidget_2)
        self.convert_pathsave_le.setObjectName(u"convert_pathsave_le")

        self.gridLayout_4.addWidget(self.convert_pathsave_le, 1, 1, 1, 1)

        self.convert_pathsave_review_btn = ToolButton(self.SimpleCardWidget_2)
        self.convert_pathsave_review_btn.setObjectName(u"convert_pathsave_review_btn")
        self.convert_pathsave_review_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.convert_pathsave_review_btn.setIcon(icon3)
        self.convert_pathsave_review_btn.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.convert_pathsave_review_btn, 1, 2, 1, 1)

        self.BodyLabel_3 = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.gridLayout_4.addWidget(self.BodyLabel_3, 2, 0, 1, 1)

        self.convert_name_savefile_le = LineEdit(self.SimpleCardWidget_2)
        self.convert_name_savefile_le.setObjectName(u"convert_name_savefile_le")

        self.gridLayout_4.addWidget(self.convert_name_savefile_le, 2, 1, 1, 1)

        self.BodyLabel_4 = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.gridLayout_4.addWidget(self.BodyLabel_4, 2, 2, 1, 1)

        self.convert_run_btn = PrimaryPushButton(self.SimpleCardWidget_2)
        self.convert_run_btn.setObjectName(u"convert_run_btn")
        self.convert_run_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.convert_run_btn, 2, 3, 1, 1)


        self.gridLayout_5.addWidget(self.SimpleCardWidget_2, 3, 0, 1, 7)

        self.stackedWidget.addWidget(self.convert_page)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pupo", None))
        self.about_project_reference.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0435\u043a\u0442\u0435", None))
#if QT_CONFIG(tooltip)
        self.collect_results_item.setToolTip(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0438\u0440\u0443\u044e\u0449\u0438\u0445 \u0444\u0430\u0439\u043b\u043e\u0432 \u043f\u043e\u0441\u043b\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.collect_results_item.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u043e\u0440 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
#if QT_CONFIG(tooltip)
        self.preview_item.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.preview_item.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0444\u0430\u0439\u043b\u043e\u0432", None))
#if QT_CONFIG(tooltip)
        self.convert_item.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.convert_item.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434 txt to excel", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0443\u0434\u0430:", None))
        self.copy_from_path_le.setInputMask("")
        self.copy_from_path_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0434\u0430", None))
        self.copy_to_path_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435", None))
        self.copy_prefix_cb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0444\u0438\u043a\u0441", None))
        self.copy_prefix_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0440 \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e \u0438\u043c\u0435\u043d\u0438: \u043f\u0440\u0435\u0444\u0438\u043a\u0441_{\u0438\u043c\u044f \u0444\u0430\u0439\u043b\u0430}", None))
        self.copy_prefix_datenow_cb.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0434\u0430\u0442\u0430", None))
        self.copy_postfix_cb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0444\u0438\u043a\u0441", None))
        self.copy_postfix_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0440 \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e \u0438\u043c\u0435\u043d\u0438: \u043f\u043e\u0441\u0442\u0444\u0438\u043a\u0441_{\u0438\u043c\u044f \u0444\u0430\u0439\u043b\u0430}", None))
        self.copy_postfix_datenow_cb.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0434\u0430\u0442\u0430", None))
#if QT_CONFIG(tooltip)
        self.copy_cutmode_cb.setToolTip(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u0430\u043f\u043a\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.copy_cutmode_cb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0435\u0437\u0430\u0442\u044c", None))
        self.copy_output_te.setDocumentTitle("")
        self.copy_output_te.setPlaceholderText("")
        self.copy_run_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.BodyLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b:", None))
        self.preview_current_file_label.setText(QCoreApplication.translate("MainWindow", u"Body label", None))
        self.StrongBodyLabel_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446:", None))
        self.current_column_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.reset_link.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043f\u0430\u043b\u0438\u0442\u0440\u0443", None))
        self.set_params_link.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.map_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u0430", None))
        self.StrongBodyLabel_4.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
#if QT_CONFIG(tooltip)
        self.min_link.setToolTip(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.min_link.setText(QCoreApplication.translate("MainWindow", u"Hyperlink label", None))
#if QT_CONFIG(tooltip)
        self.StrongBodyLabel_5.setToolTip(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.max_link.setText(QCoreApplication.translate("MainWindow", u"Hyperlink label", None))
        self.SwitchButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043a\u0432\u0430\u0434\u0440\u0443\u043f\u043e\u043b\u0435\u0439", None))
        self.SwitchButton.setOnText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043a\u0432\u0430\u0434\u0440\u0443\u043f\u043e\u043b\u0435\u0439", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043a\u0432\u0430\u0434\u0440\u0443\u043f\u043e\u043b\u0435\u0439", None))
        self.convert_findpath_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u043e\u0445\u043e\u0434\u0438\u0442\u044c \u043f\u043e\u0438\u0441\u043a \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043e:", None))
        self.convert_count_selected_row_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.many_to_one_tbtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0431\u044b\u043b\u0438 \u0432\u044b\u0431\u0440\u0430\u043d\u044b, \u0437\u0430\u043f\u0438\u0448\u0443\u0442\u0441\u044f \u0432 \u043e\u0434\u0438\u043d \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u044d\u043a\u0441\u0435\u043b\u044c \u0432 \u043e\u0434\u0438\u043d \u043b\u0438\u0441\u0442", None))
#endif // QT_CONFIG(tooltip)
        self.many_to_one_tbtn.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043e\u0434\u0438\u043d \u043b\u0438\u0441\u0442", None))
#if QT_CONFIG(tooltip)
        self.many_to_many_tbtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430 \u0432 \u0441\u043a\u043b\u0435\u0439\u043a\u0435, \u0431\u0443\u0434\u0435\u0442 \u0441\u043e\u0437\u0434\u0430\u043d \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0439 \u043b\u0438\u0441\u0442 \u0432 \u044d\u043a\u0441\u0435\u043b\u044c \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.many_to_many_tbtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0439 \u043b\u0438\u0441\u0442", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435:", None))
        self.convert_pathsave_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435, \u043a\u0443\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0441\u043a\u043b\u0435\u0439\u043a\u0438", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430:", None))
        self.convert_name_savefile_le.setInputMask("")
        self.convert_name_savefile_le.setText(QCoreApplication.translate("MainWindow", u"result", None))
        self.convert_name_savefile_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0440\u0443\u044e\u0449\u0435\u0433\u043e \u0444\u0430\u0439\u043b\u0430", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("MainWindow", u".xlsx", None))
        self.convert_run_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi
