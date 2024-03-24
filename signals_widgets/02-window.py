import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

window = QPushButton("Нажми здесь")
window.show()

app.exec()
