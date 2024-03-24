import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QPushButton,
    QTabWidget,
    )

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
                
        self.setWindowTitle("Моё приложение")
        
        self.setMinimumSize(QSize(200, 150))
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        
        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        
        self.setCentralWidget(tabs)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
