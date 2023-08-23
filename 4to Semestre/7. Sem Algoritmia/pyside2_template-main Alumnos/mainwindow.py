from PySide2.QtWidgets import QMainWindow, QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
    
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for i in range(0,100):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            color = QColor(r,g,b)
            pen.setColor(color)

            x_origen = randint(0,500)
            x_destino = randint(0,500)
            y_origen = randint(0,500)
            y_destino = randint(0,500)

            self.scene.addEllipse(x_origen,y_origen,6,6,pen)
            self.scene.addEllipse(x_destino,y_destino,6,6,pen)
            self.scene.addLine(x_origen+3,y_origen+3,x_destino+3,y_destino+3,pen)
        #print("Dibujar")
    
    @Slot()
    def limpiar(self):
        self.scene.clear()
        #print("limpiar")
    
    def wheelEvent(self, event):
        #print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)
