from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Notification(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(300, 80)  
        self.UI()

    def UI(self):
        layout = QHBoxLayout(self)

        self.error_icon = QPixmap("icons/error.png")
        self.success_icon = QPixmap("icons/success.png")

        self.icon_label = QLabel(self)
        self.icon_label.setPixmap(self.error_icon.scaled(25, 25, Qt.KeepAspectRatio))
        layout.addWidget(self.icon_label)

        self.label = QLabel("Error message goes here", self)
        self.label.setStyleSheet("color: white;font-size: 14px;")
        self.label.setFixedWidth(220)
        self.label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label)

        close_icon = QPixmap("icons/close.png")
        close_icon_label = QLabel(self)
        close_icon_label.setStyleSheet("margin-left: 40px")
        close_icon_label.setPixmap(close_icon.scaled(20, 20, Qt.KeepAspectRatio)) 
        
        layout.addWidget(close_icon_label)
        self.setLayout(layout)

    def set_message(self, message, color, status):
        if status == "success":
            self.icon_label.setPixmap(self.success_icon.scaled(25, 25, Qt.KeepAspectRatio))
        elif status == "error":
            self.icon_label.setPixmap(self.error_icon.scaled(25, 25, Qt.KeepAspectRatio))


        self.label.setText(message)
        self.setStyleSheet(f"background-color: {color}; border:none")

    def show_notification(self):
        self.show()

    def hide_notification(self):
        self.hide()
