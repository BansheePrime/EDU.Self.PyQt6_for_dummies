from PyQt6 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle("Говорим по-русски!")
window.resize(300, 70)
label = QtWidgets.QLabel("<center><h1>Привет, мир!</h1></center>")
btnQuit = QtWidgets.QPushButton("&Закрыть")

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)

window.setLayout(vbox)

btnQuit.clicked.connect(app.quit)


window.show()
sys.exit(app.exec())
