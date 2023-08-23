from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from aeropuerto import Aeropuerto
from vuelo import Vuelo
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):#reserva memoria para mostrar ventana
        super(MainWindow,self).__init__()#constructor para reservar memoria
        #clase hija

        self.aeropuerto = Aeropuerto()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agrega_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

    @Slot( )
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()

        encontrado = False
        for vuelo in self.aeropuerto:
            if id == vuelo.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(vuelo.id)
                origen_widget = QTableWidgetItem(vuelo.origen)
                destino_widget = QTableWidgetItem(vuelo.destino)
                peso_widget = QTableWidgetItem(str(vuelo.peso))

                self.ui.tabla.setItem(0,0,id_widget)
                self.ui.tabla.setItem(0,1,origen_widget)
                self.ui.tabla.setItem(0,2,destino_widget)
                self.ui.tabla.setItem(0,3,peso_widget)

                encontrado = True
                return

        if not encontrado:
            QMessageBox.warning(
            self,
            "Atencion",
            f'El vuelo con el identificador {(id)} no fue encontrado'
        )
        #print("Presion")

    @Slot( )
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(4)
        headers = ["ID","Origen","Destino","Peso"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.aeropuerto))

        row = 0
        for vuelo in self.aeropuerto:
            id_widget = QTableWidgetItem(vuelo.id)
            origen_widget = QTableWidgetItem(vuelo.origen)
            destino_widget = QTableWidgetItem(vuelo.destino)
            peso_widget = QTableWidgetItem(str(vuelo.peso))

            self.ui.tabla.setItem(row,0,id_widget)
            self.ui.tabla.setItem(row,1,origen_widget)
            self.ui.tabla.setItem(row,2,destino_widget)
            self.ui.tabla.setItem(row,3,peso_widget)
            
            row += 1
            #print(vuelo)
        #print("Mostrar Tbla")

    @Slot( )
    def click_agregar(self):
        id = self.ui.id_lineEdit.text()
        origen = self.ui.origen_lineEdit.text()
        destino = self.ui.destino_lineEdit.text()
        peso = self.ui.peso_spinBox.value()

        vuelo = Vuelo(id,origen,destino,peso)
        self.aeropuerto.agrega_final(vuelo)
        #print(id,origen,destino,peso)
        #self.ui.salida.insertPlainText(id + origen + destino + str(peso))

    @Slot( )
    def click_agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen = self.ui.origen_lineEdit.text()
        destino = self.ui.destino_lineEdit.text()
        peso = self.ui.peso_spinBox.value()

        vuelo = Vuelo(id,origen,destino,peso)
        self.aeropuerto.agrega_inicio(vuelo)

    @Slot( )
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.aeropuerto))
        #self.aeropuerto.mostrar()

    @Slot( )
    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.aeropuerto.abrir(ubicacion):
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
        self.aeropuerto.abrir(ubicacion)
        #print("Abrir_Archivo")

    @Slot( )
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.aeropuerto.guardar(ubicacion):
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
        self.aeropuerto.guardar(ubicacion)
        #print("Guardar_Archivo")
    