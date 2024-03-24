import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Моё приложение")
        
        widget = QLabel("Hello, World!")
        font = widget.font()
        font.setPointSize(24)
        widget.setFont(font)
        
        align_top_left = Qt.AlignLeft | Qt.AlignTop
        widget.setAlignment(align_top_left)

        self.setCentralWidget(widget)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
