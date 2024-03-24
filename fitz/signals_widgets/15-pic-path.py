import os
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    )

basedir = os.path.dirname(__file__)
print("Current working directory: ", os.getcwd())
print("Paths are relative to: ", basedir)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Моё приложение")
        
        widget = QLabel("Hello, Yachiru!")
        widget.setPixmap(QPixmap(os.path.join(basedir, "./pic/yachiru.png")))
        # widget.setScaledContents(True)
        
        self.setCentralWidget(widget)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
