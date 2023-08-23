# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfileWindow.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import logo_rc
import icons_rc
import icons_rc
import logo_rc

class Ui_ProfileWindow(object):
    def setupUi(self, ProfileWindow):
        if not ProfileWindow.objectName():
            ProfileWindow.setObjectName(u"ProfileWindow")
        ProfileWindow.resize(1700, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProfileWindow.sizePolicy().hasHeightForWidth())
        ProfileWindow.setSizePolicy(sizePolicy)
        ProfileWindow.setMinimumSize(QSize(1700, 900))
        ProfileWindow.setMaximumSize(QSize(1700, 900))
        ProfileWindow.setBaseSize(QSize(0, 0))
        ProfileWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.233, y1:0.176, x2:1, y2:1, stop:0 rgba(255, 35, 79, 255), stop:1 rgba(255, 129, 62, 255))")
        self.actionRegresar_al_inicio = QAction(ProfileWindow)
        self.actionRegresar_al_inicio.setObjectName(u"actionRegresar_al_inicio")
        self.centralwidget = QWidget(ProfileWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/*VERTICAL BAR*/\n"
"QScrollBar:vertical {\n"
"            border: none;\n"
"            width:10px;    \n"
"            margin: 10px 0px 10px 0px;\n"
"			border-radius: 4px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"            min-height: 0px;\n"
"          	border: none;\n"
"			border-radius: 4px;\n"
"			background-color: rgb(49, 60, 72);\n"
"        }\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 35, 79);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(255, 35, 79);\n"
"}\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"/*HORIZONTAL BAR*/\n"
"QScrollBar:horizontal {\n"
"            border: none;\n"
"            margin: 0px"
                        " 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:horizontal {         \n"
"            min-height: 0px;\n"
"          	border: none;\n"
"			border-radius: 4px;\n"
"			background-color: rgb(49, 60, 72);\n"
"        }\n"
"QScrollBar::handle:horizontal:hover{	\n"
"	background-color: rgb(255, 35, 79);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: rgb(255, 35, 79);\n"
"}\n"
"        QScrollBar::add-line:horizontal {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:horizontal {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(100, 70, 1481, 751))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-color: rgb(22, 27, 32);\n"
"border-radius: 43px;")
        self.logo = QLabel(self.groupBox)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 20, 91, 91))
        self.logo.setPixmap(QPixmap(u":/LogoMain/logo.png"))
        self.logo.setScaledContents(True)
        self.star_pushButton = QPushButton(self.groupBox)
        self.star_pushButton.setObjectName(u"star_pushButton")
        self.star_pushButton.setGeometry(QRect(40, 250, 51, 51))
        self.star_pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/buttons/star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.star_pushButton.setIcon(icon)
        self.star_pushButton.setIconSize(QSize(34, 50))
        self.home_pushButton = QPushButton(self.groupBox)
        self.home_pushButton.setObjectName(u"home_pushButton")
        self.home_pushButton.setGeometry(QRect(40, 150, 51, 51))
        self.home_pushButton.setStyleSheet(u"qproperty-icon: url(:/buttons/home.png);\n"
"background-color: rgba(0,0,0,0%)")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_pushButton.setIcon(icon1)
        self.home_pushButton.setIconSize(QSize(37, 50))
        self.heart_pushButton = QPushButton(self.groupBox)
        self.heart_pushButton.setObjectName(u"heart_pushButton")
        self.heart_pushButton.setGeometry(QRect(40, 350, 51, 51))
        self.heart_pushButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/heart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.heart_pushButton.setIcon(icon2)
        self.heart_pushButton.setIconSize(QSize(33, 35))
        self.message_pushButton = QPushButton(self.groupBox)
        self.message_pushButton.setObjectName(u"message_pushButton")
        self.message_pushButton.setGeometry(QRect(40, 450, 51, 51))
        self.message_pushButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/buttons/message.png", QSize(), QIcon.Normal, QIcon.Off)
        self.message_pushButton.setIcon(icon3)
        self.message_pushButton.setIconSize(QSize(35, 50))
        self.bell_pushButton = QPushButton(self.groupBox)
        self.bell_pushButton.setObjectName(u"bell_pushButton")
        self.bell_pushButton.setGeometry(QRect(40, 550, 51, 51))
        self.bell_pushButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/buttons/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bell_pushButton.setIcon(icon4)
        self.bell_pushButton.setIconSize(QSize(35, 50))
        self.person_pushButton = QPushButton(self.groupBox)
        self.person_pushButton.setObjectName(u"person_pushButton")
        self.person_pushButton.setGeometry(QRect(40, 650, 51, 51))
        self.person_pushButton.setStyleSheet(u"background-color: rgba(0,0,0,0%)")
        icon5 = QIcon()
        icon5.addFile(u":/buttons/person.png", QSize(), QIcon.Normal, QIcon.Off)
        self.person_pushButton.setIcon(icon5)
        self.person_pushButton.setIconSize(QSize(40, 50))
        self.main_scrollArea = QScrollArea(self.groupBox)
        self.main_scrollArea.setObjectName(u"main_scrollArea")
        self.main_scrollArea.setGeometry(QRect(120, 30, 921, 691))
        self.main_scrollArea.setMinimumSize(QSize(0, 691))
        self.main_scrollArea.setMaximumSize(QSize(1321, 691))
        self.main_scrollArea.setAutoFillBackground(False)
        self.main_scrollArea.setStyleSheet(u"")
        self.main_scrollArea.setFrameShape(QFrame.NoFrame)
        self.main_scrollArea.setFrameShadow(QFrame.Sunken)
        self.main_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.main_scrollArea.setWidgetResizable(True)
        self.main_scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.profile_scrollAreaWidgetContents = QWidget()
        self.profile_scrollAreaWidgetContents.setObjectName(u"profile_scrollAreaWidgetContents")
        self.profile_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 911, 898))
        font = QFont()
        font.setPointSize(13)
        self.profile_scrollAreaWidgetContents.setFont(font)
        self.profile_scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.profile_scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.profile_groupBox = QGroupBox(self.profile_scrollAreaWidgetContents)
        self.profile_groupBox.setObjectName(u"profile_groupBox")
        self.profile_groupBox.setMinimumSize(QSize(0, 880))
        self.profile_groupBox.setStyleSheet(u"background-color: rgb(31, 38, 46);\n"
"border-color: rgb(22, 27, 32);\n"
"border-radius: 43px;")
        self.buscar_lineEdit = QLineEdit(self.profile_groupBox)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")
        self.buscar_lineEdit.setGeometry(QRect(480, 20, 341, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.buscar_lineEdit.setFont(font1)
        self.buscar_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Titulo = QLabel(self.profile_groupBox)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(70, 10, 291, 41))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(35)
        font2.setBold(True)
        self.Titulo.setFont(font2)
        self.Titulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.buscar_pushButton = QPushButton(self.profile_groupBox)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")
        self.buscar_pushButton.setGeometry(QRect(400, 20, 75, 41))
        self.buscar_pushButton.setFont(font1)
        self.buscar_pushButton.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.top_imegen_label = QLabel(self.profile_groupBox)
        self.top_imegen_label.setObjectName(u"top_imegen_label")
        self.top_imegen_label.setGeometry(QRect(0, 0, 891, 261))
        self.top_imegen_label.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid white;")
        self.top_imegen_label.setOpenExternalLinks(True)
        self.publicaciones_scrollArea = QScrollArea(self.profile_groupBox)
        self.publicaciones_scrollArea.setObjectName(u"publicaciones_scrollArea")
        self.publicaciones_scrollArea.setGeometry(QRect(30, 330, 841, 511))
        self.publicaciones_scrollArea.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid white;\n"
"")
        self.publicaciones_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 829, 1068))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.publicaciones_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.publicaciones_groupBox.setObjectName(u"publicaciones_groupBox")
        self.publicaciones_groupBox.setMinimumSize(QSize(0, 1050))
        self.publicaciones_groupBox.setStyleSheet(u"border-radius: 0px;\n"
"border: 0px solid white;\n"
"")
        self.publicaciones_more_pushButton = QPushButton(self.publicaciones_groupBox)
        self.publicaciones_more_pushButton.setObjectName(u"publicaciones_more_pushButton")
        self.publicaciones_more_pushButton.setGeometry(QRect(380, 990, 51, 51))
        icon6 = QIcon()
        icon6.addFile(u":/buttons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.publicaciones_more_pushButton.setIcon(icon6)
        self.publicaciones_more_pushButton.setIconSize(QSize(50, 50))
        self.publicacion1 = QGroupBox(self.publicaciones_groupBox)
        self.publicacion1.setObjectName(u"publicacion1")
        self.publicacion1.setGeometry(QRect(10, 9, 790, 161))
        self.publicacion1.setStyleSheet(u"border-radius: 43px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);")
        self.ImagenP1 = QLabel(self.publicacion1)
        self.ImagenP1.setObjectName(u"ImagenP1")
        self.ImagenP1.setGeometry(QRect(30, 10, 221, 141))
        self.ImagenP1.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid black;")
        self.tituloP1 = QLabel(self.publicacion1)
        self.tituloP1.setObjectName(u"tituloP1")
        self.tituloP1.setGeometry(QRect(270, 20, 471, 31))
        font3 = QFont()
        font3.setPointSize(18)
        self.tituloP1.setFont(font3)
        self.descrP1 = QLabel(self.publicacion1)
        self.descrP1.setObjectName(u"descrP1")
        self.descrP1.setGeometry(QRect(280, 60, 461, 81))
        font4 = QFont()
        font4.setPointSize(12)
        self.descrP1.setFont(font4)
        self.descrP1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP1 = QPushButton(self.publicacion1)
        self.up_pushButtonP1.setObjectName(u"up_pushButtonP1")
        self.up_pushButtonP1.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP1.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        icon7 = QIcon()
        icon7.addFile(u":/buttons/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.up_pushButtonP1.setIcon(icon7)
        self.up_pushButtonP1.setIconSize(QSize(35, 50))
        self.publicacion2 = QGroupBox(self.publicaciones_groupBox)
        self.publicacion2.setObjectName(u"publicacion2")
        self.publicacion2.setGeometry(QRect(10, 210, 790, 161))
        self.publicacion2.setStyleSheet(u"border-radius: 43px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);")
        self.ImagenP2 = QLabel(self.publicacion2)
        self.ImagenP2.setObjectName(u"ImagenP2")
        self.ImagenP2.setGeometry(QRect(30, 10, 221, 141))
        self.ImagenP2.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid black;")
        self.tituloP2 = QLabel(self.publicacion2)
        self.tituloP2.setObjectName(u"tituloP2")
        self.tituloP2.setGeometry(QRect(270, 20, 470, 31))
        self.tituloP2.setFont(font3)
        self.descrP2 = QLabel(self.publicacion2)
        self.descrP2.setObjectName(u"descrP2")
        self.descrP2.setGeometry(QRect(280, 60, 460, 81))
        self.descrP2.setFont(font4)
        self.descrP2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP2 = QPushButton(self.publicacion2)
        self.up_pushButtonP2.setObjectName(u"up_pushButtonP2")
        self.up_pushButtonP2.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP2.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        self.up_pushButtonP2.setIcon(icon7)
        self.up_pushButtonP2.setIconSize(QSize(35, 50))
        self.publicacion3 = QGroupBox(self.publicaciones_groupBox)
        self.publicacion3.setObjectName(u"publicacion3")
        self.publicacion3.setGeometry(QRect(10, 410, 790, 161))
        self.publicacion3.setStyleSheet(u"border-radius: 43px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);")
        self.ImagenP3 = QLabel(self.publicacion3)
        self.ImagenP3.setObjectName(u"ImagenP3")
        self.ImagenP3.setGeometry(QRect(30, 10, 221, 141))
        self.ImagenP3.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid black;")
        self.tituloP3 = QLabel(self.publicacion3)
        self.tituloP3.setObjectName(u"tituloP3")
        self.tituloP3.setGeometry(QRect(270, 20, 471, 31))
        self.tituloP3.setFont(font3)
        self.descrP3 = QLabel(self.publicacion3)
        self.descrP3.setObjectName(u"descrP3")
        self.descrP3.setGeometry(QRect(280, 60, 461, 81))
        self.descrP3.setFont(font4)
        self.descrP3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP3 = QPushButton(self.publicacion3)
        self.up_pushButtonP3.setObjectName(u"up_pushButtonP3")
        self.up_pushButtonP3.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP3.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        self.up_pushButtonP3.setIcon(icon7)
        self.up_pushButtonP3.setIconSize(QSize(35, 50))
        self.publicacion4 = QGroupBox(self.publicaciones_groupBox)
        self.publicacion4.setObjectName(u"publicacion4")
        self.publicacion4.setGeometry(QRect(10, 610, 790, 161))
        self.publicacion4.setStyleSheet(u"border-radius: 43px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);")
        self.ImagenP4 = QLabel(self.publicacion4)
        self.ImagenP4.setObjectName(u"ImagenP4")
        self.ImagenP4.setGeometry(QRect(30, 10, 221, 141))
        self.ImagenP4.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid black;")
        self.tituloP4 = QLabel(self.publicacion4)
        self.tituloP4.setObjectName(u"tituloP4")
        self.tituloP4.setGeometry(QRect(270, 20, 471, 31))
        self.tituloP4.setFont(font3)
        self.descrP4 = QLabel(self.publicacion4)
        self.descrP4.setObjectName(u"descrP4")
        self.descrP4.setGeometry(QRect(280, 60, 461, 81))
        self.descrP4.setFont(font4)
        self.descrP4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP4 = QPushButton(self.publicacion4)
        self.up_pushButtonP4.setObjectName(u"up_pushButtonP4")
        self.up_pushButtonP4.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP4.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        self.up_pushButtonP4.setIcon(icon7)
        self.up_pushButtonP4.setIconSize(QSize(35, 50))
        self.publicacion5 = QGroupBox(self.publicaciones_groupBox)
        self.publicacion5.setObjectName(u"publicacion5")
        self.publicacion5.setGeometry(QRect(10, 810, 790, 161))
        self.publicacion5.setStyleSheet(u"border-radius: 43px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);")
        self.ImagenP5 = QLabel(self.publicacion5)
        self.ImagenP5.setObjectName(u"ImagenP5")
        self.ImagenP5.setGeometry(QRect(30, 10, 221, 141))
        self.ImagenP5.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid black;")
        self.tituloP5 = QLabel(self.publicacion5)
        self.tituloP5.setObjectName(u"tituloP5")
        self.tituloP5.setGeometry(QRect(270, 20, 471, 31))
        self.tituloP5.setFont(font3)
        self.descrP5 = QLabel(self.publicacion5)
        self.descrP5.setObjectName(u"descrP5")
        self.descrP5.setGeometry(QRect(280, 60, 461, 81))
        self.descrP5.setFont(font4)
        self.descrP5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP5 = QPushButton(self.publicacion5)
        self.up_pushButtonP5.setObjectName(u"up_pushButtonP5")
        self.up_pushButtonP5.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP5.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        self.up_pushButtonP5.setIcon(icon7)
        self.up_pushButtonP5.setIconSize(QSize(35, 50))

        self.verticalLayout_2.addWidget(self.publicaciones_groupBox)

        self.publicaciones_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Publicaciones = QLabel(self.profile_groupBox)
        self.Publicaciones.setObjectName(u"Publicaciones")
        self.Publicaciones.setGeometry(QRect(30, 280, 161, 31))
        font5 = QFont()
        font5.setPointSize(18)
        font5.setBold(True)
        self.Publicaciones.setFont(font5)
        self.Publicaciones.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.top_imegen_label.raise_()
        self.buscar_lineEdit.raise_()
        self.Titulo.raise_()
        self.buscar_pushButton.raise_()
        self.publicaciones_scrollArea.raise_()
        self.Publicaciones.raise_()

        self.verticalLayout.addWidget(self.profile_groupBox)

        self.main_scrollArea.setWidget(self.profile_scrollAreaWidgetContents)
        self.marca = QLabel(self.groupBox)
        self.marca.setObjectName(u"marca")
        self.marca.setGeometry(QRect(40, 650, 51, 51))
        self.marca.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.233, y1:0.176, x2:1, y2:1, stop:0 rgba(255, 35, 79, 40%), stop:1 rgba(255, 129, 62, 40%));\n"
"border-radius: 43px;")
        self.details_scrollArea = QScrollArea(self.groupBox)
        self.details_scrollArea.setObjectName(u"details_scrollArea")
        self.details_scrollArea.setGeometry(QRect(1039, 29, 401, 691))
        self.details_scrollArea.setStyleSheet(u"\n"
"border-radius: 43px;\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid white;")
        self.details_scrollArea.setWidgetResizable(True)
        self.details_scrollAreaWidgetContents = QWidget()
        self.details_scrollAreaWidgetContents.setObjectName(u"details_scrollAreaWidgetContents")
        self.details_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 391, 998))
        self.details_scrollAreaWidgetContents.setStyleSheet(u"border-radius:0px;\n"
"border-top: 0px solid white;\n"
"border-bottom: 0px solid white;")
        self.horizontalLayout = QHBoxLayout(self.details_scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.details_groupBox = QGroupBox(self.details_scrollAreaWidgetContents)
        self.details_groupBox.setObjectName(u"details_groupBox")
        self.details_groupBox.setMinimumSize(QSize(0, 980))
        self.details_groupBox.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-color: rgb(22, 27, 32);\n"
"border-radius: 43px;\n"
"border: 1px solid white;\n"
"")
        self.perfil_imagen_label = QLabel(self.details_groupBox)
        self.perfil_imagen_label.setObjectName(u"perfil_imagen_label")
        self.perfil_imagen_label.setGeometry(QRect(20, 20, 171, 171))
        self.perfil_imagen_label.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid white;")
        self.info_label = QLabel(self.details_groupBox)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(210, 40, 131, 91))
        self.info_label.setFont(font5)
        self.info_label.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.point = QLabel(self.details_groupBox)
        self.point.setObjectName(u"point")
        self.point.setGeometry(QRect(210, 150, 16, 21))
        self.point.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"")
        self.point.setPixmap(QPixmap(u":/buttons/point.png"))
        self.point.setScaledContents(True)
        self.ubicacion_label = QLabel(self.details_groupBox)
        self.ubicacion_label.setObjectName(u"ubicacion_label")
        self.ubicacion_label.setGeometry(QRect(230, 150, 111, 21))
        self.ubicacion_label.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"color: rgb(255, 255, 255);")
        self.line = QFrame(self.details_groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 320, 330, 1))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Seguidores = QLabel(self.details_groupBox)
        self.Seguidores.setObjectName(u"Seguidores")
        self.Seguidores.setGeometry(QRect(60, 280, 91, 21))
        self.Seguidores.setFont(font1)
        self.Seguidores.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"color: rgb(255, 255, 255);")
        self.seguidores_label = QLabel(self.details_groupBox)
        self.seguidores_label.setObjectName(u"seguidores_label")
        self.seguidores_label.setGeometry(QRect(30, 220, 151, 61))
        font6 = QFont()
        font6.setPointSize(26)
        font6.setBold(True)
        self.seguidores_label.setFont(font6)
        self.seguidores_label.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.seguidores_label.setAlignment(Qt.AlignCenter)
        self.seguir_pushButton = QPushButton(self.details_groupBox)
        self.seguir_pushButton.setObjectName(u"seguir_pushButton")
        self.seguir_pushButton.setGeometry(QRect(220, 240, 111, 41))
        self.seguir_pushButton.setFont(font1)
        self.seguir_pushButton.setStyleSheet(u"border-radius: 20px;\n"
"border: 0px solid white;\n"
"color: rgb(255, 255, 255);\n"
"background-color: \n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:0.756, y2:0.795455, stop:0 rgba(255, 35, 79, 255), stop:0.994318 rgba(255, 122, 63, 255))\n"
"\n"
"")
        self.Portafolio = QLabel(self.details_groupBox)
        self.Portafolio.setObjectName(u"Portafolio")
        self.Portafolio.setGeometry(QRect(20, 340, 91, 21))
        self.Portafolio.setFont(font1)
        self.Portafolio.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"color: rgb(255, 255, 255);")
        self.Tabajo1 = QGroupBox(self.details_groupBox)
        self.Tabajo1.setObjectName(u"Tabajo1")
        self.Tabajo1.setGeometry(QRect(20, 380, 341, 111))
        self.Tabajo1.setStyleSheet(u"border-radius: 43px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);")
        self.imagenT1 = QLabel(self.Tabajo1)
        self.imagenT1.setObjectName(u"imagenT1")
        self.imagenT1.setGeometry(QRect(30, 10, 91, 91))
        self.imagenT1.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid black;")
        self.descrpcionT1 = QLabel(self.Tabajo1)
        self.descrpcionT1.setObjectName(u"descrpcionT1")
        self.descrpcionT1.setGeometry(QRect(140, 10, 171, 61))
        self.descrpcionT1.setFont(font4)
        self.point_2 = QLabel(self.Tabajo1)
        self.point_2.setObjectName(u"point_2")
        self.point_2.setGeometry(QRect(140, 80, 16, 21))
        self.point_2.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"")
        self.point_2.setPixmap(QPixmap(u":/buttons/point.png"))
        self.point_2.setScaledContents(True)
        self.ubicacionT1 = QLabel(self.Tabajo1)
        self.ubicacionT1.setObjectName(u"ubicacionT1")
        self.ubicacionT1.setGeometry(QRect(170, 80, 141, 20))
        self.Tabajo2 = QGroupBox(self.details_groupBox)
        self.Tabajo2.setObjectName(u"Tabajo2")
        self.Tabajo2.setGeometry(QRect(20, 510, 341, 111))
        self.Tabajo2.setStyleSheet(u"border-radius: 43px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);")
        self.imagenT2 = QLabel(self.Tabajo2)
        self.imagenT2.setObjectName(u"imagenT2")
        self.imagenT2.setGeometry(QRect(30, 10, 91, 91))
        self.imagenT2.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid black;")
        self.descrpcionT2 = QLabel(self.Tabajo2)
        self.descrpcionT2.setObjectName(u"descrpcionT2")
        self.descrpcionT2.setGeometry(QRect(140, 10, 171, 61))
        self.descrpcionT2.setFont(font4)
        self.point_3 = QLabel(self.Tabajo2)
        self.point_3.setObjectName(u"point_3")
        self.point_3.setGeometry(QRect(140, 80, 16, 21))
        self.point_3.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"")
        self.point_3.setPixmap(QPixmap(u":/buttons/point.png"))
        self.point_3.setScaledContents(True)
        self.ubicacionT2 = QLabel(self.Tabajo2)
        self.ubicacionT2.setObjectName(u"ubicacionT2")
        self.ubicacionT2.setGeometry(QRect(170, 80, 141, 20))
        self.Tabajo3 = QGroupBox(self.details_groupBox)
        self.Tabajo3.setObjectName(u"Tabajo3")
        self.Tabajo3.setGeometry(QRect(20, 640, 341, 111))
        self.Tabajo3.setStyleSheet(u"border-radius: 43px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);")
        self.imagenT3 = QLabel(self.Tabajo3)
        self.imagenT3.setObjectName(u"imagenT3")
        self.imagenT3.setGeometry(QRect(30, 10, 91, 91))
        self.imagenT3.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid black;")
        self.descrpcionT3 = QLabel(self.Tabajo3)
        self.descrpcionT3.setObjectName(u"descrpcionT3")
        self.descrpcionT3.setGeometry(QRect(140, 10, 171, 61))
        self.descrpcionT3.setFont(font4)
        self.point_4 = QLabel(self.Tabajo3)
        self.point_4.setObjectName(u"point_4")
        self.point_4.setGeometry(QRect(140, 80, 16, 21))
        self.point_4.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"")
        self.point_4.setPixmap(QPixmap(u":/buttons/point.png"))
        self.point_4.setScaledContents(True)
        self.ubicacionT3 = QLabel(self.Tabajo3)
        self.ubicacionT3.setObjectName(u"ubicacionT3")
        self.ubicacionT3.setGeometry(QRect(170, 80, 141, 20))
        self.Tabajo4 = QGroupBox(self.details_groupBox)
        self.Tabajo4.setObjectName(u"Tabajo4")
        self.Tabajo4.setGeometry(QRect(20, 770, 341, 111))
        self.Tabajo4.setStyleSheet(u"border-radius: 43px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);")
        self.imagenT4 = QLabel(self.Tabajo4)
        self.imagenT4.setObjectName(u"imagenT4")
        self.imagenT4.setGeometry(QRect(30, 10, 91, 91))
        self.imagenT4.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid black;")
        self.descrpcionT4 = QLabel(self.Tabajo4)
        self.descrpcionT4.setObjectName(u"descrpcionT4")
        self.descrpcionT4.setGeometry(QRect(140, 10, 171, 61))
        self.descrpcionT4.setFont(font4)
        self.point_5 = QLabel(self.Tabajo4)
        self.point_5.setObjectName(u"point_5")
        self.point_5.setGeometry(QRect(140, 80, 16, 21))
        self.point_5.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"border-radius: 0px;\n"
"border: 0px solid white;\n"
"")
        self.point_5.setPixmap(QPixmap(u":/buttons/point.png"))
        self.point_5.setScaledContents(True)
        self.ubicacionT4 = QLabel(self.Tabajo4)
        self.ubicacionT4.setObjectName(u"ubicacionT4")
        self.ubicacionT4.setGeometry(QRect(170, 80, 141, 20))
        self.Portafolio_more_pushButton = QPushButton(self.details_groupBox)
        self.Portafolio_more_pushButton.setObjectName(u"Portafolio_more_pushButton")
        self.Portafolio_more_pushButton.setGeometry(QRect(160, 900, 51, 51))
        self.Portafolio_more_pushButton.setStyleSheet(u"\n"
"border: 0px solid white;")
        self.Portafolio_more_pushButton.setIcon(icon6)
        self.Portafolio_more_pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.details_groupBox)

        self.details_scrollArea.setWidget(self.details_scrollAreaWidgetContents)
        self.logo.raise_()
        self.star_pushButton.raise_()
        self.heart_pushButton.raise_()
        self.message_pushButton.raise_()
        self.bell_pushButton.raise_()
        self.main_scrollArea.raise_()
        self.home_pushButton.raise_()
        self.marca.raise_()
        self.person_pushButton.raise_()
        self.details_scrollArea.raise_()
        ProfileWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ProfileWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1700, 22))
        ProfileWindow.setMenuBar(self.menubar)

        self.retranslateUi(ProfileWindow)

        QMetaObject.connectSlotsByName(ProfileWindow)
    # setupUi

    def retranslateUi(self, ProfileWindow):
        ProfileWindow.setWindowTitle(QCoreApplication.translate("ProfileWindow", u"MainWindow", None))
        self.actionRegresar_al_inicio.setText(QCoreApplication.translate("ProfileWindow", u"Regresar al inicio", None))
        self.groupBox.setTitle("")
        self.logo.setText("")
        self.star_pushButton.setText("")
        self.home_pushButton.setText("")
        self.heart_pushButton.setText("")
        self.message_pushButton.setText("")
        self.bell_pushButton.setText("")
        self.person_pushButton.setText("")
        self.profile_groupBox.setTitle("")
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("ProfileWindow", u"     Busca el nombre de un Artista", None))
        self.Titulo.setText(QCoreApplication.translate("ProfileWindow", u"MESSENGERS", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("ProfileWindow", u"Buscar", None))
        self.top_imegen_label.setText("")
        self.publicaciones_groupBox.setTitle("")
        self.publicaciones_more_pushButton.setText("")
        self.publicacion1.setTitle("")
        self.ImagenP1.setText("")
        self.tituloP1.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.descrP1.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.up_pushButtonP1.setText("")
        self.publicacion2.setTitle("")
        self.ImagenP2.setText("")
        self.tituloP2.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.descrP2.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.up_pushButtonP2.setText("")
        self.publicacion3.setTitle("")
        self.ImagenP3.setText("")
        self.tituloP3.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.descrP3.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.up_pushButtonP3.setText("")
        self.publicacion4.setTitle("")
        self.ImagenP4.setText("")
        self.tituloP4.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.descrP4.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.up_pushButtonP4.setText("")
        self.publicacion5.setTitle("")
        self.ImagenP5.setText("")
        self.tituloP5.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.descrP5.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.up_pushButtonP5.setText("")
        self.Publicaciones.setText(QCoreApplication.translate("ProfileWindow", u"Publicaciones", None))
        self.marca.setText("")
        self.details_groupBox.setTitle("")
        self.perfil_imagen_label.setText("")
        self.info_label.setText("")
        self.point.setText("")
        self.ubicacion_label.setText("")
        self.Seguidores.setText(QCoreApplication.translate("ProfileWindow", u" Seguidores", None))
        self.seguidores_label.setText("")
        self.seguir_pushButton.setText(QCoreApplication.translate("ProfileWindow", u"Seguir", None))
        self.Portafolio.setText(QCoreApplication.translate("ProfileWindow", u"Portafolio", None))
        self.Tabajo1.setTitle("")
        self.imagenT1.setText("")
        self.descrpcionT1.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.point_2.setText("")
        self.ubicacionT1.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.Tabajo2.setTitle("")
        self.imagenT2.setText("")
        self.descrpcionT2.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.point_3.setText("")
        self.ubicacionT2.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.Tabajo3.setTitle("")
        self.imagenT3.setText("")
        self.descrpcionT3.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.point_4.setText("")
        self.ubicacionT3.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.Tabajo4.setTitle("")
        self.imagenT4.setText("")
        self.descrpcionT4.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.point_5.setText("")
        self.ubicacionT4.setText(QCoreApplication.translate("ProfileWindow", u"TextLabel", None))
        self.Portafolio_more_pushButton.setText("")
    # retranslateUi

