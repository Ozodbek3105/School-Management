# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentDialogCjVdFW.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
                               QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_StudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(548, 584)
        font = QFont()
        font.setBold(True)
        self.setFont(font)
        self.setStyleSheet(u"QDialog{\n"
                                    "	background-color:white;\n"
                                    "}\n"
                                    "QLineEdit{\n"
                                    "	border:1px solid gray;\n"
                                    "	border-radius:6px;\n"
                                    "	padding-left:15px;\n"
                                    "	height:35px;\n"
                                    "}\n"
                                    "\n"
                                    "QDateEdit{\n"
                                    "	border:1px solid gray;\n"
                                    "	border-radius:6px;\n"
                                    "	padding-left:15px;\n"
                                    "	height:31px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox{\n"
                                    "	border:2px solid white;\n"
                                    "	border-radius:8px;\n"
                                    "    padding:1px 18px 1px 3px;\n"
                                    "	color:white;\n"
                                    "	background-color:black;\n"
                                    "	height:35px;\n"
                                    "	padding-left:15px;\n"
                                    "	font-weight:bold;\n"
                                    "	selection-background-color:#298069\n"
                                    "}\n"
                                    "")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 551, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 411, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable Small Semibol"])
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 100, 531, 401))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Palatino Linotype"])
        font2.setPointSize(12)
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.layoutWidget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.name_lineEdit)

        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.layoutWidget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setFont(font)

        self.verticalLayout_5.addWidget(self.gender_comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_7)

        self.class_comboBox = QComboBox(self.layoutWidget)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")
        self.class_comboBox.setFont(font)

        self.verticalLayout_6.addWidget(self.class_comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.layoutWidget)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")
        font3 = QFont()
        font3.setBold(False)
        self.dob_dateEdit.setFont(font3)

        self.verticalLayout_7.addWidget(self.dob_dateEdit)

        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.address_lineEdit = QLineEdit(self.layoutWidget)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setMinimumSize(QSize(0, 35))
        self.address_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.address_lineEdit)

        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_5)

        self.phone_lineEdit = QLineEdit(self.layoutWidget)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMinimumSize(QSize(0, 35))
        self.phone_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.phone_lineEdit)

        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.email_lineEdit = QLineEdit(self.layoutWidget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.email_lineEdit)

        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(300, 530, 211, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveStudent_btn = QPushButton(self.layoutWidget1)
        self.saveStudent_btn.setObjectName(u"saveStudent_btn")
        self.saveStudent_btn.setMinimumSize(QSize(0, 41))
        self.saveStudent_btn.setMaximumSize(QSize(16777215, 16777215))
        self.saveStudent_btn.setFont(font)
        self.saveStudent_btn.setStyleSheet(u"QPushButton{\n"
                                           "	background-color:#34d481;\n"
                                           "	color:white;\n"
                                           "	border:none;\n"
                                           "	border-radius:8px;\n"
                                           "	font-weight:bold;\n"
                                           "	font-size:15px;\n"
                                           "}")

        self.horizontalLayout_2.addWidget(self.saveStudent_btn)

        self.cancel_btn = QPushButton(self.layoutWidget1)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 41))
        self.cancel_btn.setMaximumSize(QSize(16777215, 16777215))
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
                                      "	background-color:#585858;\n"
                                      "	color:white;\n"
                                      "	border:none;\n"
                                      "	border-radius:8px;\n"
                                      "	font-weight:bold;\n"
                                      "	font-size:15px;\n"
                                      "}")

        self.horizontalLayout_2.addWidget(self.cancel_btn)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self, StudentDialog):
        StudentDialog.setWindowTitle(QCoreApplication.translate("StudentDialog", u"Students Dialog", None))
        self.label.setText(QCoreApplication.translate("StudentDialog", u"Add New Students", None))
        self.label_2.setText(QCoreApplication.translate("StudentDialog", u"Full name", None))
        self.label_6.setText(QCoreApplication.translate("StudentDialog", u"Select Gender", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentDialog", u"Famale", None))

        self.label_7.setText(QCoreApplication.translate("StudentDialog", u"Select Class", None))
        self.class_comboBox.setItemText(0, QCoreApplication.translate("StudentDialog", u"Garde 1", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("StudentDialog", u"Garde 2", None))
        self.class_comboBox.setItemText(2, QCoreApplication.translate("StudentDialog", u"Garde 3", None))
        self.class_comboBox.setItemText(3, QCoreApplication.translate("StudentDialog", u"Garde 4", None))
        self.class_comboBox.setItemText(4, QCoreApplication.translate("StudentDialog", u"Garde 5", None))
        self.class_comboBox.setItemText(5, QCoreApplication.translate("StudentDialog", u"Garde 6", None))
        self.class_comboBox.setItemText(6, QCoreApplication.translate("StudentDialog", u"Garde 7", None))
        self.class_comboBox.setItemText(7, QCoreApplication.translate("StudentDialog", u"Garde 8", None))
        self.class_comboBox.setItemText(8, QCoreApplication.translate("StudentDialog", u"Garde 9", None))
        self.class_comboBox.setItemText(9, QCoreApplication.translate("StudentDialog", u"Garde 10", None))
        self.class_comboBox.setItemText(10, QCoreApplication.translate("StudentDialog", u"Garde 11", None))
        self.class_comboBox.setItemText(11, QCoreApplication.translate("StudentDialog", u"Garde 12", None))

        self.label_8.setText(QCoreApplication.translate("StudentDialog", u"Date of Birth", None))
        self.label_4.setText(QCoreApplication.translate("StudentDialog", u"Adress", None))
        self.label_5.setText(QCoreApplication.translate("StudentDialog", u"Phone Number", None))
        self.label_3.setText(QCoreApplication.translate("StudentDialog", u"Email", None))
        self.saveStudent_btn.setText(QCoreApplication.translate("StudentDialog", u"Add Student", None))
        self.cancel_btn.setText(QCoreApplication.translate("StudentDialog", u"Cancel", None))
    # retranslateUi
