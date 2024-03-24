import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QLabel,
    QWidget,
    )

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
                
        self.setWindowTitle("Моё приложение")
        
        self.setMinimumSize(QSize(200, 150))
        
        layout = QGridLayout()
        
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("purple"), 2, 1)
                
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
