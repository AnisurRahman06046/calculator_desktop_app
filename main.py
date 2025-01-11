from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,QVBoxLayout,QLabel,QGridLayout,QLineEdit
from PyQt6.QtCore import Qt 


# app settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Cal2025")
main_window.resize(600,600)


# all objects

display = QLineEdit()
grid = QGridLayout()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]


# run the app
main_window.show()
app.exec()