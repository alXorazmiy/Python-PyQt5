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

        self.error_icon = QPixmap("icons/error2.png")
        self.success_icon = QPixmap("icons/success.png")

        self.icon_label = QLabel(self)
        self.icon_label.setPixmap(self.error_icon.scaled(25, 25, Qt.KeepAspectRatio))
        self.icon_label.setStyleSheet("background:none, margin-left:10px")
        self.icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.icon_label)

        message_layout = QVBoxLayout(self)
        

        self.label = QLabel("", self)
        self.label.setStyleSheet("color: white; background: none")
        self.label.setFixedWidth(220)
        self.label.setFixedHeight(20)

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
            self.label.setStyleSheet("color: #1b9c85")

        elif status == "error":
            self.icon_label.setPixmap(self.error_icon.scaled(25, 25, Qt.KeepAspectRatio))
            self.label.setStyleSheet("color: #ff0060")


        self.label.setText(message)
        self.label2.setText(message2) 


        self.setStyleSheet(f"background-color: #2c384a; border:none; border-radius: 4px")
     
    def show_notification(self):
        self.show()

    def hide_notification(self):
        self.hide()
