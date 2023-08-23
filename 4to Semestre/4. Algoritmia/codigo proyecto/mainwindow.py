from PySide2.QtWidgets import QMainWindow, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor,QFont
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem
from grafo import Grafo
from nodo import Nodo
from random import randint
#from arista import Arista

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.grafo = Grafo()
        self.id_cont = 1

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.ingresar_ver_pushButton.clicked.connect(self.click_agregar)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.agregar_asi_pushButton.clicked.connect(self.agregar_asintota)

        self.ui.mostrar_grafo_pushButton.clicked.connect(self.mostrar_grafo)
        self.ui.dijkstra_pushButton.clicked.connect(self.dijkstra)

        

    @Slot( )
    def mostrar_grafo(self):
        pen = QPen()
        pen.setWidth(2)
        fila = 0
        for arista in self.grafo.artistas:
            columna = 0
            for distancia in arista:
                if distancia != '-':
                    x1 = self.grafo.vertices[fila].origen_x
                    y1 = self.grafo.vertices[fila].origen_y
                    x2 = self.grafo.vertices[columna].origen_x
                    y2 = self.grafo.vertices[columna].origen_y
                    color = QColor(51,116,255)#azul
                    pen.setColor(color)
                    self.scene.addLine(x1,y1,x2,y2,pen)
                columna+=1
            fila+=1
        for vertice in self.grafo.vertices:
            x = vertice.origen_x
            y = vertice.origen_y

            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            color = QColor(r,g,b)
            pen.setColor(color)
            self.scene.addEllipse(x-1.5,y-1.5,3,3,pen)
            font = QFont("Times", 2)
            self.scene.addSimpleText(vertice.nombre,font).setPos(x-8,y-6)

    def camino(self):
        for planeta in self.grafo.vertices:
            print("Distancia del vertice: " + str(planeta.nombre) + " es " + str(planeta.distancia) + " llegando desde " + str(planeta.padre))
        camino = []
        actual = len(self.grafo.vertices)-1
        while actual != None:
            camino.insert(0,actual)
            actual = self.grafo.vertices[actual].padre
        print(camino, self.grafo.vertices[len(self.grafo.vertices)-1].distancia)

        #mostrar en grafo
        pen = QPen()
        pen.setWidth(2)
        color = QColor(245,101,206)#rosa
        pen.setColor(color)
        for planeta in self.grafo.vertices:
            if planeta.padre != None:
                x1 = planeta.origen_x
                y1 = planeta.origen_y
                x2 = self.grafo.vertices[planeta.padre].origen_x
                y2 = self.grafo.vertices[planeta.padre].origen_y
                self.scene.addLine(x1,y1,x2,y2,pen)
    
    def minimo(self, lista):
        if len(lista) > 0:
            ver = self.grafo.vertices[lista[0]].distancia
            min = lista[0]
            for planeta in lista:
                if ver > self.grafo.vertices[planeta].distancia:
                    ver = self.grafo.vertices[planeta].distancia
                    min = planeta
            return min
    
    @Slot( )
    def dijkstra(self):
        inicio = 0
        self.grafo.vertices[inicio].distancia = 0
        actual = inicio
        noVisitados = []
        for planeta in self.grafo.vertices:
            if inicio != self.grafo.vertices.index(planeta):
                planeta.distancia = float('inf')
            planeta.padre = None
            noVisitados.append(self.grafo.vertices.index(planeta))

        while len(noVisitados) > 0:
            pos = 0
            for dist in self.grafo.artistas[actual].distancias:
                if self.grafo.vertices[pos].visitado == False:
                    if dist != '-':
                        if self.grafo.vertices[actual].distancia + dist < self.grafo.vertices[pos].distancia:
                            self.grafo.vertices[pos].distancia = self.grafo.vertices[actual].distancia + dist
                            self.grafo.vertices[pos].padre = actual
                pos+=1
            self.grafo.vertices[actual].visitado = True
            noVisitados.remove(actual)
            actual = self.minimo(noVisitados)
        self.camino()
        
    @Slot( )
    def agregar_asintota(self):
        inicio = self.ui.inicio_pinBox.value()
        final = self.ui.final_spinBox.value()
        distancia = self.ui.distancia_doubleSpinBox.value()
        self.grafo.agrega_arista(inicio-1,final-1,distancia)

    @Slot( )
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(len(self.grafo))
        self.ui.tabla.setRowCount(len(self.grafo))
        row = 0
        for arista in self.grafo:
            i = 0
            for distancia in arista:
                widget = QTableWidgetItem(str(distancia))
                self.ui.tabla.setItem(row,i,widget)
                i+=1
            row += 1
    
    @Slot( )
    def click_agregar(self):
        id = self.id_cont
        nombre = self.ui.nombre_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        nodo = Nodo(id,nombre,origen_x,origen_y)
        self.grafo.agrega_nodo(nodo)
        self.grafo.agrega_aristas_vacia()
        self.id_cont+=1


    @Slot( )
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.grafo))

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)