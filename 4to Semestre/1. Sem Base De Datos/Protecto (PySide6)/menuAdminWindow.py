from PySide6.QtWidgets import QMainWindow, QGraphicsScene
from PySide6.QtCore import Slot
from ui_menu_admin import Ui_MainWindow
from PySide6.QtGui import QFont
import mainwindow
import posgres


class MenuAdmin(QMainWindow):
    def __init__(self):
        super(MenuAdmin,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.ui.eleminar_graphicsView.setScene(self.scene)
        self.act_mus()

        self.ui.add_mus_pushButton.clicked.connect(self.addMus)
        self.ui.eli_mus_pushButton.clicked.connect(self.eliminarMus)
        self.ui.eli_mus_lineEdit.setPlaceholderText("ID Museo")
        self.ui.add_encar_pushButton.clicked.connect(self.addEmcar)

        self.ui.actionSing_Out.triggered.connect(self.volver_inicio)

    @Slot()
    def addMus(self):
        id =  int(self.ui.add_id_lineEdit.text())
        nom = self.ui.add_nom_lineEdit.text()
        hor = self.ui.add_hor_lineEdit.text()
        ubi = self.ui.add_ubi_lineEdit.text()
        con = self.ui.add_con_lineEdit.text()
        posgres.addMuseo(id,nom,hor,ubi,con)

    @Slot()
    def eliminarMus(self):
        id = int(self.ui.eli_mus_lineEdit.text())
        posgres.eliMuseo(id)

    @Slot()
    def addEmcar(self):
        id =  int(self.ui.add_id_encar_lineEdit.text())
        nom = self.ui.add_nom_encar_lineEdit.text()
        con = self.ui.add_con_encar_lineEdit.text()
        usu = self.ui.add_usu_encar_lineEdit_3.text()
        pwd = self.ui.add_pwd_encar_lineEdit.text()
        posgres.addEncar(id,nom,con,usu,pwd)

    @Slot()
    def volver_inicio(self):
        global main
        main = mainwindow.MainWindow()
        main.show()
        self.hide()

    def act_mus(self):
        self.scene.clear()
        font = QFont("Times", 14)
        cad = posgres.musRelevantes()
        self.scene.addSimpleText(cad,font)