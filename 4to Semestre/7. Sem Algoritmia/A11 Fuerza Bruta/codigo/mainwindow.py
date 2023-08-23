from PySide2.QtWidgets import QMainWindow, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor
from admin import Admin
from particula import Particula
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from random import randint
from algoritmos import puntos_mas_cercanos

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.admin = Admin()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)

        self.ui.ingresar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.ingresar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.mostrar_grafo_pushButton.clicked.connect(self.mostrar_grafo)

        self.ui.ordenar_id_pushButton.clicked.connect(self.ordena_id)
        self.ui.ordenar_dis_pushButton.clicked.connect(self.ordena_dis)
        self.ui.ordena_vel_pushButton.clicked.connect(self.ordena_vel)

        self.ui.mostrar_puntos_action.triggered.connect(self.mostrar_puntos)
        self.ui.fuerza_bruta_accion.triggered.connect(self.fuerza_bruta)

    @Slot( )
    def mostrar_puntos(self):
        self.scene.clear()
        pen = QPen()
        pen.setWidth(2)
        for particula in self.admin.particulas: 
            color = QColor(particula.red,particula.green,particula.blue)
            pen.setColor(color)
            x1 = particula.origen_x
            y1 = particula.origen_y
            x2 = particula.destino_x
            y2 = particula.destino_y
            self.scene.addEllipse(x1-1.5,y1-1.5,3,3,pen)
            self.scene.addEllipse(x2-1.5,y2-1.5,3,3,pen)
    @Slot( )
    def fuerza_bruta(self):
        puntos = []
        for particula in self.admin.particulas:
            x1 = particula.origen_x
            y1 = particula.origen_y
            x2 = particula.destino_x
            y2 = particula.destino_y
            punto1 = (x1,y1)
            puntos.append(punto1)
            punto2 = (x2,y2) 
            puntos.append(punto2)
        resultado = puntos_mas_cercanos(puntos)
        print(resultado)
        for punto1, punto2 in resultado:
            x1 =punto1[0]
            y1 =punto1[1]
            x2 =punto2[0]
            y2 =punto2[1]
            self.scene.addLine(x1,y1,x2,y2)

    @Slot( )
    def ordena_id(self):
        self.admin.particulas.sort(key = lambda particula: particula.id)
    @Slot( )
    def ordena_dis(self):
        self.admin.particulas.sort(key = lambda particula: particula.distancia,reverse=True)
    @Slot( )
    def ordena_vel(self):
        self.admin.particulas.sort(key = lambda particula: particula.velocidad)

    @Slot( )
    def mostrar_grafo(self):
        self.scene.clear()
        pen = QPen()
        pen.setWidth(2)
        for particula in self.admin.particulas:
            color = QColor(particula.red,particula.green,particula.blue)
            pen.setColor(color)
            x1 = particula.origen_x
            y1 = particula.origen_y
            x2 = particula.destino_x
            y2 = particula.destino_y
            self.scene.addEllipse(x1-1.5,y1-1.5,3,3,pen)
            self.scene.addEllipse(x2-1.5,y2-1.5,3,3,pen)
            self.scene.addLine(x1,y1,x2,y2,pen)
            

    @Slot( )
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()

        encontrado = False
        for particula in self.admin:
            if int(id) == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origen_widget = QTableWidgetItem(str(particula.origen))
                destino_widget = QTableWidgetItem(str(particula.destino))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                color_widget = QTableWidgetItem(str(particula.color))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0,0,id_widget)
                self.ui.tabla.setItem(0,1,origen_widget)
                self.ui.tabla.setItem(0,2,destino_widget)
                self.ui.tabla.setItem(0,3,velocidad_widget)
                self.ui.tabla.setItem(0,4,color_widget)
                self.ui.tabla.setItem(0,5,distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
            self,
            "Atencion",
            f'La particula con el identificador {(id)} no fue encontrado'
        )

    @Slot( )
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(6)
        headers = ["ID","Origen","Destino ","Velocidad","Color","Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.admin))
        row = 0
        for particula in self.admin:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_widget = QTableWidgetItem(particula.origen)
            destino_widget = QTableWidgetItem(particula.destino)
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            color_widget = QTableWidgetItem(particula.color)
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row,0,id_widget)
            self.ui.tabla.setItem(row,1,origen_widget)
            self.ui.tabla.setItem(row,2,destino_widget)
            self.ui.tabla.setItem(row,3,velocidad_widget)
            self.ui.tabla.setItem(row,4,color_widget)
            self.ui.tabla.setItem(row,5,distancia_widget)
            row += 1
    
    @Slot( )
    def click_agregar(self):
        origen = dict()
        destino = dict()
        color = dict()

        id = self.ui.id_spinBox.value()
        origen["x"] = self.ui.origen_x_spinBox.value()
        origen["y"] = self.ui.origen_y_spinBox.value()
        destino["x"]  = self.ui.destino_x_spinBox.value()
        destino["y"] = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        color["red"] = randint(0,255)
        color["green"] = randint(0,255)
        color["blue"] = randint(0,255)

        particula = Particula(id,origen,destino,velocidad,color)
        self.admin.agrega_final(particula)

    @Slot( )
    def click_agregar_inicio(self):
        origen = dict()
        destino = dict()
        color = dict()

        id = self.ui.id_spinBox.value()
        origen["x"] = self.ui.origen_x_spinBox.value()
        origen["y"] = self.ui.origen_y_spinBox.value()
        destino["x"]  = self.ui.destino_x_spinBox.value()
        destino["y"] = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        color["red"] = randint(0,255)
        color["green"] = randint(0,255)
        color["blue"] = randint(0,255)

        particula = Particula(id,origen,destino,velocidad,color)
        self.admin.agrega_inicio(particula)

    @Slot( )
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.admin))
    
    @Slot( )
    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.admin.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo abrir el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo abrir el archivo " + ubicacion
            )
        self.admin.abrir(ubicacion)
    @Slot( )
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.admin.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )
        self.admin.guardar(ubicacion)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)