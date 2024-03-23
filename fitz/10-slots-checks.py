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
        
        # self.button_is_checked = True
        
        self.setWindowTitle("Моё приложение")
        
        self.button = QPushButton("Нажмите здесь")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        self.setFixedSize(QSize(200, 150))
        
        self.setCentralWidget(self.button)
        
    def the_button_was_clicked(self):
        # self.button.setText("Уже кликнул")
        self.setWindowTitle("Новый заголовок")
        self.button.setEnabled(False)
                       
        # self.setWindowTitle("Ваншот")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
