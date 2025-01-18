
from PyQt5.QtWidgets import QFrame,QDesktopWidget,QLabel,QVBoxLayout,QHBoxLayout,QSpacerItem,QSizePolicy
from PyQt5.QtGui import QPixmap,QMovie
from PyQt5.QtCore import Qt,QSize

class Loader(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1d2633")
        screen = QDesktopWidget().screenGeometry()
        self.setFixedSize(screen.width() - 250, screen.height())
        self.UI()



    def UI(self):
        v_layout = QVBoxLayout()


        self.label = QLabel(self)

        self.gif = QMovie("./assets/gif/loader.gif")
        self.gif.setScaledSize(QSize(20, 20))
        self.label.setMovie(self.gif)
        self.gif.start()       
        
        
        v_layout.addWidget(self.label)
        v_layout.setAlignment(Qt.AlignCenter)
   


        self.setLayout(v_layout)
