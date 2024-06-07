import sys

from PySide6.QtWidgets import QApplication

from front_page import MySchool

app = QApplication(sys.argv)
window = MySchool()
window.show()
app.exec()
