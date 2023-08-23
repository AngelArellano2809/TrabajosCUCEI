from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox
from PySide6.QtCore import Slot
from ui_detalles_museo import Ui_MainWindow
from PySide6.QtGui import QFont
import mainwindow 
import posgres

class DetallesWindow(QMainWindow):
    def __init__(self,id:int):
        super(DetallesWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id_museo = id

        font = QFont("Times", 14)

        self.act_esp = QGraphicsScene()
        self.ui.act_esp_graphicsView.setScene(self.act_esp)
        str1 = posgres.actividades_especiales(self.id_museo)
        self.act_esp.addSimpleText(str1,font)
        self.desc_mus = QGraphicsScene()
        self.ui.desc_mus_graphicsView.setScene(self.desc_mus)
        str2 = posgres.descripcion(self.id_museo)
        self.desc_mus.addSimpleText(str2,font)
        self.acc_mus = QGraphicsScene()
        self.ui.acc_mus_graphicsView.setScene(self.acc_mus)
        str3 = posgres.accesivilidad(self.id_museo)
        self.acc_mus.addSimpleText(str3,font)
        self.horario = QGraphicsScene()
        self.ui.horarios_graphicsView.setScene(self.horario)
        str4 = posgres.horario(self.id_museo)
        self.horario.addSimpleText(str4,font)
        self.col_per = QGraphicsScene()
        self.ui.col_per_graphicsView.setScene(self.col_per)
        str5 = posgres.colPer(self.id_museo)
        self.col_per.addSimpleText(str5,font)
        self.col_tem = QGraphicsScene()
        self.ui.col_tem_graphicsView.setScene(self.col_tem)
        str6 = posgres.colTem(self.id_museo)
        self.col_tem.addSimpleText(str6,font)

        self.ui.actionVolver_al_inicio.triggered.connect(self.volver_inicio)

    @Slot()
    def volver_inicio(self):
        global main
        main = mainwindow.MainWindow()
        main.show()
        self.hide()
