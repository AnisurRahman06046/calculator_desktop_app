from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,QVBoxLayout,QLabel
from PyQt6.QtCore import Qt 


# app settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Cal2025")
main_window.resize(600,600)







# run the app
main_window.show()
app.exec()