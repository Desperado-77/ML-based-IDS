# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSplitter, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(940, 564)
        self.verticalLayout_11 = QVBoxLayout(Form)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget_3 = QWidget(self.splitter)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_1 = QPushButton(self.frame)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.verticalLayout.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout_2.setStretch(3, 3)

        self.verticalLayout_9.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.frame_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_3.addWidget(self.radioButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout.addWidget(self.pushButton_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 1, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 2, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.splitter.addWidget(self.widget_3)
        self.container = QWidget(self.splitter)
        self.container.setObjectName(u"container")
        self.verticalLayout_12 = QVBoxLayout(self.container)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lable_show = QLabel(self.container)
        self.lable_show.setObjectName(u"lable_show")
        self.lable_show.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lable_show)

        self.splitter.addWidget(self.container)

        self.verticalLayout_11.addWidget(self.splitter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u53ef\u89c6\u5316", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"service\u7edf\u8ba1\u56fe", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"label\u7edf\u8ba1\u56fe", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"protocol_type\u7edf\u8ba1\u56fe", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"flag\u7edf\u8ba1\u56fe", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"target\u7edf\u8ba1\u56fe", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"attack_type\u7edf\u8ba1\u56fe", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u7b97\u6cd5\u9009\u62e9", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u51b3\u7b56\u6811\u6a21\u578b", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u903b\u8f91\u56de\u5f52\u6a21\u578b", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u4eba\u5de5\u795e\u7ecf\u7f51\u7edc\u6a21\u578b", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Go", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6a21\u578b\u8bc4\u4f30", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7ed8\u5236\u6df7\u6dc6\u77e9\u9635", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Go", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4e09\u4e2a\u6a21\u578b\u7684\u51c6\u786e\u7387\u6bd4\u8f83", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u8bef\u62a5\u7387\u548c\u6f0f\u62a5\u7387\u6bd4\u8f83", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"Go", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Go", None))
        self.lable_show.setText("")
    # retranslateUi

