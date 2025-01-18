import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QStackedWidget
from PyQt5.QtCore import QTimer,Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QFontDatabase, QFont

from pages.login.login import LoginPage
from pages.dashboard.dashboard import DashboardPage
from components.notification import Notification


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.screen = QDesktopWidget().screenGeometry()
        self.UI()

    def UI(self):
        self.setWindowTitle("Dashboard")
        self.setStyleSheet("background-color: #1d2633")

        font_path = "assets/fonts/Montserrat-Regular.ttf"  
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family)
            font.setPointSize(10) 
            QApplication.setFont(font)
        else:
            print("Fontni yuklashda xato yuz berdi")

        self.stacked_widget = QStackedWidget(self)

        self.login_page = LoginPage(self)
        self.dashboard_page = DashboardPage()

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.dashboard_page)  
        
        self.setCentralWidget(self.stacked_widget)

        self.notification = Notification(self)
        self.notification.setGeometry(self.screen.width() + self.notification.width() + 70, self.screen.height() - self.notification.height() - 120, self.notification.width(), self.notification.height())
        # self.notification.move(self.screen.width() - self.notification.width() - 70, self.screen.height() - self.notification.height() - 120)

        self.showMaximized()

    def hide_notification(self):


        self.animation = QPropertyAnimation(self.notification, b"geometry")
        self.animation.setDuration(400)  
        self.animation.setStartValue(QRect(self.screen.width() - self.notification.width() - 70, self.screen.height() - self.notification.height() - 120, self.notification.width(), self.notification.height()))
        self.animation.setEndValue(QRect(self.screen.width() +  self.notification.width() + 70, self.screen.height() - self.notification.height() - 120, self.notification.width(), self.notification.height())) 
        self.animation.start()
        # self.notification.hide_notification()

    def show_notification(self):
        # self.notification.show_notification()

        self.animation = QPropertyAnimation(self.notification, b"geometry")
        self.animation.setDuration(400)  
        self.animation.setStartValue(QRect(self.screen.width() +  self.notification.width() + 70, self.screen.height() - self.notification.height() - 120, self.notification.width(), self.notification.height()))  
        self.animation.setEndValue(QRect(self.screen.width() - self.notification.width() - 70, self.screen.height() - self.notification.height() - 120, self.notification.width(), self.notification.height()))
        self.animation.start()
        QTimer.singleShot(5000, self.hide_notification)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
