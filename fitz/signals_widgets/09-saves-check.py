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
        
        self.button_is_checked = True
        
        self.setWindowTitle("Моё приложение")
        
        self.button = QPushButton("Нажмите здесь")
        self.button.setCheckable(True)
        self.button.released.connect(
            self.the_button_was_released
        )
        self.button.setChecked(self.button_is_checked)
        
        self.setFixedSize(QSize(400, 300))
        
        self.setCentralWidget(self.button)
        
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        
        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
