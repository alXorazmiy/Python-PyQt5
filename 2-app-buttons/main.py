import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.label = QLabel(f"{self.counter}", self)
        self.UI()

    def UI(self):
        self.setWindowTitle("2-app-buttons")

        label_layout = QVBoxLayout()
        self.label.setAlignment(Qt.AlignCenter)
        label_layout.addWidget(self.label)

   
        button_layout = QVBoxLayout()
        button = QPushButton("Oshirish", self)
      
        button.clicked.connect(self.oshirish)
        button_layout.addWidget(button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(label_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setGeometry(100, 100, 300, 300)


    def oshirish(self):
        self.counter += 1
        self.label.setText(f"{self.counter}")
        self.label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()

    ex.show()
    sys.exit(app.exec_())
