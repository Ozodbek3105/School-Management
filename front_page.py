import os
import sys
import psycopg2
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QMainWindow

from ui_interfeys import Ui_MainWindow


# def resource_path(relative_path):
#     """ .py va .exe ikkala holatda ishlaydigan qilish """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
#     return os.path.join(base_path, relative_path)

class MySchool(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("School Managment")

        # Hide Widget Menu
        self.icon_only_widget.setHidden(True)

        # Hide Dropdown
        self.students_dropdown.setHidden(True)
        self.teacher_dropdown.setHidden(True)
        self.busines_dropdown.setHidden(True)

        # Connect Button switch to different page
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)
        self.institution_1.clicked.connect(self.switch_to_institution_page)
        self.institution_2.clicked.connect(self.switch_to_institution_page)
        self.student_info.clicked.connect(self.switch_to_studentInfo_page)
        self.student_payments.clicked.connect(self.switch_to_studentpayments_page)
        self.student_transactions.clicked.connect(self.switch_to_studentTransaction_page)
        self.teacher_info.clicked.connect(self.switch_to_teacherInfo_page)
        self.teacher_salaries.clicked.connect(self.switch_to_teacherSalaries_page)
        self.teacher_transactions.clicked.connect(self.switch_to_teacherTransactions_page)
        self.budgets.clicked.connect(self.switch_to_budegts_page)
        self.expenses.clicked.connect(self.switch_to_expenses_page)
        self.busines_overview.clicked.connect(self.switch_to_budgetOverview_page)
        self.setting_2.clicked.connect(self.switch_to_setting_page)
        self.setting_1.clicked.connect(self.switch_to_setting_page)
        self.manage_students_1.clicked.connect(self.students_context_menu)
        self.manage_teacher_1.clicked.connect(self.teachers_context_menu)
        self.manage_finances_1.clicked.connect(self.finances_context_menu)

    # Methods to switch to different page
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_institution_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_studentInfo_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_studentpayments_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_studentTransaction_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_teacherInfo_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_teacherSalaries_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_teacherTransactions_page(self):
        self.stackedWidget.setCurrentIndex(7)

    def switch_to_budegts_page(self):
        self.stackedWidget.setCurrentIndex(8)

    def switch_to_expenses_page(self):
        self.stackedWidget.setCurrentIndex(9)

    def switch_to_budgetOverview_page(self):
        self.stackedWidget.setCurrentIndex(10)

    def switch_to_setting_page(self):
        self.stackedWidget.setCurrentIndex(11)

    # methods to show context menus
    def students_context_menu(self):
        self.show_custom_context_menu(self.manage_students_1,
                                      ["Student Information", "Student Payments", "Student Transactions"])

    def teachers_context_menu(self):
        self.show_custom_context_menu(self.manage_teacher_1,
                                      ["Teacher Information", "Teacher Salaries", "Teacher Transactions"])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.manage_finances_1,
                                      ["Budgets", "Expenses", "Business Overview"])

    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)

        # set style for the menu
        menu.setStyleSheet("""
                              QMenu{
                            background-color:black;
                            color:white;
                            }
                            QMenu:selected{
                            background-color:white;
                            color:#12B298;
                            }""")
        # Add action to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)
        # show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()
        if text == "Student Information":
            self.switch_to_studentInfo_page()
        elif text == "Student Payments":
            self.switch_to_studentpayments_page()
        elif text == "Student Transactions":
            self.switch_to_studentTransaction_page()
        elif text == "Teacher Information":
            self.switch_to_teacherInfo_page()
        elif text == "Teacher Salaries":
            self.switch_to_teacherSalaries_page()
        elif text == "Teacher Transactions":
            self.switch_to_teacherTransactions_page()
        elif text == "Budgets":
            self.switch_to_budegts_page()
        elif text == "Expenses":
            self.switch_to_expenses_page()
        elif text == "Business Overview":
            self.switch_to_budgetOverview_page()

    # CREATE DATABASE CONNECTION
    def create_connection(self):
        # Replace these with your actual pgAdmin server details
        self.conn = psycopg2.connect(database="school",
                                     host="localhost",
                                     user="postgres",
                                     password="admin",
                                     port="5432")
        # Create a cursor to execute SQL queries
        cursor = self.conn
        