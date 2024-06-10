# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QSizePolicy, QWidget)

class Ui_GraphUi(object):
    def setupUi(self, GraphUi):
        if not GraphUi.objectName():
            GraphUi.setObjectName(u"GraphUi")
        GraphUi.resize(484, 330)
        self.gridLayout = QGridLayout(GraphUi)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(GraphUi)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(GraphUi)

        QMetaObject.connectSlotsByName(GraphUi)
    # setupUi

    def retranslateUi(self, GraphUi):
        GraphUi.setWindowTitle(QCoreApplication.translate("GraphUi", u"Dialog", None))
    # retranslateUi

