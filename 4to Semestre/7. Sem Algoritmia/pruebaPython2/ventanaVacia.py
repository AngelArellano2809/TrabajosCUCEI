from PySide6.QtWidgets import QMainWindow, QApplication
import sys
#APlicacion de Qt
app = QApplication()

#Se crea una ventana vacia
window = QMainWindow()

#Se hace visible la ventana
window.show()

#Qt loop
sys.exit(app.exec_())