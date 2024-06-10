# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QSizePolicy,
    QSpacerItem, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, DoubleSpinBox,
    PrimaryPushButton, PushButton, SimpleCardWidget, SpinBox,
    StrongBodyLabel, SwitchButton)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(745, 307)
        Dialog.setMaximumSize(QSize(1000, 1000))
        Dialog.setStyleSheet(u"QDialog{\n"
"	\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.SimpleCardWidget = SimpleCardWidget(Dialog)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.gridLayout = QGridLayout(self.SimpleCardWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.BodyLabel_6 = BodyLabel(self.SimpleCardWidget)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.gridLayout.addWidget(self.BodyLabel_6, 0, 0, 1, 1)

        self.preview_corr_cb = ComboBox(self.SimpleCardWidget)
        self.preview_corr_cb.setObjectName(u"preview_corr_cb")
        self.preview_corr_cb.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.preview_corr_cb, 0, 1, 1, 1)

        self.BodyLabel_7 = BodyLabel(self.SimpleCardWidget)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")

        self.gridLayout.addWidget(self.BodyLabel_7, 1, 0, 1, 1)

        self.preview_maxlimit_spin = DoubleSpinBox(self.SimpleCardWidget)
        self.preview_maxlimit_spin.setObjectName(u"preview_maxlimit_spin")
        self.preview_maxlimit_spin.setMaximum(9999999.000000000000000)
        self.preview_maxlimit_spin.setSingleStep(0.010000000000000)

        self.gridLayout.addWidget(self.preview_maxlimit_spin, 1, 1, 1, 1)

        self.BodyLabel_8 = BodyLabel(self.SimpleCardWidget)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")

        self.gridLayout.addWidget(self.BodyLabel_8, 2, 0, 1, 1)

        self.preview_minlimit_spin = DoubleSpinBox(self.SimpleCardWidget)
        self.preview_minlimit_spin.setObjectName(u"preview_minlimit_spin")
        self.preview_minlimit_spin.setMaximum(9999999.000000000000000)
        self.preview_minlimit_spin.setSingleStep(0.010000000000000)

        self.gridLayout.addWidget(self.preview_minlimit_spin, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.SimpleCardWidget, 0, 0, 1, 2)

        self.SimpleCardWidget_2 = SimpleCardWidget(Dialog)
        self.SimpleCardWidget_2.setObjectName(u"SimpleCardWidget_2")
        self.gridLayout_2 = QGridLayout(self.SimpleCardWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BodyLabel = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.gridLayout_2.addWidget(self.BodyLabel, 0, 0, 1, 1)

        self.preview_corr_cb_2 = ComboBox(self.SimpleCardWidget_2)
        self.preview_corr_cb_2.setObjectName(u"preview_corr_cb_2")
        self.preview_corr_cb_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.preview_corr_cb_2, 0, 1, 1, 1)

        self.BodyLabel_2 = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.gridLayout_2.addWidget(self.BodyLabel_2, 1, 0, 1, 1)

        self.main_azimut = SpinBox(self.SimpleCardWidget_2)
        self.main_azimut.setObjectName(u"main_azimut")
        self.main_azimut.setMaximum(360)

        self.gridLayout_2.addWidget(self.main_azimut, 1, 1, 1, 1)

        self.BodyLabel_3 = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.gridLayout_2.addWidget(self.BodyLabel_3, 2, 0, 1, 1)

        self.min_azimut = SpinBox(self.SimpleCardWidget_2)
        self.min_azimut.setObjectName(u"min_azimut")
        self.min_azimut.setMaximum(360)

        self.gridLayout_2.addWidget(self.min_azimut, 2, 1, 1, 1)

        self.BodyLabel_4 = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.gridLayout_2.addWidget(self.BodyLabel_4, 3, 0, 1, 1)

        self.max_azimut = SpinBox(self.SimpleCardWidget_2)
        self.max_azimut.setObjectName(u"max_azimut")
        self.max_azimut.setMaximum(360)

        self.gridLayout_2.addWidget(self.max_azimut, 3, 1, 1, 1)

        self.BodyLabel_5 = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.gridLayout_2.addWidget(self.BodyLabel_5, 4, 0, 1, 1)

        self.distance_limit = SpinBox(self.SimpleCardWidget_2)
        self.distance_limit.setObjectName(u"distance_limit")
        self.distance_limit.setMaximum(10000)

        self.gridLayout_2.addWidget(self.distance_limit, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.SimpleCardWidget_2, 0, 2, 2, 3)

        self.StrongBodyLabel_7 = StrongBodyLabel(Dialog)
        self.StrongBodyLabel_7.setObjectName(u"StrongBodyLabel_7")

        self.gridLayout_3.addWidget(self.StrongBodyLabel_7, 1, 0, 1, 1)

        self.preview_count_row_show_cb = ComboBox(Dialog)
        self.preview_count_row_show_cb.setObjectName(u"preview_count_row_show_cb")
        self.preview_count_row_show_cb.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.preview_count_row_show_cb, 1, 1, 1, 1)

        self.SwitchButton = SwitchButton(Dialog)
        self.SwitchButton.setObjectName(u"SwitchButton")

        self.gridLayout_3.addWidget(self.SwitchButton, 2, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 0, 1, 3)

        self.cancel_btn = PushButton(Dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout_3.addWidget(self.cancel_btn, 3, 3, 1, 1)

        self.save_btn = PrimaryPushButton(Dialog)
        self.save_btn.setObjectName(u"save_btn")

        self.gridLayout_3.addWidget(self.save_btn, 3, 4, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Dialog", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440:", None))
#if QT_CONFIG(tooltip)
        self.preview_corr_cb.setToolTip(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u043e\u043b\u0431\u0435\u0446 \u0434\u043b\u044f \u043a\u043e\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u0440\u0430\u0441\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.preview_corr_cb.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u043e\u043b\u0431\u0435\u0446", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430:", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Dialog", u"\u041d\u0438\u0436\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430:", None))
        self.BodyLabel.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u043e\u043b\u0431\u0435\u0446 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f:", None))
#if QT_CONFIG(tooltip)
        self.preview_corr_cb_2.setToolTip(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u043e\u043b\u0431\u0435\u0446 \u0434\u043b\u044f \u043a\u043e\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u0440\u0430\u0441\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.preview_corr_cb_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u043e\u043b\u0431\u0435\u0446", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u0438\u0433\u043d\u0430\u043b\u0430 (\u0433\u0440\u0430\u0434\u0443\u0441\u044b):", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Dialog", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0430\u0437\u0438\u043c\u0443\u0442 (\u0433\u0440\u0430\u0434\u0443\u0441\u044b):", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0430\u0437\u0438\u043c\u0443\u0442 (\u0433\u0440\u0430\u0434\u0443\u0441\u044b):", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Dialog", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0434\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438 (\u043c):", None))
        self.distance_limit.setSuffix("")
        self.distance_limit.setPrefix("")
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043f\u043e:", None))
#if QT_CONFIG(tooltip)
        self.preview_count_row_show_cb.setToolTip(QCoreApplication.translate("Dialog", u"\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e 10", None))
#endif // QT_CONFIG(tooltip)
        self.preview_count_row_show_cb.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u043e\u043a", None))
        self.SwitchButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u043c\u0443 \u0441\u0442\u043e\u043b\u0431\u0446\u0443", None))
        self.SwitchButton.setOnText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u043c\u0443 \u0441\u0442\u043e\u043b\u0431\u0446\u0443", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u043c\u0443 \u0441\u0442\u043e\u043b\u0431\u0446\u0443", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi
