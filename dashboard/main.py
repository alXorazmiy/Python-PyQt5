import sys
from PyQt5.QtWidgets import QApplication, QFrame,QMainWindow, QLabel, QDesktopWidget, QHBoxLayout,QStackedWidget,QVBoxLayout
from PyQt5.QtCore import Qt,QSize, QTimer
from PyQt5.QtGui import QMovie,QColor,QPixmap

from pages.login import LoginPage
from pages.dashboard import DashboardPage
from pages.notification import Notification
from utils.utils import notification_status

from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("Dashboard")
        self.setStyleSheet("background-color: #1d2633")


        self.stacked_widget = QStackedWidget(self)


        self.login_page = LoginPage(self)
        self.dashboard_page = DashboardPage()

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.dashboard_page)
        
        self.setCentralWidget(self.stacked_widget)



       
        self.notification = Notification(self)
        screen = QDesktopWidget().screenGeometry()
        self.notification.move(screen.width() - self.notification.width() - 50, screen.height() - self.notification.height() - 100)
        self.notification.hide_notification()


        self.showMaximized()

    def hide_notification(self):
        self.notification.hide_notification()

    def show_notification(self):
        self.notification.show_notification()
        QTimer.singleShot(3000, self.hide_notification)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
