# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)
import icons_rc
import logo_rc
import icons_rc
import logo_rc
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 630)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.233, y1:0.176, x2:1, y2:1, stop:0 rgba(255, 35, 79, 255), stop:1 rgba(255, 129, 62, 255))")
        self.actionRegresar = QAction(MainWindow)
        self.actionRegresar.setObjectName(u"actionRegresar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(65, 50, 500, 500))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-color: rgb(22, 27, 32);\n"
"border-radius: 43px;")
        self.logo = QLabel(self.groupBox)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 20, 71, 71))
        self.logo.setPixmap(QPixmap(u":/LogoMain/logo.png"))
        self.logo.setScaledContents(True)
        self.Titulo = QLabel(self.groupBox)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(105, 30, 290, 41))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(35)
        font.setBold(True)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 110, 441, 341))
        self.tabWidget.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.Acceder = QWidget()
        self.Acceder.setObjectName(u"Acceder")
        self.accder_log_pushButton = QPushButton(self.Acceder)
        self.accder_log_pushButton.setObjectName(u"accder_log_pushButton")
        self.accder_log_pushButton.setGeometry(QRect(180, 210, 80, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.accder_log_pushButton.setFont(font1)
        self.accder_log_pushButton.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.usauario_log_lineEdit = QLineEdit(self.Acceder)
        self.usauario_log_lineEdit.setObjectName(u"usauario_log_lineEdit")
        self.usauario_log_lineEdit.setGeometry(QRect(50, 60, 341, 41))
        self.usauario_log_lineEdit.setFont(font1)
        self.usauario_log_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.pw_log_lineEdit = QLineEdit(self.Acceder)
        self.pw_log_lineEdit.setObjectName(u"pw_log_lineEdit")
        self.pw_log_lineEdit.setGeometry(QRect(50, 140, 341, 41))
        self.pw_log_lineEdit.setFont(font1)
        self.pw_log_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.Artistas = QLabel(self.Acceder)
        self.Artistas.setObjectName(u"Artistas")
        self.Artistas.setGeometry(QRect(50, 10, 101, 31))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.Artistas.setFont(font2)
        self.Artistas.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid white;")
        self.tabWidget.addTab(self.Acceder, "")
        self.Registrarse = QWidget()
        self.Registrarse.setObjectName(u"Registrarse")
        self.tabWidget_2 = QTabWidget(self.Registrarse)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 441, 321))
        self.tabWidget_2.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.tabWidget_2.setTabPosition(QTabWidget.West)
        self.tabWidget_2.setTabShape(QTabWidget.Triangular)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(False)
        self.Aficionado = QWidget()
        self.Aficionado.setObjectName(u"Aficionado")
        self.fan_reg_pushButton = QPushButton(self.Aficionado)
        self.fan_reg_pushButton.setObjectName(u"fan_reg_pushButton")
        self.fan_reg_pushButton.setGeometry(QRect(170, 220, 100, 41))
        self.fan_reg_pushButton.setFont(font1)
        self.fan_reg_pushButton.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.nombre_fan_reg_lineEdit = QLineEdit(self.Aficionado)
        self.nombre_fan_reg_lineEdit.setObjectName(u"nombre_fan_reg_lineEdit")
        self.nombre_fan_reg_lineEdit.setGeometry(QRect(50, 40, 341, 41))
        self.nombre_fan_reg_lineEdit.setFont(font1)
        self.nombre_fan_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.pw_fan_reg_lineEdit = QLineEdit(self.Aficionado)
        self.pw_fan_reg_lineEdit.setObjectName(u"pw_fan_reg_lineEdit")
        self.pw_fan_reg_lineEdit.setGeometry(QRect(50, 100, 341, 41))
        self.pw_fan_reg_lineEdit.setFont(font1)
        self.pw_fan_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.pref_fan_reg_lineEdit = QLineEdit(self.Aficionado)
        self.pref_fan_reg_lineEdit.setObjectName(u"pref_fan_reg_lineEdit")
        self.pref_fan_reg_lineEdit.setGeometry(QRect(50, 160, 341, 41))
        self.pref_fan_reg_lineEdit.setFont(font1)
        self.pref_fan_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.Titulo1 = QLabel(self.Aficionado)
        self.Titulo1.setObjectName(u"Titulo1")
        self.Titulo1.setGeometry(QRect(50, 3, 251, 31))
        self.Titulo1.setFont(font2)
        self.Titulo1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid white;")
        self.tabWidget_2.addTab(self.Aficionado, "")
        self.Artista = QWidget()
        self.Artista.setObjectName(u"Artista")
        self.scrollArea = QScrollArea(self.Artista)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, -7, 421, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 402, 478))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 460))
        self.groupBox_2.setStyleSheet(u"border: 0px solid white;")
        self.area_art_reg_lineEdit = QLineEdit(self.groupBox_2)
        self.area_art_reg_lineEdit.setObjectName(u"area_art_reg_lineEdit")
        self.area_art_reg_lineEdit.setGeometry(QRect(40, 97, 341, 41))
        self.area_art_reg_lineEdit.setFont(font1)
        self.area_art_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.art_reg_pushButton = QPushButton(self.groupBox_2)
        self.art_reg_pushButton.setObjectName(u"art_reg_pushButton")
        self.art_reg_pushButton.setGeometry(QRect(160, 400, 100, 41))
        self.art_reg_pushButton.setFont(font1)
        self.art_reg_pushButton.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.nombre_art_reg_lineEdit = QLineEdit(self.groupBox_2)
        self.nombre_art_reg_lineEdit.setObjectName(u"nombre_art_reg_lineEdit")
        self.nombre_art_reg_lineEdit.setGeometry(QRect(40, 37, 341, 41))
        self.nombre_art_reg_lineEdit.setFont(font1)
        self.nombre_art_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.genero_art_reg_lineEdit = QLineEdit(self.groupBox_2)
        self.genero_art_reg_lineEdit.setObjectName(u"genero_art_reg_lineEdit")
        self.genero_art_reg_lineEdit.setGeometry(QRect(40, 157, 341, 41))
        self.genero_art_reg_lineEdit.setFont(font1)
        self.genero_art_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.ubi_art_reg_lineEdit = QLineEdit(self.groupBox_2)
        self.ubi_art_reg_lineEdit.setObjectName(u"ubi_art_reg_lineEdit")
        self.ubi_art_reg_lineEdit.setGeometry(QRect(40, 220, 341, 41))
        self.ubi_art_reg_lineEdit.setFont(font1)
        self.ubi_art_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.pw_art_reg_lineEdit = QLineEdit(self.groupBox_2)
        self.pw_art_reg_lineEdit.setObjectName(u"pw_art_reg_lineEdit")
        self.pw_art_reg_lineEdit.setGeometry(QRect(40, 340, 341, 41))
        self.pw_art_reg_lineEdit.setFont(font1)
        self.pw_art_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.usuario_art_reg_lineEdit = QLineEdit(self.groupBox_2)
        self.usuario_art_reg_lineEdit.setObjectName(u"usuario_art_reg_lineEdit")
        self.usuario_art_reg_lineEdit.setGeometry(QRect(40, 280, 341, 41))
        self.usuario_art_reg_lineEdit.setFont(font1)
        self.usuario_art_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.Titulo2 = QLabel(self.groupBox_2)
        self.Titulo2.setObjectName(u"Titulo2")
        self.Titulo2.setGeometry(QRect(40, 0, 211, 31))
        self.Titulo2.setFont(font2)
        self.Titulo2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid white;")

        self.verticalLayout.addWidget(self.groupBox_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget_2.addTab(self.Artista, "")
        self.Negocio = QWidget()
        self.Negocio.setObjectName(u"Negocio")
        self.scrollArea_2 = QScrollArea(self.Negocio)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, -7, 421, 331))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 402, 478))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 460))
        self.groupBox_3.setStyleSheet(u"border: 0px solid white;")
        self.nomEnc_neg_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.nomEnc_neg_reg_lineEdit.setObjectName(u"nomEnc_neg_reg_lineEdit")
        self.nomEnc_neg_reg_lineEdit.setGeometry(QRect(40, 97, 341, 41))
        self.nomEnc_neg_reg_lineEdit.setFont(font1)
        self.nomEnc_neg_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.neg_reg_pushButton = QPushButton(self.groupBox_3)
        self.neg_reg_pushButton.setObjectName(u"neg_reg_pushButton")
        self.neg_reg_pushButton.setGeometry(QRect(160, 400, 100, 41))
        self.neg_reg_pushButton.setFont(font1)
        self.neg_reg_pushButton.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.nomNeg_neg_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.nomNeg_neg_reg_lineEdit.setObjectName(u"nomNeg_neg_reg_lineEdit")
        self.nomNeg_neg_reg_lineEdit.setGeometry(QRect(40, 37, 341, 41))
        self.nomNeg_neg_reg_lineEdit.setFont(font1)
        self.nomNeg_neg_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.pw_neg_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.pw_neg_reg_lineEdit.setObjectName(u"pw_neg_reg_lineEdit")
        self.pw_neg_reg_lineEdit.setGeometry(QRect(40, 157, 341, 41))
        self.pw_neg_reg_lineEdit.setFont(font1)
        self.pw_neg_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.contacto_neg_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.contacto_neg_reg_lineEdit.setObjectName(u"contacto_neg_reg_lineEdit")
        self.contacto_neg_reg_lineEdit.setGeometry(QRect(40, 220, 341, 41))
        self.contacto_neg_reg_lineEdit.setFont(font1)
        self.contacto_neg_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.dir_neg_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.dir_neg_reg_lineEdit.setObjectName(u"dir_neg_reg_lineEdit")
        self.dir_neg_reg_lineEdit.setGeometry(QRect(40, 340, 341, 41))
        self.dir_neg_reg_lineEdit.setFont(font1)
        self.dir_neg_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.pref_neg_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.pref_neg_reg_lineEdit.setObjectName(u"pref_neg_reg_lineEdit")
        self.pref_neg_reg_lineEdit.setGeometry(QRect(40, 280, 341, 41))
        self.pref_neg_reg_lineEdit.setFont(font1)
        self.pref_neg_reg_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.Titulo2_2 = QLabel(self.groupBox_3)
        self.Titulo2_2.setObjectName(u"Titulo2_2")
        self.Titulo2_2.setGeometry(QRect(40, 0, 211, 31))
        self.Titulo2_2.setFont(font2)
        self.Titulo2_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid white;")

        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget_2.addTab(self.Negocio, "")
        self.tabWidget.addTab(self.Registrarse, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 630, 22))
        self.menuCancelar = QMenu(self.menubar)
        self.menuCancelar.setObjectName(u"menuCancelar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCancelar.menuAction())
        self.menuCancelar.addAction(self.actionRegresar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRegresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.groupBox.setTitle("")
        self.logo.setText("")
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"MESSENGERS", None))
        self.accder_log_pushButton.setText(QCoreApplication.translate("MainWindow", u"Acceder", None))
        self.usauario_log_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Nombre de usuario", None))
        self.pw_log_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Contase\u00f1a", None))
        self.Artistas.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Acceder), QCoreApplication.translate("MainWindow", u"Acceder", None))
        self.fan_reg_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.nombre_fan_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Nombre de usuario", None))
        self.pw_fan_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Contase\u00f1a", None))
        self.pref_fan_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Preferencia en", None))
        self.Titulo1.setText(QCoreApplication.translate("MainWindow", u"Registro Aficionados", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Aficionado), QCoreApplication.translate("MainWindow", u"Aficionado", None))
        self.groupBox_2.setTitle("")
        self.area_art_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Area del arte", None))
        self.art_reg_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.nombre_art_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Nombre de Artista", None))
        self.genero_art_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Genero perteneciente", None))
        self.ubi_art_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Estado de recidencia", None))
        self.pw_art_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Contrase\u00f1a", None))
        self.usuario_art_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Nombre de usuario", None))
        self.Titulo2.setText(QCoreApplication.translate("MainWindow", u"Registro Artista", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Artista), QCoreApplication.translate("MainWindow", u"Artista", None))
        self.groupBox_3.setTitle("")
        self.nomEnc_neg_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Nombre del Encargado (Usuario)", None))
        self.neg_reg_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.nomNeg_neg_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Nombre del Negocio", None))
        self.pw_neg_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Contrase\u00f1a", None))
        self.contacto_neg_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Contacto", None))
        self.dir_neg_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Direccion", None))
        self.pref_neg_reg_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Interesado en", None))
        self.Titulo2_2.setText(QCoreApplication.translate("MainWindow", u"Registro Negocio", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Negocio), QCoreApplication.translate("MainWindow", u"Negocio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Registrarse), QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.menuCancelar.setTitle(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

