from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,QVBoxLayout,QLabel,QGridLayout,QLineEdit
from PyQt6.QtCore import Qt 


# app settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Cal2025")
main_window.resize(250,200)


# all objects

display = QLineEdit()
grid = QGridLayout()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

clear = QPushButton("Clear")
delete = QPushButton("<")

# design
master_layout = QVBoxLayout()

master_layout.addWidget(display)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addLayout(button_row)

main_window.setLayout(master_layout)
# run the app
main_window.show()
app.exec()