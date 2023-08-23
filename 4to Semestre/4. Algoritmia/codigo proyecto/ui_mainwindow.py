# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 493)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(2000)

        self.gridLayout.addWidget(self.origen_y_spinBox, 2, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.ingresar_ver_pushButton = QPushButton(self.groupBox)
        self.ingresar_ver_pushButton.setObjectName(u"ingresar_ver_pushButton")

        self.gridLayout.addWidget(self.ingresar_ver_pushButton, 3, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 4, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(2000)

        self.gridLayout.addWidget(self.origen_x_spinBox, 1, 1, 1, 1)

        self.nombre_lineEdit = QLineEdit(self.groupBox)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")

        self.gridLayout.addWidget(self.nombre_lineEdit, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.inicio_pinBox = QSpinBox(self.tab_2)
        self.inicio_pinBox.setObjectName(u"inicio_pinBox")
        self.inicio_pinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.inicio_pinBox, 1, 1, 1, 1)

        self.distancia_doubleSpinBox = QDoubleSpinBox(self.tab_2)
        self.distancia_doubleSpinBox.setObjectName(u"distancia_doubleSpinBox")
        self.distancia_doubleSpinBox.setMaximum(1999.990000000000009)

        self.gridLayout_3.addWidget(self.distancia_doubleSpinBox, 1, 5, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_3.addWidget(self.mostrar_tabla_pushButton, 1, 7, 1, 1)

        self.final_spinBox = QSpinBox(self.tab_2)
        self.final_spinBox.setObjectName(u"final_spinBox")
        self.final_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.final_spinBox, 1, 3, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 1, 2, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_3.addWidget(self.tabla, 0, 0, 1, 8)

        self.agregar_asi_pushButton = QPushButton(self.tab_2)
        self.agregar_asi_pushButton.setObjectName(u"agregar_asi_pushButton")

        self.gridLayout_3.addWidget(self.agregar_asi_pushButton, 1, 6, 1, 1)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 4, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mostrar_grafo_pushButton = QPushButton(self.tab_3)
        self.mostrar_grafo_pushButton.setObjectName(u"mostrar_grafo_pushButton")

        self.gridLayout_5.addWidget(self.mostrar_grafo_pushButton, 1, 0, 1, 1)

        self.dijkstra_pushButton = QPushButton(self.tab_3)
        self.dijkstra_pushButton.setObjectName(u"dijkstra_pushButton")

        self.gridLayout_5.addWidget(self.dijkstra_pushButton, 1, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 791, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Nodos", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Origen y", None))
        self.ingresar_ver_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen x", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"De Nodo:", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"a Nodo:", None))
        self.agregar_asi_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Distancia:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.mostrar_grafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.dijkstra_pushButton.setText(QCoreApplication.translate("MainWindow", u"Aplicar Dijkstra", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

