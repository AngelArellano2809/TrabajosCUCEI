from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from ui_MainWindow import Ui_MainWindow
import posgres
import profilewindow 
import loginwindow
from grafo import Grafo

class MainWindow(QMainWindow):
    def __init__(self,log:int,type:chr,grafo:Grafo):                                    #variables necesarias para iniicar la ui
        super(MainWindow,self).__init__()

        self.ui = Ui_MainWindow()   #Iniciador
        self.ui.setupUi(self)
        self.cuenta = log
        self.tipo = type
        self.grafo = grafo

        self.Re1 = 0
        self.Re2 = 0
        self.Re3 = 0
        self.Re4 = 0
        self.Re5 = 0
        self.Re6 = 0
        self.Re7 = 0

        #Recuperar y crear informacion grafo
        self.ui.actionAbrir_Vertices.triggered.connect(self.action_abrirArchivoVertices)
        self.ui.actionAbrir_Aristas.triggered.connect(self.action_abrirArchivoAristas)
        self.ui.actionGuardar_Vertices.triggered.connect(self.action_guardarArchivoVertices)
        self.ui.actionGuardar_Aristas.triggered.connect(self.action_guardarArchivoAristas)

        #Boton para buscar un artista
        self.ui.buscar_pushButton.clicked.connect(self.buscar_artista)

        #Poreseso de log in y log out
        self.ui.actionAcceder.triggered.connect(self.action_logIn)
        self.ui.actionSalir.triggered.connect(self.action_logOut)

        #Algoritmo de recoemndacion General
        self.ui.pushButton.clicked.connect(self.gerarRecomendacion)
        self.ui.art1_pushButton.clicked.connect(self.recArt1)
        self.ui.art2_pushButton.clicked.connect(self.recArt2)
        self.ui.art3_pushButton.clicked.connect(self.recArt3)
        self.ui.art4_pushButton.clicked.connect(self.recArt4)
        self.ui.art5_pushButton.clicked.connect(self.recArt5)
        self.ui.art6_pushButton.clicked.connect(self.recArt6)
        self.ui.art7_pushButton.clicked.connect(self.recArt7)

    #Funcion para generar una recoemndacion dependiendo de las preferencias del usuario
    @Slot( )
    def gerarRecomendacion(self):
        info = posgres.recomedacionGneral(posgres.getPref(self.cuenta,self.tipo))
        print(info)
        self.ui.art1_pushButton.setText(info[0][0])
        self.Re1=info[0][1]

        self.ui.art2_pushButton.setText(info[1][0])
        self.Re2=info[1][1]

        self.ui.art3_pushButton.setText(info[2][0])
        self.Re3=info[2][1]

        self.ui.art4_pushButton.setText(info[3][0])
        self.Re4=info[3][1]

        self.ui.art5_pushButton.setText(info[4][0])
        self.Re5=info[4][1]
        
        self.ui.art6_pushButton.setText(info[5][0])
        self.Re6=info[5][1]

        self.ui.art7_pushButton.setText(info[6][0])
        self.Re7=info[6][1]

    #Funcion para buscar un artista en la base de datos
    @Slot( )
    def buscar_artista(self):
        artista_name = self.ui.buscar_lineEdit.text()
        artista_id = posgres.buscarArtista(artista_name)
        if artista_id == None:
            QMessageBox.warning(self,"Error","No existe ese artista")
        else:
            self.openProfile(artista_id)

    @Slot( )
    def action_logIn(self):
        if self.cuenta == 0 and self.tipo == ' ':
            global logIn
            logIn = loginwindow.LogInWindow(self.grafo)
            logIn.show()
            self.hide()
        else:
            QMessageBox.warning(self,"Error","Ya ha accedido a una cuenta")

    @Slot( )
    def action_logOut(self):
        self.cuenta = 0
        self.tipo = ' ' 

    @Slot()
    def action_abrirArchivoVertices(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if (self.grafo.abrirVertices(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "El archivo se cargó correctamente " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo cargar el archivo " + ubicacion
            )
    
    @Slot()
    def action_guardarArchivoVertices(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]
        print(ubicacion)
        if (self.grafo.guardarVertices(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "El archivo se guardó correctamente " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def action_abrirArchivoAristas(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if (self.grafo.abrirAristas(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "El archivo se cargó correctamente " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo cargar el archivo " + ubicacion
            )
    
    @Slot()
    def action_guardarArchivoAristas(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]
        print(ubicacion)
        if (self.grafo.guardarAristas(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "El archivo se guardó correctamente " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot( )
    def recArt1(self):
        self.openProfile(self.Re1)
    @Slot( )
    def recArt2(self):
        self.openProfile(self.Re2)
    @Slot( )
    def recArt3(self):
        self.openProfile(self.Re3)
    @Slot( )
    def recArt4(self):
        self.openProfile(self.Re4)
    @Slot( )
    def recArt5(self):
        self.openProfile(self.Re5)
    @Slot( )
    def recArt6(self):
        self.openProfile(self.Re6)
    @Slot( )
    def recArt7(self):
        self.openProfile(self.Re7)

    def openProfile(self,artista_id):
        global profile
        profile = profilewindow.ProfileWindow(artista_id,self.cuenta,self.tipo,self.grafo)
        profile.show()
        self.hide()