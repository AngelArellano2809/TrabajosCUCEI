from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox
from PySide2.QtCore import Slot
from PySide2.QtGui import QFont
from ui_home import Ui_MainWindow
from loginwindow import LoginWindow
import posgres
import detalleswindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.museos_relevantes()

        self.ui.buscar_pushButton.clicked.connect(self.buscar_museo)
        self.ui.sign_in_pushButton.clicked.connect(self.signIn)
        
    @Slot( )
    def buscar_museo(self):
        museo_name = self.ui.buscar_lineEdit.text()
        museo_id = posgres.buscarMuseo(museo_name)
        if museo_id == None:
            QMessageBox.warning(self,"Error","No existe ese museo")
        else:
            global detalles
            detalles = detalleswindow.DetallesWindow(museo_id)
            detalles.show()
            self.hide()

    @Slot( )
    def signIn(self):
        global login
        login = LoginWindow()
        login.show()
        self.hide()
        
    def museos_relevantes(self):
        font = QFont("Times", 14)
        cad = posgres.musRelevantes()
        self.scene.addSimpleText(cad,font)