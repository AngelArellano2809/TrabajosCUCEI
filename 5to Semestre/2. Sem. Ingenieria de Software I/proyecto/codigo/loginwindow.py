from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox
from PySide6.QtCore import Slot,Qt
from PySide6.QtGui import QPixmap
from ui_LogWindow import Ui_MainWindow
from PySide6.QtGui import QFont
import mainwindow 
import posgres
from grafo import Grafo
from nodo import Nodo

class LogInWindow(QMainWindow):
    def __init__(self,grafo:Grafo):                                
        super(LogInWindow,self).__init__()

        self.ui = Ui_MainWindow()                       #contructor de la ventana
        self.ui.setupUi(self)
        self.grafo = grafo

        #cancelar porceso
        self.ui.actionRegresar.triggered.connect(self.regresar_inicio)

        #Proceso para acceder
        self.ui.accder_log_pushButton.clicked.connect(self.acceder)

        #Procesos para registrarse en cualquier tipo de cuenta
        self.ui.fan_reg_pushButton.clicked.connect(self.registroFan)
        self.ui.art_reg_pushButton.clicked.connect(self.registroArt)
        self.ui.neg_reg_pushButton.clicked.connect(self.registroNeg)



    #Funcion para regrear al inicio
    @Slot( )
    def regresar_inicio(self):
        global window
        window = mainwindow.MainWindow(0,' ',self.grafo)
        window.show()
        self.hide()

    #Funcion para buscar un artista en la base de datos
    @Slot( )
    def acceder(self):
        usuario = self.ui.usauario_log_lineEdit.text()
        pw = self.ui.pw_log_lineEdit.text()
        log_dup = (0,' ')
        log_dup = posgres.acceso(usuario,pw)
        if log_dup[0] == 0:
            QMessageBox.warning(self,"Error","No existe ese usuario")
        elif log_dup[1] == ' ':
            QMessageBox.warning(self,"Error","Contraseña Incorrecta")
        else:
            global window
            window = mainwindow.MainWindow(log_dup[0],log_dup[1],self.grafo)
            window.show()
            self.hide()

    @Slot( )
    def registroFan(self):
        nombre = self.ui.nombre_fan_reg_lineEdit.text()
        pw = self.ui.pw_fan_reg_lineEdit.text()
        pref = self.ui.pref_fan_reg_lineEdit.text()
        val = posgres.regFan(nombre,pw,pref)
        if val == True:
            self.agregarNodo(posgres.getId(nombre),'F',0)
            QMessageBox.information(self,"Exito","Se creo el usuario")

    @Slot( )
    def registroArt(self):
        nombre = self.ui.nombre_art_reg_lineEdit.text()
        area = self.ui.area_art_reg_lineEdit.text()
        genero = self.ui.genero_art_reg_lineEdit.text()
        estado = self.ui.ubi_art_reg_lineEdit.text()
        usuario = self.ui.usuario_art_reg_lineEdit.text()
        pw = self.ui.pw_art_reg_lineEdit.text()
        val = posgres.regArt(nombre,area,genero,estado,usuario,pw)
        if val == True:
            self.agregarNodo(posgres.getId(usuario),'A',0)
            QMessageBox.information(self,"Exito","Se creo el usuario")

    @Slot( )
    def registroNeg(self):
        nombre = self.ui.nomNeg_neg_reg_lineEdit.text()
        usuario = self.ui.nomEnc_neg_reg_lineEdit.text()
        pw = self.ui.pw_neg_reg_lineEdit.text()
        contacto = self.ui.contacto_neg_reg_lineEdit.text()
        pref = self.ui.pref_neg_reg_lineEdit.text()
        dir = self.ui.dir_neg_reg_lineEdit.text()
        val = posgres.regNeg(nombre,usuario,pw,contacto,pref,dir)
        if val == True:
            self.agregarNodo(posgres.getId(usuario),'N',0)
            QMessageBox.information(self,"Exito","Se creo el usuario")

    def agregarNodo(self,idReal,tipo,peso):
        id = len(self.grafo.vertices)+1 #self.id_cont
        nodo = Nodo(id,idReal,tipo,peso)
        self.grafo.agrega_nodo(nodo)
        self.grafo.agrega_aristas_vacia()
        #self.grafo.guardarVertices('J:/Trabajos 5 CUCEI/2. Sem. Ingenieria de Software I/proyecto/codigo/Vertises.json')
        print(str(self.grafo))