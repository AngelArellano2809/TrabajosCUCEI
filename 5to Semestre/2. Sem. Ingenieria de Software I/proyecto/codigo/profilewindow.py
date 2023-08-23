from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox
from PySide6.QtCore import Slot,Qt
from PySide6.QtGui import QPixmap
from PIL import Image
import json
from ui_ProfileWindow import Ui_ProfileWindow
import mainwindow 
import posgres
from grafo import Grafo

class ProfileWindow(QMainWindow):
    def __init__(self,id:int,log:int,type:chr,grafo:Grafo):                     #variables necesarias para iniicar la ui
        super(ProfileWindow,self).__init__()

        self.ui = Ui_ProfileWindow()                                           #contructor de la ventana
        self.ui.setupUi(self)
        self.id_artista = id                                                   #define el id del artista
        self.cuenta = log
        self.tipo = type
        self.grafo = grafo
        

        #Texto de las etiquetas
        self.ui.info_label.setText(posgres.infoArtista(self.id_artista))       #coloca la informacion del artista (nombre, area, genero)
        self.ui.ubicacion_label.setText(posgres.ubicacion(self.id_artista))    #coloca la ubicacion del artista
        self.ui.seguidores_label.setText(posgres.seguidores(self.id_artista))  #coloca los seguidores del artista
        self.ui.Titulo.setStyleSheet("color: white; background-color: rgba(0, 255, 255, 0%);")

        #Publicaciones
        self.showPublicacion()

        #Imagenes del perfil
        if (posgres.topImagen(self.id_artista) != None): # valida que exita un foto
            #imagen de arriba del perfil
            img_top = 'J:/Trabajos 5 CUCEI/2. Sem. Ingenieria de Software I/proyecto/codigo/imagenes artista/' + posgres.topImagen(self.id_artista)
                #Mostrar Imagen
            pixmap = QPixmap(img_top)
            self.ui.top_imegen_label.setPixmap(pixmap)
            self.ui.top_imegen_label.setScaledContents(True)
            self.ui.top_imegen_label.setAlignment(Qt.AlignCenter)
            
            #imagen de perfil principal
            img_profile = 'J:/Trabajos 5 CUCEI/2. Sem. Ingenieria de Software I/proyecto/codigo/imagenes artista/' + posgres.perfilImagen(self.id_artista)
                #Mostrar Imagen
            pixmap = QPixmap(img_profile)
            self.ui.perfil_imagen_label.setPixmap(pixmap)
            self.ui.perfil_imagen_label.setScaledContents(True)
            self.ui.perfil_imagen_label.setAlignment(Qt.AlignCenter)
            
        #ciclar las ventanas
        self.ui.home_pushButton.clicked.connect(self.volver_inicio)

        #barra de busqueda
        self.ui.buscar_pushButton.clicked.connect(self.buscar_artista)

        #votar por publicaciones de artista no propias
        self.ui.up_pushButtonP1.clicked.connect(self.agregar_peso_arista)
        self.ui.up_pushButtonP1.clicked.connect(self.changeColor1)
        self.ui.up_pushButtonP2.clicked.connect(self.agregar_peso_arista)
        self.ui.up_pushButtonP2.clicked.connect(self.changeColor2)
        self.ui.up_pushButtonP3.clicked.connect(self.agregar_peso_arista)
        self.ui.up_pushButtonP3.clicked.connect(self.changeColor3)
        self.ui.up_pushButtonP4.clicked.connect(self.agregar_peso_arista)
        self.ui.up_pushButtonP4.clicked.connect(self.changeColor4)
        self.ui.up_pushButtonP5.clicked.connect(self.agregar_peso_arista)
        self.ui.up_pushButtonP5.clicked.connect(self.changeColor5)

        

    #funcion para mostrar las publicaciones del artista de cuatro en cuatro
    @Slot()
    def showPublicacion(self):
        info = posgres.infoPublicacion(self.id_artista)
        self.ui.tituloP1.setText(info[0][0])
        self.ui.descrP1.setText(info[0][1] + '\n' + str(info[0][2]))
        self.ui.ImagenP1.setText(info[0][3])

        self.ui.tituloP2.setText(info[1][0])
        self.ui.descrP2.setText(info[1][1] + '\n' + str(info[1][2]))
        self.ui.ImagenP2.setText(info[1][3])

        self.ui.tituloP3.setText(info[2][0])
        self.ui.descrP3.setText(info[2][1] + '\n' + str(info[2][2]))
        self.ui.ImagenP3.setText(info[2][3])

        self.ui.tituloP4.setText(info[3][0])
        self.ui.descrP4.setText(info[3][1] + '\n' + str(info[3][2]))
        self.ui.ImagenP4.setText(info[3][3])

        self.ui.tituloP5.setText(info[4][0])
        self.ui.descrP5.setText(info[4][1] + '\n' + str(info[4][2]))
        self.ui.ImagenP5.setText(info[4][3])

    #funcion para regresar a home
    @Slot()
    def volver_inicio(self):
        global main
        main = mainwindow.MainWindow(self.cuenta,self.tipo,self.grafo)
        main.show()
        self.hide()

    #funcion para buscar otro artista
    @Slot( )
    def buscar_artista(self):
        artista_name = self.ui.buscar_lineEdit.text()
        artista_id = posgres.buscarArtista(artista_name)
        if artista_id == None:
            QMessageBox.warning(self,"Error","No existe ese artista")
        else:
            global profile
            profile = ProfileWindow(artista_id,self.cuenta,self.tipo,self.grafo)
            profile.show()
            self.hide()

    @Slot( )
    def agregar_peso_arista(self):
        if (self.id_artista == self.cuenta and self.tipo == 'A') or (self.cuenta == 0):
            QMessageBox.warning(self,"Error","No puedes votar por esta cuenta")
        else:
            inicio = 0
            final = 0
            cont = 0
            pos = 0
            copiagraf = self.grafo.vertices
            for ver in copiagraf:
                if ver.real==self.cuenta and ver.tipo==self.tipo:
                    inicio = ver.id
                elif ver.real==self.id_artista and ver.tipo=='A':
                    pos = cont
                    final = ver.id
                cont +=1
            self.grafo.agrega_arista(inicio-1,final-1)
            self.grafo.vertices[pos].incPeso()
            posgres.addPeso(self.id_artista)

    def changeColor1(self):
        self.ui.up_pushButtonP1.setStyleSheet("background-color: gold")
    def changeColor2(self):
        self.ui.up_pushButtonP2.setStyleSheet("background-color: gold")
    def changeColor3(self):
        self.ui.up_pushButtonP3.setStyleSheet("background-color: gold")
    def changeColor4(self):
        self.ui.up_pushButtonP4.setStyleSheet("background-color: gold")
    def changeColor5(self):
        self.ui.up_pushButtonP5.setStyleSheet("background-color: gold")