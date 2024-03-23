import sys
from random import choice

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
)

window_titles = [
    "My App1", 
    "My App2", 
    "Still My App3", 
    "Still My App4", 
    "What on earth5", 
    "What on earth6", 
    "This is surprising7", 
    "This is surprising8", 
    "Something went wrong",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # self.button_is_checked = True
        
        self.setWindowTitle("Моё приложение")
        
        self.button = QPushButton("Нажмите здесь")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        self.windowTitleChanged.connect(
            self.the_window_title_changed    
        )

        self.setFixedSize(QSize(200, 150))
        
        self.setCentralWidget(self.button)
        
    def the_button_was_clicked(self):
        print("Нажали")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        # self.button.setText("Уже кликнул")
        self.setWindowTitle(new_window_title)
                               
    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        
        if window_title == "Something went wrong":
            self.button.setDisabled(True)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
