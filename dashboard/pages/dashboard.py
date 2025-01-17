
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QMovie



class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("Dashboard Page")
        layout = QVBoxLayout()

        label = QLabel("Welcome to the Dashboard!")
        layout.addWidget(label)

        self.setLayout(layout)

        

# class DashboardPage(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Dashboard Page")
#         layout = QVBoxLayout()

#         label = QLabel("Welcome to the Dashboard!")
#         layout.addWidget(label)

#         self.setLayout(layout)