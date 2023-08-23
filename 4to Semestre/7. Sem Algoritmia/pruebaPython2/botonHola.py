from PySide6.QtWidgets import QPushButton, QApplication
import sys
#APlicacion de Qt
app = QApplication()

#Se crea un boton con la palabra hola
button = QPushButton('Hola')

#Se hace visible el boton
button.show()

#Qt loop
sys.exit(app.exec_())