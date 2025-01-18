
from PyQt5.QtWidgets import  QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QMovie
from .component.sidebar import Sidebar
from pages.home.home import HomePage
from pages.settings.settings import SettingsPage
from components.loader import Loader


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1d2633")

        self.UI()

    def UI(self):
        self.setWindowTitle("Dashboard Page")

        self.sidebar = Sidebar(self)
        self.sidebar.move(0,0)


        self.loader = Loader(self)
        self.loader.move(250, 0)
        self.loader.hide()

        self.home = HomePage(self)
        self.home.move(300, 50)

        self.settings = SettingsPage(self)
        self.settings.move(300, 50)
        self.settings.hide()

            

            


            

