
from PyQt5.QtWidgets import QFrame,QDesktopWidget,QLabel,QVBoxLayout,QHBoxLayout,QSpacerItem,QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class SettingsPage(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #2c384a")
        screen = QDesktopWidget().screenGeometry()
        self.setFixedSize(screen.width() - 350, screen.height() - 150 )
        self.UI()


    def UI(self):
        
        v_layout = QVBoxLayout()

     
        
        label = QLabel("SettingsPage",self)
        v_layout.addWidget(label)
        v_layout.setAlignment(Qt.AlignCenter)
   


        self.setLayout(v_layout)





    