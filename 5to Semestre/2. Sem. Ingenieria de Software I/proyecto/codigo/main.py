from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys
from grafo import Grafo

app = QApplication(sys.argv)
grafo = Grafo()
window = MainWindow(0,' ',grafo)
window.show()

sys.exit(app.exec())
