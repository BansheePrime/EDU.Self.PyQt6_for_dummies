import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Моё приложение")
        
        button = QPushButton("Нажмите здесь")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        
        self.setFixedSize(QSize(400, 300))
        
        self.setCentralWidget(button)
        
    def the_button_was_clicked(self):
        print("Нажали!")
        
    def the_button_was_toggled(self, checked):
        print("Нажали??", checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
