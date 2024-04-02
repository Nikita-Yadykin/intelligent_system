# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1082, 852)
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 281, 571))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.groupBox.setFont(font)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 271, 537))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 2, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 0, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 1, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.layoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 2, 1, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.layoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 3, 1, 1, 1)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.gridLayout)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_2.addWidget(self.label_10)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_10 = QCheckBox(self.layoutWidget)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_3.addWidget(self.checkBox_10, 2, 1, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.checkBox_9 = QCheckBox(self.layoutWidget)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_3.addWidget(self.checkBox_9, 1, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.layoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_3.addWidget(self.checkBox_8, 0, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_3.addWidget(self.label_14)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_4.addWidget(self.label_15, 0, 0, 2, 1)

        self.checkBox_11 = QCheckBox(self.layoutWidget)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_4.addWidget(self.checkBox_11, 0, 1, 1, 1)

        self.checkBox_12 = QCheckBox(self.layoutWidget)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout_4.addWidget(self.checkBox_12, 1, 1, 2, 1)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.gridLayout_4.addWidget(self.label_17, 3, 0, 1, 1)

        self.checkBox_13 = QCheckBox(self.layoutWidget)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout_4.addWidget(self.checkBox_13, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.verticalLayout_6.addWidget(self.label_18)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_5.addWidget(self.label_19, 0, 0, 1, 1)

        self.checkBox_14 = QCheckBox(self.layoutWidget)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout_5.addWidget(self.checkBox_14, 0, 1, 1, 1)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout_5.addWidget(self.label_20, 1, 0, 1, 1)

        self.checkBox_15 = QCheckBox(self.layoutWidget)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout_5.addWidget(self.checkBox_15, 1, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_21 = QLabel(self.layoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.gridLayout_6.addWidget(self.label_22, 0, 0, 1, 1)

        self.checkBox_16 = QCheckBox(self.layoutWidget)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout_6.addWidget(self.checkBox_16, 0, 1, 1, 1)

        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout_6.addWidget(self.label_23, 1, 0, 1, 1)

        self.checkBox_17 = QCheckBox(self.layoutWidget)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.gridLayout_6.addWidget(self.checkBox_17, 1, 1, 1, 1)


        self.formLayout_2.setLayout(1, QFormLayout.LabelRole, self.gridLayout_6)


        self.verticalLayout_7.addLayout(self.formLayout_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(300, 10, 351, 261))
        font2 = QFont()
        font2.setBold(True)
        self.groupBox_2.setFont(font2)
        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 325, 222))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_24)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_25 = QLabel(self.layoutWidget1)
        self.label_25.setObjectName(u"label_25")
        font3 = QFont()
        font3.setBold(False)
        self.label_25.setFont(font3)

        self.gridLayout_7.addWidget(self.label_25, 0, 0, 1, 1)

        self.checkBox_18 = QCheckBox(self.layoutWidget1)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.gridLayout_7.addWidget(self.checkBox_18, 0, 1, 1, 1)

        self.label_26 = QLabel(self.layoutWidget1)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.gridLayout_7.addWidget(self.label_26, 1, 0, 1, 1)

        self.checkBox_19 = QCheckBox(self.layoutWidget1)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout_7.addWidget(self.checkBox_19, 1, 1, 1, 1)

        self.label_27 = QLabel(self.layoutWidget1)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.gridLayout_7.addWidget(self.label_27, 2, 0, 1, 1)

        self.checkBox_20 = QCheckBox(self.layoutWidget1)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout_7.addWidget(self.checkBox_20, 2, 1, 1, 1)

        self.label_28 = QLabel(self.layoutWidget1)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.gridLayout_7.addWidget(self.label_28, 3, 0, 1, 1)

        self.checkBox_21 = QCheckBox(self.layoutWidget1)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout_7.addWidget(self.checkBox_21, 3, 1, 1, 1)

        self.label_29 = QLabel(self.layoutWidget1)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.gridLayout_7.addWidget(self.label_29, 4, 0, 1, 1)

        self.checkBox_22 = QCheckBox(self.layoutWidget1)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.gridLayout_7.addWidget(self.checkBox_22, 4, 1, 1, 1)

        self.label_30 = QLabel(self.layoutWidget1)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.gridLayout_7.addWidget(self.label_30, 5, 0, 1, 1)

        self.checkBox_23 = QCheckBox(self.layoutWidget1)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout_7.addWidget(self.checkBox_23, 5, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_7)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_31 = QLabel(self.layoutWidget1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)

        self.gridLayout_8.addWidget(self.label_31, 0, 0, 1, 1)

        self.checkBox_24 = QCheckBox(self.layoutWidget1)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout_8.addWidget(self.checkBox_24, 0, 1, 1, 1)

        self.label_32 = QLabel(self.layoutWidget1)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)

        self.gridLayout_8.addWidget(self.label_32, 1, 0, 1, 1)

        self.checkBox_25 = QCheckBox(self.layoutWidget1)
        self.checkBox_25.setObjectName(u"checkBox_25")

        self.gridLayout_8.addWidget(self.checkBox_25, 1, 1, 1, 1)

        self.label_33 = QLabel(self.layoutWidget1)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)

        self.gridLayout_8.addWidget(self.label_33, 2, 0, 1, 1)

        self.checkBox_26 = QCheckBox(self.layoutWidget1)
        self.checkBox_26.setObjectName(u"checkBox_26")

        self.gridLayout_8.addWidget(self.checkBox_26, 2, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_8)

        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 320, 201, 91))
        self.pushButton.setFont(font2)
        self.label_70 = QLabel(Widget)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(310, 430, 721, 351))
        self.label_70.setMouseTracking(False)
        self.label_70.setWordWrap(True)
        self.label_70.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.layoutWidget2 = QWidget(Widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(670, 20, 188, 130))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.layoutWidget2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_34)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_35 = QLabel(self.layoutWidget2)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_9.addWidget(self.label_35, 0, 0, 1, 1)

        self.checkBox_27 = QCheckBox(self.layoutWidget2)
        self.checkBox_27.setObjectName(u"checkBox_27")

        self.gridLayout_9.addWidget(self.checkBox_27, 0, 1, 1, 1)

        self.label_36 = QLabel(self.layoutWidget2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_9.addWidget(self.label_36, 1, 0, 1, 1)

        self.checkBox_28 = QCheckBox(self.layoutWidget2)
        self.checkBox_28.setObjectName(u"checkBox_28")

        self.gridLayout_9.addWidget(self.checkBox_28, 1, 1, 1, 1)

        self.label_38 = QLabel(self.layoutWidget2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_9.addWidget(self.label_38, 2, 0, 1, 1)

        self.checkBox_29 = QCheckBox(self.layoutWidget2)
        self.checkBox_29.setObjectName(u"checkBox_29")

        self.gridLayout_9.addWidget(self.checkBox_29, 2, 1, 1, 1)

        self.label_39 = QLabel(self.layoutWidget2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_9.addWidget(self.label_39, 3, 0, 1, 1)

        self.checkBox_30 = QCheckBox(self.layoutWidget2)
        self.checkBox_30.setObjectName(u"checkBox_30")

        self.gridLayout_9.addWidget(self.checkBox_30, 3, 1, 1, 1)

        self.label_40 = QLabel(self.layoutWidget2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_9.addWidget(self.label_40, 4, 0, 1, 1)

        self.checkBox_31 = QCheckBox(self.layoutWidget2)
        self.checkBox_31.setObjectName(u"checkBox_31")

        self.gridLayout_9.addWidget(self.checkBox_31, 4, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_9)

        self.layoutWidget3 = QWidget(Widget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(870, 20, 173, 108))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.layoutWidget3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_54)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_55 = QLabel(self.layoutWidget3)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_10.addWidget(self.label_55, 0, 0, 1, 1)

        self.checkBox_32 = QCheckBox(self.layoutWidget3)
        self.checkBox_32.setObjectName(u"checkBox_32")

        self.gridLayout_10.addWidget(self.checkBox_32, 0, 1, 1, 1)

        self.label_56 = QLabel(self.layoutWidget3)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_10.addWidget(self.label_56, 1, 0, 1, 1)

        self.checkBox_33 = QCheckBox(self.layoutWidget3)
        self.checkBox_33.setObjectName(u"checkBox_33")

        self.gridLayout_10.addWidget(self.checkBox_33, 1, 1, 1, 1)

        self.label_57 = QLabel(self.layoutWidget3)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_10.addWidget(self.label_57, 2, 0, 1, 1)

        self.checkBox_34 = QCheckBox(self.layoutWidget3)
        self.checkBox_34.setObjectName(u"checkBox_34")

        self.gridLayout_10.addWidget(self.checkBox_34, 2, 1, 1, 1)

        self.label_58 = QLabel(self.layoutWidget3)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_10.addWidget(self.label_58, 3, 0, 1, 1)

        self.checkBox_35 = QCheckBox(self.layoutWidget3)
        self.checkBox_35.setObjectName(u"checkBox_35")

        self.gridLayout_10.addWidget(self.checkBox_35, 3, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_10)

        self.layoutWidget4 = QWidget(Widget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(670, 160, 206, 130))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.layoutWidget4)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_59)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_60 = QLabel(self.layoutWidget4)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_11.addWidget(self.label_60, 0, 0, 1, 1)

        self.checkBox_36 = QCheckBox(self.layoutWidget4)
        self.checkBox_36.setObjectName(u"checkBox_36")

        self.gridLayout_11.addWidget(self.checkBox_36, 0, 1, 1, 1)

        self.label_61 = QLabel(self.layoutWidget4)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_11.addWidget(self.label_61, 1, 0, 1, 1)

        self.checkBox_37 = QCheckBox(self.layoutWidget4)
        self.checkBox_37.setObjectName(u"checkBox_37")

        self.gridLayout_11.addWidget(self.checkBox_37, 1, 1, 1, 1)

        self.label_62 = QLabel(self.layoutWidget4)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_11.addWidget(self.label_62, 2, 0, 1, 1)

        self.checkBox_38 = QCheckBox(self.layoutWidget4)
        self.checkBox_38.setObjectName(u"checkBox_38")

        self.gridLayout_11.addWidget(self.checkBox_38, 2, 1, 1, 1)

        self.label_63 = QLabel(self.layoutWidget4)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_11.addWidget(self.label_63, 3, 0, 1, 1)

        self.checkBox_39 = QCheckBox(self.layoutWidget4)
        self.checkBox_39.setObjectName(u"checkBox_39")

        self.gridLayout_11.addWidget(self.checkBox_39, 3, 1, 1, 1)

        self.label_65 = QLabel(self.layoutWidget4)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_11.addWidget(self.label_65, 4, 0, 1, 1)

        self.checkBox_40 = QCheckBox(self.layoutWidget4)
        self.checkBox_40.setObjectName(u"checkBox_40")

        self.gridLayout_11.addWidget(self.checkBox_40, 4, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_11)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043c\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e\u0431 \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u044f\u0445", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0432\u0438\u0434\u044b \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u043d\u044b\u0445 \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u0435\u0439", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u0423\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u044c \u043a\u043e\u0434\u0430", None))
        self.checkBox.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u0423\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u044c \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u044b", None))
        self.checkBox_2.setText("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u041c\u043d\u043e\u0433\u043e\u0444\u0430\u043a\u0442\u043e\u0440\u043d\u0430\u044f \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.checkBox_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0443\u0440\u043e\u0432\u043d\u0438 \u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u0435\u0439", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u041d\u0438\u0437\u043a\u0438\u0439", None))
        self.checkBox_4.setText("")
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439", None))
        self.checkBox_5.setText("")
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0441\u043e\u043a\u0438\u0439", None))
        self.checkBox_6.setText("")
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u041a\u0440\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439", None))
        self.checkBox_7.setText("")
        self.label_10.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0441\u0442\u0430\u0442\u0443\u0441 \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u0435\u0439", None))
        self.checkBox_10.setText("")
        self.label_11.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u043c", None))
        self.checkBox_9.setText("")
        self.checkBox_8.setText("")
        self.label_12.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0430 \u0432 \u0445\u043e\u0434\u0435 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0439", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043d\u0430\u043b\u0438\u0447\u0438\u0435 \u044d\u043a\u0441\u043f\u043b\u043e\u0439\u0442\u0430", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0443\u0442\u043e\u043d\u044f\u044e\u0442\u0441\u044f", None))
        self.checkBox_11.setText("")
        self.checkBox_12.setText("")
        self.label_16.setText(QCoreApplication.translate("Widget", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 \u0432 \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u043c \u0434\u043e\u0441\u0442\u0443\u043f\u0435", None))
        self.checkBox_13.setText("")
        self.label_18.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e\u0431 \u0443\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u0438\u0438", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"\u0423\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u0430", None))
        self.checkBox_14.setText("")
        self.label_20.setText(QCoreApplication.translate("Widget", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u0443\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u0438\u0438 \u043e\u0441\u0442\u0443\u0442\u0441\u0432\u0443\u0435\u0442", None))
        self.checkBox_15.setText("")
        self.label_21.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0441\u0432\u044f\u0437\u044c \u0441 \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u0430\u043c\u0438 \u0418\u0411", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u0438\u0441\u0443\u0442\u0441\u0432\u0443\u0435\u0442", None))
        self.checkBox_16.setText("")
        self.label_23.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.checkBox_17.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e\u0431 \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u044f\u0445", None))
        self.label_24.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u0443\u0433\u0440\u043e\u0437\u044b", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u043d\u0430\u0440\u0443\u0448\u0438\u0442\u0435\u043b\u044c \u0441 \u043d\u0438\u0437\u043a\u0438\u043c \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043e\u043c", None))
        self.checkBox_18.setText("")
        self.label_26.setText(QCoreApplication.translate("Widget", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043d\u0430\u0440\u0443\u0448\u0438\u0442\u0435\u043b\u044c \u0441 \u043d\u0438\u0437\u043a\u0438\u043c \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043e\u043c", None))
        self.checkBox_19.setText("")
        self.label_27.setText(QCoreApplication.translate("Widget", u"\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u043d\u0430\u0440\u0443\u0448\u0438\u0442\u0435\u043b\u044c \u0441\u043e \u0441\u0440\u0435\u0434\u043d\u0438\u043c \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043e\u043c", None))
        self.checkBox_20.setText("")
        self.label_28.setText(QCoreApplication.translate("Widget", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043d\u0430\u0440\u0443\u0448\u0438\u0442\u0435\u043b\u044c \u0441\u043e \u0441\u0440\u0435\u0434\u043d\u0438\u043c \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043e\u043c", None))
        self.checkBox_21.setText("")
        self.label_29.setText(QCoreApplication.translate("Widget", u"\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u043d\u0430\u0440\u0443\u0448\u0438\u0442\u0435\u043b\u044c \u0441 \u0432\u044b\u0441\u043e\u043a\u0438\u043c \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043e\u043c", None))
        self.checkBox_22.setText("")
        self.label_30.setText(QCoreApplication.translate("Widget", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043d\u0430\u0440\u0443\u0448\u0438\u0442\u0435\u043b\u044c \u0441 \u0432\u044b\u0441\u043e\u043a\u0438\u043c \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043e\u043c", None))
        self.checkBox_23.setText("")
        self.label_31.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u043f\u0440\u0438 \u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0438 \u043a\u043e\u043d\u0444\u0438\u0434\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
        self.checkBox_24.setText("")
        self.label_32.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u043f\u0440\u0438 \u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0438 \u0446\u0435\u043b\u043e\u0441\u0442\u043d\u043e\u0441\u0442\u0438", None))
        self.checkBox_25.setText("")
        self.label_33.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u043f\u0440\u0438 \u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0438 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438", None))
        self.checkBox_26.setText("")
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_70.setText("")
        self.label_34.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0442\u0438\u043f \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432", None))
        self.label_35.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u0449\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0439", None))
        self.checkBox_27.setText("")
        self.label_36.setText(QCoreApplication.translate("Widget", u"\u0414\u043b\u044f \u0441\u043b\u0443\u0436\u0435\u0431\u043d\u043e\u0433\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.checkBox_28.setText("")
        self.label_38.setText(QCoreApplication.translate("Widget", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.checkBox_29.setText("")
        self.label_39.setText(QCoreApplication.translate("Widget", u"\u041a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0430\u044f \u0442\u0430\u0439\u043d\u0430", None))
        self.checkBox_30.setText("")
        self.label_40.setText(QCoreApplication.translate("Widget", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.checkBox_31.setText("")
        self.label_54.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432", None))
        self.label_55.setText(QCoreApplication.translate("Widget", u"\u041d\u0435\u0434\u043e\u0440\u043e\u0433\u043e\u0439", None))
        self.checkBox_32.setText("")
        self.label_56.setText(QCoreApplication.translate("Widget", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u043d\u043e\u0439", None))
        self.checkBox_33.setText("")
        self.label_57.setText(QCoreApplication.translate("Widget", u"\u0414\u043e\u0440\u043e\u0433\u043e\u0441\u0442\u043e\u044f\u0449\u0438\u0439", None))
        self.checkBox_34.setText("")
        self.label_58.setText(QCoreApplication.translate("Widget", u"\u042d\u043a\u0441\u043a\u043b\u044e\u0437\u0438\u0432\u043d\u044b\u0439", None))
        self.checkBox_35.setText("")
        self.label_59.setText(QCoreApplication.translate("Widget", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043c\u0435\u0441\u0442\u043e \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432", None))
        self.label_60.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u043b\u0430\u0447\u043d\u043e\u0435 \u0445\u0440\u0430\u043d\u0438\u043b\u0438\u0449\u0435", None))
        self.checkBox_36.setText("")
        self.label_61.setText(QCoreApplication.translate("Widget", u"\u041b\u043e\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.checkBox_37.setText("")
        self.label_62.setText(QCoreApplication.translate("Widget", u"\u041b\u043e\u043a\u0430\u043b\u044c\u043d\u043e \u043d\u0430 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430\u0445", None))
        self.checkBox_38.setText("")
        self.label_63.setText(QCoreApplication.translate("Widget", u"\u041e\u0444\u0438\u0441", None))
        self.checkBox_39.setText("")
        self.label_65.setText(QCoreApplication.translate("Widget", u"\u0412\u0435\u0431-\u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.checkBox_40.setText("")
    # retranslateUi

