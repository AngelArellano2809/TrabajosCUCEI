from PySide2.QtWidgets import QMainWindow, QApplication
from mainwindow import MainWindow
import sys

#APlicacion de Qt
app = QApplication()

#Se crea una ventana vacia
window = MainWindow()

#Se hace visible la ventana
window.show()

#Qt loop
sys.exit(app.exec_())