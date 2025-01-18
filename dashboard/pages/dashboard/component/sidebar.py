
from PyQt5.QtWidgets import QFrame,QDesktopWidget,QLabel,QVBoxLayout,QHBoxLayout,QSpacerItem,QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer

class Sidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #2c384a")
        screen = QDesktopWidget().screenGeometry()
        self.setFixedSize(250, screen.height())
        self.UI()

        self.dashboard = parent


    def UI(self):
        icon = QPixmap("assets/img/logo.png")
        self.logo_icon = QLabel(self)
        self.logo_icon.setPixmap(icon.scaled(50, 50, Qt.KeepAspectRatio))  # Rasmni 100x100 o'lchamda ko'rsatish
     
        
        self.logo_label = QLabel("Dashboard",self)
        self.logo_label.setAlignment(Qt.AlignLeft)

    


        sidebar_layout = QVBoxLayout(self)
        spacer = QSpacerItem(0, 40)  
        sidebar_layout.addItem(spacer)



        logo_layout = QHBoxLayout()
        logo_layout.addWidget(self.logo_icon)
        logo_layout.addWidget(self.logo_label)
        logo_layout.setAlignment(Qt.AlignCenter)
        sidebar_layout.addLayout(logo_layout)


        spacer = QSpacerItem(0, 40)  
        sidebar_layout.addItem(spacer)
        
        hr_label  = QLabel(self)
        hr_label.setStyleSheet("border: 1px solid #E2DFD2")
        hr_label.setFixedHeight(1)
        sidebar_layout.addWidget(hr_label)

        spacer = QSpacerItem(0, 20)  
        sidebar_layout.addItem(spacer)
        self.create_sidebar_link(sidebar_layout, "Home", "assets/icons/home.png")
        self.create_sidebar_link(sidebar_layout, "Schedule", "assets/icons/schedule.png")
        self.create_sidebar_link(sidebar_layout, "Users", "assets/icons/user.png")
        self.create_sidebar_link(sidebar_layout, "Statistics", "assets/icons/statistics.png")
        self.create_sidebar_link(sidebar_layout, "Location", "assets/icons/location.png")


        self.create_sidebar_link(sidebar_layout, "Settings", "assets/icons/settings.png")
        self.create_sidebar_link(sidebar_layout, "Support", "assets/icons/support.png")
        sidebar_layout.setAlignment(Qt.AlignTop)
        self.setLayout(sidebar_layout)







    def create_sidebar_link(self, layout, label, icon_path):

        button = QLabel(self)
        

        icon = QPixmap(icon_path)  
        icon_label = QLabel(self)
        icon_label.setPixmap(icon.scaled(20, 20)) 
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setFixedWidth(30)
        

        text_label = QLabel(label, self)
        text_label.setStyleSheet("color: white") 
        text_label.setAlignment(Qt.AlignLeft)


        button_layout = QHBoxLayout(button)
        button_layout.addWidget(icon_label)
        button_layout.addWidget(text_label)


        button.setFixedHeight(30)
        button.setStyleSheet("margin-left: 10px")
        button.setCursor(Qt.PointingHandCursor)
        layout.addWidget(button)
        
    
        button.mousePressEvent = lambda event, label=label: self.on_button_click(event, label)
    
    def on_button_click(self, event, label):

        def hide_all_page(self):
            self.dashboard.home.hide()
            self.dashboard.settings.hide()
            
  
        hide_all_page(self)

        if label == "Home":
            self.dashboard.loader.show()
            QTimer.singleShot(500, self.dashboard.home.show) 
          
            

        elif label == "Settings":
            self.dashboard.loader.show()
            QTimer.singleShot(500, self.dashboard.settings.show) 
          