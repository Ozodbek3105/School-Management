# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfeyspSBTGj.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1556, 866)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/imges/images/logo (1).png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/imges/images/dashboardsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/imges/images/dashboardsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.dashboard_1)

        self.institution_1 = QPushButton(self.icon_only_widget)
        self.institution_1.setObjectName(u"institution_1")
        icon1 = QIcon()
        icon1.addFile(u":/imges/images/institutionsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/imges/images/institutionsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.institution_1.setIcon(icon1)
        self.institution_1.setIconSize(QSize(100, 20))
        self.institution_1.setCheckable(True)
        self.institution_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.institution_1)

        self.manage_students_1 = QPushButton(self.icon_only_widget)
        self.manage_students_1.setObjectName(u"manage_students_1")
        icon2 = QIcon()
        icon2.addFile(u":/imges/images/studentssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/imges/images/studentssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.manage_students_1.setIcon(icon2)
        self.manage_students_1.setIconSize(QSize(100, 20))
        self.manage_students_1.setCheckable(True)
        self.manage_students_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.manage_students_1)

        self.manage_teacher_1 = QPushButton(self.icon_only_widget)
        self.manage_teacher_1.setObjectName(u"manage_teacher_1")
        icon3 = QIcon()
        icon3.addFile(u":/imges/images/teacherssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/imges/images/teacherssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.manage_teacher_1.setIcon(icon3)
        self.manage_teacher_1.setIconSize(QSize(100, 20))
        self.manage_teacher_1.setCheckable(True)
        self.manage_teacher_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.manage_teacher_1)

        self.manage_finances_1 = QPushButton(self.icon_only_widget)
        self.manage_finances_1.setObjectName(u"manage_finances_1")
        icon4 = QIcon()
        icon4.addFile(u":/imges/images/financessmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/imges/images/financessmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.manage_finances_1.setIcon(icon4)
        self.manage_finances_1.setIconSize(QSize(100, 20))
        self.manage_finances_1.setCheckable(True)
        self.manage_finances_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.manage_finances_1)


        self.verticalLayout_11.addLayout(self.verticalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(17, 432, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(28)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 10)
        self.setting_1 = QPushButton(self.icon_only_widget)
        self.setting_1.setObjectName(u"setting_1")
        icon5 = QIcon()
        icon5.addFile(u":/imges/images/settingssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/imges/images/settingssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.setting_1.setIcon(icon5)
        self.setting_1.setIconSize(QSize(100, 19))
        self.setting_1.setCheckable(True)
        self.setting_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.setting_1)

        self.exit_1 = QPushButton(self.icon_only_widget)
        self.exit_1.setObjectName(u"exit_1")
        icon6 = QIcon()
        icon6.addFile(u":/imges/images/signoutsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/imges/images/signoutsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.exit_1.setIcon(icon6)
        self.exit_1.setIconSize(QSize(100, 18))
        self.exit_1.setCheckable(True)
        self.exit_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.exit_1)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"}\n"
"QPushButtons{\n"
"	heigh:30px;\n"
"	border:none;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/imges/images/logo (1).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 25, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/imges/images/dashboard2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/imges/images/dashboard1.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_2.setIcon(icon7)
        self.dashboard_2.setIconSize(QSize(100, 45))
        self.dashboard_2.setCheckable(True)

        self.verticalLayout_7.addWidget(self.dashboard_2)

        self.institution_2 = QPushButton(self.icon_text_widget)
        self.institution_2.setObjectName(u"institution_2")
        self.institution_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-65px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/imges/images/institution2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/imges/images/institution1.png", QSize(), QIcon.Normal, QIcon.On)
        self.institution_2.setIcon(icon8)
        self.institution_2.setIconSize(QSize(100, 45))
        self.institution_2.setCheckable(True)

        self.verticalLayout_7.addWidget(self.institution_2)

        self.frame = QFrame(self.icon_text_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.manage_students_2 = QPushButton(self.frame)
        self.manage_students_2.setObjectName(u"manage_students_2")
        icon9 = QIcon()
        icon9.addFile(u":/imges/images/students3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/imges/images/students4.png", QSize(), QIcon.Normal, QIcon.On)
        self.manage_students_2.setIcon(icon9)
        self.manage_students_2.setIconSize(QSize(200, 45))
        self.manage_students_2.setCheckable(True)

        self.verticalLayout_3.addWidget(self.manage_students_2)

        self.students_dropdown = QFrame(self.frame)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.students_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.student_info = QPushButton(self.students_dropdown)
        self.student_info.setObjectName(u"student_info")
        self.student_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.student_info.setCheckable(True)

        self.verticalLayout.addWidget(self.student_info)

        self.student_payments = QPushButton(self.students_dropdown)
        self.student_payments.setObjectName(u"student_payments")
        self.student_payments.setStyleSheet(u"QPushButton{\n"
"	padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.student_payments.setCheckable(True)

        self.verticalLayout.addWidget(self.student_payments)

        self.student_transactions = QPushButton(self.students_dropdown)
        self.student_transactions.setObjectName(u"student_transactions")
        self.student_transactions.setStyleSheet(u"QPushButton{\n"
"	padding-left:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.student_transactions.setCheckable(True)

        self.verticalLayout.addWidget(self.student_transactions)


        self.verticalLayout_3.addWidget(self.students_dropdown)


        self.verticalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.icon_text_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.manage_teacher_2 = QPushButton(self.frame_2)
        self.manage_teacher_2.setObjectName(u"manage_teacher_2")
        icon10 = QIcon()
        icon10.addFile(u":/imges/images/teachers3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/imges/images/teachers4.png", QSize(), QIcon.Normal, QIcon.On)
        self.manage_teacher_2.setIcon(icon10)
        self.manage_teacher_2.setIconSize(QSize(200, 45))
        self.manage_teacher_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.manage_teacher_2)

        self.teacher_dropdown = QFrame(self.frame_2)
        self.teacher_dropdown.setObjectName(u"teacher_dropdown")
        self.teacher_dropdown.setFrameShape(QFrame.StyledPanel)
        self.teacher_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.teacher_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teacher_info = QPushButton(self.teacher_dropdown)
        self.teacher_info.setObjectName(u"teacher_info")
        self.teacher_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.teacher_info.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_info)

        self.teacher_salaries = QPushButton(self.teacher_dropdown)
        self.teacher_salaries.setObjectName(u"teacher_salaries")
        self.teacher_salaries.setStyleSheet(u"QPushButton{\n"
"	padding-left:0;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.teacher_salaries.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_salaries)

        self.teacher_transactions = QPushButton(self.teacher_dropdown)
        self.teacher_transactions.setObjectName(u"teacher_transactions")
        self.teacher_transactions.setStyleSheet(u"QPushButton{\n"
"	padding-left:27px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.teacher_transactions.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_transactions)


        self.verticalLayout_4.addWidget(self.teacher_dropdown)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.icon_text_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.manage_finances_2 = QPushButton(self.frame_3)
        self.manage_finances_2.setObjectName(u"manage_finances_2")
        icon11 = QIcon()
        icon11.addFile(u":/imges/images/finances3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/imges/images/finances4.png", QSize(), QIcon.Normal, QIcon.On)
        self.manage_finances_2.setIcon(icon11)
        self.manage_finances_2.setIconSize(QSize(200, 45))
        self.manage_finances_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.manage_finances_2)

        self.busines_dropdown = QFrame(self.frame_3)
        self.busines_dropdown.setObjectName(u"busines_dropdown")
        self.busines_dropdown.setFrameShape(QFrame.StyledPanel)
        self.busines_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.busines_dropdown)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.budgets = QPushButton(self.busines_dropdown)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setStyleSheet(u"QPushButton{\n"
"	padding-left:-40px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.budgets.setCheckable(True)

        self.verticalLayout_5.addWidget(self.budgets)

        self.expenses = QPushButton(self.busines_dropdown)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setStyleSheet(u"QPushButton{\n"
"	padding-left:-30px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.expenses.setCheckable(True)

        self.verticalLayout_5.addWidget(self.expenses)

        self.busines_overview = QPushButton(self.busines_dropdown)
        self.busines_overview.setObjectName(u"busines_overview")
        self.busines_overview.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.busines_overview.setCheckable(True)

        self.verticalLayout_5.addWidget(self.busines_overview)


        self.verticalLayout_6.addWidget(self.busines_dropdown)


        self.verticalLayout_7.addWidget(self.frame_3)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(38, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.setting_2 = QPushButton(self.icon_text_widget)
        self.setting_2.setObjectName(u"setting_2")
        self.setting_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-65px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/imges/images/settings2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/imges/images/settings1.png", QSize(), QIcon.Normal, QIcon.On)
        self.setting_2.setIcon(icon12)
        self.setting_2.setIconSize(QSize(200, 45))
        self.setting_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.setting_2)

        self.exit_2 = QPushButton(self.icon_text_widget)
        self.exit_2.setObjectName(u"exit_2")
        self.exit_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/imges/images/signout2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/imges/images/signout1.png", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2.setIcon(icon13)
        self.exit_2.setIconSize(QSize(200, 45))
        self.exit_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.exit_2)


        self.verticalLayout_12.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon14 = QIcon()
        icon14.addFile(u":/imges/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 25, -1, 25)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_13.addWidget(self.label)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(86, 86, 86);")

        self.verticalLayout_13.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(322, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	border-radius:10px;\n"
"}")
        self.label_6.setPixmap(QPixmap(u":/imges/images/img_1.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addWidget(self.header_widget, 0, 0, 1, 1)

        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(841, 741))
        self.main_screen_widget.setMaximumSize(QSize(16777215, 741))
        self.main_screen_widget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.main_screen_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(841, 741))
        self.stackedWidget.setMaximumSize(QSize(16777215, 741))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 300, 231, 151))
        font3 = QFont()
        font3.setPointSize(25)
        self.label_7.setFont(font3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 290, 251, 161))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.select_gender = QComboBox(self.page_3)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 0))
        self.select_gender.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setBold(True)
        self.select_gender.setFont(font4)
        self.select_gender.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius:8px;\n"
"    padding:1px 18px 1px 3px;\n"
"	color:white;\n"
"	background-color:black;\n"
"	height:35px;\n"
"	padding-left:15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#298069\n"
"}")

        self.horizontalLayout_7.addWidget(self.select_gender)

        self.select_class = QComboBox(self.page_3)
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(150, 0))
        self.select_class.setMaximumSize(QSize(16777215, 16777215))
        self.select_class.setFont(font4)
        self.select_class.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius:8px;\n"
"    padding:1px 18px 1px 3px;\n"
"	color:white;\n"
"	background-color:black;\n"
"	height:35px;\n"
"	padding-left:15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#298069\n"
"}")

        self.horizontalLayout_7.addWidget(self.select_class)

        self.search_student = QLineEdit(self.page_3)
        self.search_student.setObjectName(u"search_student")
        self.search_student.setMinimumSize(QSize(450, 38))
        self.search_student.setMaximumSize(QSize(450, 37))
        self.search_student.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.search_student)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.addStudent_btn = QPushButton(self.page_3)
        self.addStudent_btn.setObjectName(u"addStudent_btn")
        self.addStudent_btn.setMinimumSize(QSize(150, 41))
        self.addStudent_btn.setMaximumSize(QSize(150, 16777215))
        self.addStudent_btn.setFont(font4)
        self.addStudent_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:12px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/imges/images/add student.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addStudent_btn.setIcon(icon15)

        self.horizontalLayout_6.addWidget(self.addStudent_btn)

        self.excelExport_btn = QPushButton(self.page_3)
        self.excelExport_btn.setObjectName(u"excelExport_btn")
        self.excelExport_btn.setMinimumSize(QSize(150, 41))
        self.excelExport_btn.setMaximumSize(QSize(150, 16777215))
        self.excelExport_btn.setFont(font4)
        self.excelExport_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:#34d481;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:12px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/imges/images/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.excelExport_btn.setIcon(icon16)

        self.horizontalLayout_6.addWidget(self.excelExport_btn)

        self.pdfExport_btn = QPushButton(self.page_3)
        self.pdfExport_btn.setObjectName(u"pdfExport_btn")
        self.pdfExport_btn.setMinimumSize(QSize(150, 41))
        self.pdfExport_btn.setMaximumSize(QSize(150, 16777215))
        self.pdfExport_btn.setFont(font4)
        self.pdfExport_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 93, 93);\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:12px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/imges/images/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pdfExport_btn.setIcon(icon17)

        self.horizontalLayout_6.addWidget(self.pdfExport_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setFamilies([u"Myanmar Text"])
        font5.setPointSize(20)
        font5.setBold(True)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        font6 = QFont()
        font6.setFamilies([u"Myanmar Text"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.label_19.setFont(font6)
        self.label_19.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.studentinfo_table = QTableWidget(self.page_3)
        if (self.studentinfo_table.columnCount() < 9):
            self.studentinfo_table.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.studentinfo_table.setObjectName(u"studentinfo_table")
        self.studentinfo_table.setMaximumSize(QSize(16777215, 542))
        self.studentinfo_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	background-color:black;\n"
"	color:white;\n"
"}\n"
"QTableWidget{\n"
"	alternate-background-color:#BOEDFB;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.studentinfo_table.setAlternatingRowColors(True)

        self.gridLayout_3.addWidget(self.studentinfo_table, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(240, 230, 351, 171))
        self.label_10.setFont(font3)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(220, 210, 411, 171))
        self.label_11.setFont(font3)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(260, 250, 381, 171))
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(250, 220, 311, 181))
        self.label_13.setFont(font3)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(260, 250, 411, 171))
        self.label_14.setFont(font3)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(280, 220, 231, 171))
        self.label_15.setFont(font3)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(300, 220, 271, 171))
        self.label_16.setFont(font3)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(260, 230, 341, 171))
        self.label_17.setFont(font3)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(330, 220, 201, 171))
        self.label_18.setFont(font3)
        self.stackedWidget.addWidget(self.page_12)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.main_screen_widget, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.manage_students_2.toggled.connect(self.students_dropdown.setHidden)
        self.manage_finances_2.toggled.connect(self.busines_dropdown.setHidden)
        self.manage_teacher_2.toggled.connect(self.teacher_dropdown.setHidden)
        self.institution_2.toggled.connect(self.institution_1.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.manage_students_2.toggled.connect(self.manage_students_1.setChecked)
        self.manage_teacher_2.toggled.connect(self.manage_teacher_1.setChecked)
        self.manage_finances_2.toggled.connect(self.manage_finances_1.setChecked)
        self.setting_2.toggled.connect(self.setting_1.setChecked)
        self.exit_2.toggled.connect(self.exit_1.setChecked)
        self.exit_1.toggled.connect(MainWindow.close)
        self.exit_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.institution_1.setText("")
        self.manage_students_1.setText("")
        self.manage_teacher_1.setText("")
        self.manage_finances_1.setText("")
        self.setting_1.setText("")
        self.exit_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"School", None))
        self.dashboard_2.setText("")
        self.institution_2.setText("")
        self.manage_students_2.setText("")
        self.student_info.setText(QCoreApplication.translate("MainWindow", u"Stundent Information", None))
        self.student_payments.setText(QCoreApplication.translate("MainWindow", u"Stundent Payments", None))
        self.student_transactions.setText(QCoreApplication.translate("MainWindow", u"Stundent Transactions", None))
        self.manage_teacher_2.setText("")
        self.teacher_info.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.teacher_salaries.setText(QCoreApplication.translate("MainWindow", u"Teacher salaries", None))
        self.teacher_transactions.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.manage_finances_2.setText("")
        self.budgets.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.busines_overview.setText(QCoreApplication.translate("MainWindow", u"Busines Overview", None))
        self.setting_2.setText("")
        self.exit_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello, Ozodbek", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search, Here...", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dahsboard", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Famale", None))

        self.select_class.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT CLASS", None))
        self.select_class.setItemText(1, QCoreApplication.translate("MainWindow", u"Garde 1", None))
        self.select_class.setItemText(2, QCoreApplication.translate("MainWindow", u"Garde 2", None))
        self.select_class.setItemText(3, QCoreApplication.translate("MainWindow", u"Garde 3", None))
        self.select_class.setItemText(4, QCoreApplication.translate("MainWindow", u"Garde 4", None))
        self.select_class.setItemText(5, QCoreApplication.translate("MainWindow", u"Garde 5", None))
        self.select_class.setItemText(6, QCoreApplication.translate("MainWindow", u"Garde 6", None))
        self.select_class.setItemText(7, QCoreApplication.translate("MainWindow", u"Garde 7", None))
        self.select_class.setItemText(8, QCoreApplication.translate("MainWindow", u"Garde 8", None))
        self.select_class.setItemText(9, QCoreApplication.translate("MainWindow", u"Garde 9", None))
        self.select_class.setItemText(10, QCoreApplication.translate("MainWindow", u"Garde 10", None))
        self.select_class.setItemText(11, QCoreApplication.translate("MainWindow", u"Garde 11", None))
        self.select_class.setItemText(12, QCoreApplication.translate("MainWindow", u"Garde 12", None))

        self.search_student.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search, Student...", None))
        self.addStudent_btn.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.excelExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.pdfExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to PDF ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Info", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Welcome to the student Information page", None))
        ___qtablewidgetitem = self.studentinfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.studentinfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Student id", None));
        ___qtablewidgetitem2 = self.studentinfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.studentinfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem4 = self.studentinfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birthday", None));
        ___qtablewidgetitem5 = self.studentinfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem6 = self.studentinfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem7 = self.studentinfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem8 = self.studentinfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Teacher salaries", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Busines Overview", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

