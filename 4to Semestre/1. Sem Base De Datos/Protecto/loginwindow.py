from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtCore import Slot
from ui_log_in import Ui_MainWindow
import posgres
from menuAdminWindow import MenuAdmin
from menuEncarWindow import MenuEncar

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.log_in_pushButton.clicked.connect(self.signin)

    @Slot( )
    def signin(self):
        user = self.ui.nombre_usuario_lineEdit.text()
        pwd = self.ui.contasea_lineEdid.text()
        tipo = posgres.login(user,pwd)
        if tipo[0] == 'ADMIN':
            global menuAdmin
            menuAdmin = MenuAdmin()
            menuAdmin.show()
            self.hide()
        elif tipo[0] == 'ENCAR':
            global menuEncar
            menuEncar = MenuEncar(tipo[1])
            menuEncar.show()
            self.hide()
        else:
            QMessageBox.warning(self,"Error","Usuario Incorrecto")


