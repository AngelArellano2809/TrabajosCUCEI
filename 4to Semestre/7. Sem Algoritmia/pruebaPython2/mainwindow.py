from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):#reserva memoria para mostrar ventana
        super(MainWindow,self).__init__()#constructor para reservar memoria
        #clase hija
        ui = Ui_MainWindow()
        ui.setupUi(self)

        ui.pushButton.clicked.connect(self.click_agregar)

    @Slot( )
    def click_agregar(self):
        print('click')
