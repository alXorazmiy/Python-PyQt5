from PyQt5.QtWidgets import  QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMovie,QFont



class LoginPage(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.UI()
        self.error = False
        self.parent = parent 

    def UI(self):
        self.setStyleSheet("background-color: #1d2633")

        login_layout = QVBoxLayout()
        username_label = QLabel("Username", self)
        username_label.setAlignment(Qt.AlignLeft)
        login_layout.addWidget(username_label)

        self.username_textfield = QLineEdit(self)
        self.username_textfield.setFixedHeight(30)
        self.username_textfield.setFixedWidth(250)
        self.username_textfield.setStyleSheet("background-color: #2c384a; border: none")
        login_layout.addWidget(self.username_textfield)

        password_label = QLabel("Password", self)
        password_label.setAlignment(Qt.AlignLeft)
        password_label.setStyleSheet("margin-top: 10px")
        login_layout.addWidget(password_label)

        self.password_textfield = QLineEdit(self)
        self.password_textfield.setFixedHeight(30)
        self.password_textfield.setFixedWidth(250)
        self.password_textfield.setStyleSheet("background-color: #2c384a; border: none")
        login_layout.addWidget(self.password_textfield)

        self.button = QLabel("Sign in", self)
        self.button.setAlignment(Qt.AlignCenter)
        self.button.setFixedHeight(70)
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.setStyleSheet("margin-top: 30px; border: none; background-color: #008bff;")
        self.button.mousePressEvent = self.on_click
        login_layout.addWidget(self.button)
        login_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(login_layout)

        buttonFont = QFont()
        buttonFont.setPointSize(12)
        buttonFont.setWeight(QFont.Bold) 

        self.button.setFont(buttonFont)
        
       
       
        
    def on_click(self, event):

        self.gif = QMovie("gif/loader.gif")
        self.gif.setScaledSize(QSize(20, 20))
        self.button.setText("")  
        self.button.setMovie(self.gif)
        self.gif.start()  
        self.button.show()

        username = self.username_textfield.text()
        password = self.password_textfield.text()

        if username == "admin":
            if password == "admin":
                self.parent.notification.set_message("Successfully", "message", "#1b9c85", "success")
                self.parent.show_notification()
                
            else:
                pass
               
        else:
            self.parent.notification.set_message("Error", "Login yoki Parol xato!", "#ff0060", "error")
            self.parent.show_notification()
        self.gif.stop()
        self.button.setText("Sign in")

        

