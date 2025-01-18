from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import Qt

class Notification(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(300, 80)  
        self.UI()

    def UI(self):
        layout = QHBoxLayout(self)

        self.error_icon = QPixmap("assets/icons/error.png")
        self.success_icon = QPixmap("assets/icons/success_white.png")

        self.icon_label = QLabel(self)
        self.icon_label.setPixmap(self.error_icon.scaled(25, 25, Qt.KeepAspectRatio))
        self.icon_label.setStyleSheet("background: none;")
        self.icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.icon_label)

        message_layout = QVBoxLayout()
        

        self.label = QLabel("", self)
        
        self.label.setFixedWidth(220)
        self.label.setFixedHeight(20)
        self.label.setStyleSheet("color: white; background: none")

        self.label.setAlignment(Qt.AlignLeft)
    

        lablefont = QFont()
        lablefont.setPointSize(12)
        lablefont.setWeight(QFont.Bold) 

        self.label.setFont(lablefont)
        


        self.label2 = QLabel("", self)
        self.label2.setStyleSheet("color: white; background: none")
        self.label2.setFixedWidth(220)
        self.label2.setFixedHeight(20)
        self.label2.setAlignment(Qt.AlignLeft)

        message_layout.setAlignment(Qt.AlignTop)
    
        message_layout.addWidget(self.label)
        message_layout.addWidget(self.label2)

        layout.addLayout(message_layout) 
        self.setLayout(layout)


        



    def set_message(self, message, message2, color, status):

        if status == "success":
            self.icon_label.setPixmap(self.success_icon.scaled(25, 25, Qt.KeepAspectRatio))
            self.setStyleSheet("background-color: #1b9c85; border: none; border-radius: 6px")


        elif status == "error":
            self.icon_label.setPixmap(self.error_icon.scaled(25, 25, Qt.KeepAspectRatio))
            self.setStyleSheet("background-color: #ff0060; border: none; border-radius: 6px")
          


        self.label.setText(message)
        self.label2.setText(message2) 


     
    def show_notification(self):
        self.show()

    def hide_notification(self):
        self.hide()