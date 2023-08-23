from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from admin import Admin
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.admin = Admin()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ingresar_pushButton.clicked.connect(self.click_agregar)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot( )
    def click_agregar(self):
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(destino_x,destino_y,velocidad,red,green,blue)
        self.admin.agrega_final(particula)

    @Slot( )
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.admin))
