import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class AnimationExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Animation Example')
        self.setGeometry(100, 100, 300, 200)

        # Tugmani yaratish
        self.button = QPushButton('Click Me', self)
        self.button.setGeometry(50, 50, 200, 50)

        # Animatsiyani yaratish
        self.animation = QPropertyAnimation(self.button, b"geometry")
        self.animation.setDuration(2000)  # 2 sekund davomida
        self.animation.setStartValue(QRect(50, 50, 200, 50))  # Boshlang'ich joylashuv
        self.animation.setEndValue(QRect(50, 150, 200, 50))  # Oxirgi joylashuv

        # Tugmaga bosilganda animatsiyani boshlash
        self.button.clicked.connect(self.startAnimation)

    def startAnimation(self):
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AnimationExample()
    ex.show()
    sys.exit(app.exec_())
