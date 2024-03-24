import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLabel,
    )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Моё приложение")
        
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
             
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()