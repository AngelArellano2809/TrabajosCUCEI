from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox
from PySide6.QtCore import Slot
from ui_menu_encargado import Ui_MainWindow
from PySide6.QtGui import QFont
import mainwindow
import posgres


class MenuEncar(QMainWindow):
    def __init__(self,id:int):
        super(MenuEncar,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id_museo = id

        self.scene = QGraphicsScene()
        self.ui.eleminar_graphicsView.setScene(self.scene)
        self.act_col_tem()

        self.ui.pushButton_3.clicked.connect(self.addCol)
        self.ui.eli_col_pushButton.clicked.connect(self.eliminarCol)
        self.ui.mod_pushButton.clicked.connect(self.modMuseo)

        self.ui.actionSing_Out.triggered.connect(self.volver_inicio)

    Slot()
    def addCol(self):
        nom = self.ui.add_nom_lineEdit.text()
        desc = self.ui.add_des_lineEdit.text()
        tem = self.ui.add_tem_lineEdit.text()

        if self.ui.per_radioButton.isChecked() == True:
            posgres.addColPer(self.id_museo,nom,desc,tem)

        elif self.ui.tem_radioButton.isChecked() == True:
            ini = self.ui.add_fec_ini_lineEdit.text()
            fin = self.ui.add_fec_fin_lineEdit.text()
            posgres.addColTem(self.id_museo,nom,desc,tem,ini,fin)
            self.act_col_tem()


    @Slot()
    def eliminarCol(self):
        nom = self.ui.eli_col_lineEdit.text()
        posgres.eliminarColTem(nom)
        self.act_col_tem()

    @Slot()
    def modMuseo(self):
        nom = self.ui.mod_nom_lineEdit.text()
        hor = self.ui.mod_hor_lineEdit.text()
        ubi = self.ui.mod_ubi_lineEdit.text()
        con = self.ui.mod_con_lineEdit.text()
        posgres.modificar_datos_museo(self.id_museo,nom,hor,ubi,con)

    @Slot()
    def volver_inicio(self):
        global main
        main = mainwindow.MainWindow()
        main.show()
        self.hide()
    
    def act_col_tem(self):
        self.scene.clear()
        font = QFont("Times", 14)
        cad = posgres.colTem(self.id_museo)
        self.scene.addSimpleText(cad,font)