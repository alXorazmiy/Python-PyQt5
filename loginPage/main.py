import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QDesktopWidget,QStackedWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFontDatabase,QFont

from pages.login import LoginPage
from pages.dashboard import DashboardPage
from components.notification import Notification




class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("Dashboard")
        self.setStyleSheet("background-color: #1d2633")


        font_path = "fonts/Montserrat-Regular.ttf"  
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family)
            font.setPointSize(12) 
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
        screen = QDesktopWidget().screenGeometry()
        self.notification.move(screen.width() - self.notification.width() - 50, screen.height() - self.notification.height() - 100)
        self.notification.hide_notification()


        self.showMaximized()

    def hide_notification(self):
        self.notification.hide_notification()

    def show_notification(self):
        self.notification.show_notification()
        QTimer.singleShot(10000, self.hide_notification)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
