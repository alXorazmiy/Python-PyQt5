import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout
from PyQt5.QtCore import Qt 

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('1-app')


        layout = QVBoxLayout()
        label = QLabel('Assalomu alaykum! bu 1 - app', self)
        label.setAlignment(Qt.AlignCenter)


        layout.addWidget(label)

        self.setLayout(layout)      
        self.setGeometry(300, 300, 300, 200)

  

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
