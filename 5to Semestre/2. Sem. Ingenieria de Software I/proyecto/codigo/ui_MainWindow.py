# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import logo_rc
import icons_rc
import logo_rc
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1700, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1700, 900))
        MainWindow.setMaximumSize(QSize(1700, 900))
        MainWindow.setBaseSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.233, y1:0.176, x2:1, y2:1, stop:0 rgba(255, 35, 79, 255), stop:1 rgba(255, 129, 62, 255))")
        self.actionAcceder = QAction(MainWindow)
        self.actionAcceder.setObjectName(u"actionAcceder")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionAbrir_Vertices = QAction(MainWindow)
        self.actionAbrir_Vertices.setObjectName(u"actionAbrir_Vertices")
        self.actionGuardar_Vertices = QAction(MainWindow)
        self.actionGuardar_Vertices.setObjectName(u"actionGuardar_Vertices")
        self.actionAbrir_Aristas = QAction(MainWindow)
        self.actionAbrir_Aristas.setObjectName(u"actionAbrir_Aristas")
        self.actionGuardar_Aristas = QAction(MainWindow)
        self.actionGuardar_Aristas.setObjectName(u"actionGuardar_Aristas")
        self.centralwidget = QWidget(MainWindow)
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
        self.star_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.star_pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/buttons/star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.star_pushButton.setIcon(icon)
        self.star_pushButton.setIconSize(QSize(34, 50))
        self.home_pushButton = QPushButton(self.groupBox)
        self.home_pushButton.setObjectName(u"home_pushButton")
        self.home_pushButton.setGeometry(QRect(40, 150, 51, 51))
        self.home_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_pushButton.setStyleSheet(u"qproperty-icon: url(:/buttons/home.png);\n"
"background-color: rgba(0,0,0,0%)")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_pushButton.setIcon(icon1)
        self.home_pushButton.setIconSize(QSize(37, 50))
        self.heart_pushButton = QPushButton(self.groupBox)
        self.heart_pushButton.setObjectName(u"heart_pushButton")
        self.heart_pushButton.setGeometry(QRect(40, 350, 51, 51))
        self.heart_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.heart_pushButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/heart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.heart_pushButton.setIcon(icon2)
        self.heart_pushButton.setIconSize(QSize(33, 35))
        self.message_pushButton = QPushButton(self.groupBox)
        self.message_pushButton.setObjectName(u"message_pushButton")
        self.message_pushButton.setGeometry(QRect(40, 450, 51, 51))
        self.message_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.message_pushButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/buttons/message.png", QSize(), QIcon.Normal, QIcon.Off)
        self.message_pushButton.setIcon(icon3)
        self.message_pushButton.setIconSize(QSize(35, 50))
        self.bell_pushButton = QPushButton(self.groupBox)
        self.bell_pushButton.setObjectName(u"bell_pushButton")
        self.bell_pushButton.setGeometry(QRect(40, 550, 51, 51))
        self.bell_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.bell_pushButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/buttons/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bell_pushButton.setIcon(icon4)
        self.bell_pushButton.setIconSize(QSize(35, 50))
        self.person_pushButton = QPushButton(self.groupBox)
        self.person_pushButton.setObjectName(u"person_pushButton")
        self.person_pushButton.setGeometry(QRect(40, 650, 51, 51))
        self.person_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.person_pushButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/buttons/person.png", QSize(), QIcon.Normal, QIcon.Off)
        self.person_pushButton.setIcon(icon5)
        self.person_pushButton.setIconSize(QSize(40, 50))
        self.main_scrollArea = QScrollArea(self.groupBox)
        self.main_scrollArea.setObjectName(u"main_scrollArea")
        self.main_scrollArea.setGeometry(QRect(120, 30, 1321, 691))
        self.main_scrollArea.setMinimumSize(QSize(1321, 691))
        self.main_scrollArea.setMaximumSize(QSize(1321, 691))
        self.main_scrollArea.setAutoFillBackground(False)
        self.main_scrollArea.setStyleSheet(u"")
        self.main_scrollArea.setFrameShape(QFrame.NoFrame)
        self.main_scrollArea.setFrameShadow(QFrame.Sunken)
        self.main_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.main_scrollArea.setWidgetResizable(True)
        self.main_scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.home_scrollAreaWidgetContents = QWidget()
        self.home_scrollAreaWidgetContents.setObjectName(u"home_scrollAreaWidgetContents")
        self.home_scrollAreaWidgetContents.setGeometry(QRect(0, -161, 1311, 1218))
        font = QFont()
        font.setPointSize(13)
        self.home_scrollAreaWidgetContents.setFont(font)
        self.home_scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.home_scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_groupBox = QGroupBox(self.home_scrollAreaWidgetContents)
        self.home_groupBox.setObjectName(u"home_groupBox")
        self.home_groupBox.setMinimumSize(QSize(0, 1200))
        self.home_groupBox.setStyleSheet(u"background-color: rgb(31, 38, 46);\n"
"border-color: rgb(22, 27, 32);\n"
"border-radius: 43px;")
        self.eventos_radioButton_5 = QRadioButton(self.home_groupBox)
        self.eventos_radioButton_5.setObjectName(u"eventos_radioButton_5")
        self.eventos_radioButton_5.setGeometry(QRect(690, 290, 16, 16))
        self.eventos_radioButton_1 = QRadioButton(self.home_groupBox)
        self.eventos_radioButton_1.setObjectName(u"eventos_radioButton_1")
        self.eventos_radioButton_1.setGeometry(QRect(570, 290, 16, 16))
        self.eventos_radioButton_3 = QRadioButton(self.home_groupBox)
        self.eventos_radioButton_3.setObjectName(u"eventos_radioButton_3")
        self.eventos_radioButton_3.setGeometry(QRect(630, 290, 16, 16))
        self.buscar_lineEdit = QLineEdit(self.home_groupBox)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")
        self.buscar_lineEdit.setGeometry(QRect(480, 20, 341, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.buscar_lineEdit.setFont(font1)
        self.buscar_lineEdit.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Titulo = QLabel(self.home_groupBox)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(70, 10, 291, 41))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(35)
        font2.setBold(True)
        self.Titulo.setFont(font2)
        self.Titulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.eventos_radioButton_2 = QRadioButton(self.home_groupBox)
        self.eventos_radioButton_2.setObjectName(u"eventos_radioButton_2")
        self.eventos_radioButton_2.setGeometry(QRect(600, 290, 16, 16))
        self.eventos_label = QLabel(self.home_groupBox)
        self.eventos_label.setObjectName(u"eventos_label")
        self.eventos_label.setGeometry(QRect(90, 130, 1121, 151))
        self.eventos_label.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid white;\n"
"")
        self.eventos_label.setScaledContents(False)
        self.eventos_label.setOpenExternalLinks(True)
        self.eventos_radioButton_4 = QRadioButton(self.home_groupBox)
        self.eventos_radioButton_4.setObjectName(u"eventos_radioButton_4")
        self.eventos_radioButton_4.setGeometry(QRect(660, 290, 16, 16))
        self.eventos_radioButton_6 = QRadioButton(self.home_groupBox)
        self.eventos_radioButton_6.setObjectName(u"eventos_radioButton_6")
        self.eventos_radioButton_6.setGeometry(QRect(720, 290, 16, 16))
        self.Artistas = QLabel(self.home_groupBox)
        self.Artistas.setObjectName(u"Artistas")
        self.Artistas.setGeometry(QRect(70, 330, 101, 31))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.Artistas.setFont(font3)
        self.Artistas.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Eventos = QLabel(self.home_groupBox)
        self.Eventos.setObjectName(u"Eventos")
        self.Eventos.setGeometry(QRect(70, 80, 101, 31))
        self.Eventos.setFont(font3)
        self.Eventos.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.buscar_pushButton = QPushButton(self.home_groupBox)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")
        self.buscar_pushButton.setGeometry(QRect(400, 20, 75, 41))
        self.buscar_pushButton.setFont(font1)
        self.buscar_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.buscar_pushButton.setStyleSheet(u"background-color: rgb(22, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.artista_crollArea = QScrollArea(self.home_groupBox)
        self.artista_crollArea.setObjectName(u"artista_crollArea")
        self.artista_crollArea.setGeometry(QRect(90, 380, 1121, 191))
        self.artista_crollArea.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid white;\n"
"")
        self.artista_crollArea.setWidgetResizable(True)
        self.artista_scrollAreaWidgetContents = QWidget()
        self.artista_scrollAreaWidgetContents.setObjectName(u"artista_scrollAreaWidgetContents")
        self.artista_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1518, 172))
        self.horizontalLayout = QHBoxLayout(self.artista_scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.artista_groupBox = QGroupBox(self.artista_scrollAreaWidgetContents)
        self.artista_groupBox.setObjectName(u"artista_groupBox")
        self.artista_groupBox.setMinimumSize(QSize(1500, 138))
        self.artista_groupBox.setStyleSheet(u"border-radius: 0px;\n"
"border: 0px solid white;\n"
"")
        self.pushButton = QPushButton(self.artista_groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1430, 50, 51, 51))
        icon6 = QIcon()
        icon6.addFile(u":/buttons/restart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(30, 30))
        self.art1_pushButton = QPushButton(self.artista_groupBox)
        self.art1_pushButton.setObjectName(u"art1_pushButton")
        self.art1_pushButton.setGeometry(QRect(10, 0, 141, 151))
        font4 = QFont()
        font4.setPointSize(16)
        self.art1_pushButton.setFont(font4)
        self.art1_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.art1_pushButton.setStyleSheet(u"border-radius: 10px;\n"
"border: 5px solid gold;\n"
"background-color: rgb(240, 240, 240);\n"
"Text-align:bottom")
        self.art2_pushButton = QPushButton(self.artista_groupBox)
        self.art2_pushButton.setObjectName(u"art2_pushButton")
        self.art2_pushButton.setGeometry(QRect(210, 0, 141, 151))
        self.art2_pushButton.setFont(font4)
        self.art2_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.art2_pushButton.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);\n"
"Text-align:bottom")
        self.art3_pushButton = QPushButton(self.artista_groupBox)
        self.art3_pushButton.setObjectName(u"art3_pushButton")
        self.art3_pushButton.setGeometry(QRect(410, 0, 141, 151))
        self.art3_pushButton.setFont(font4)
        self.art3_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.art3_pushButton.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);\n"
"Text-align:bottom")
        self.art4_pushButton = QPushButton(self.artista_groupBox)
        self.art4_pushButton.setObjectName(u"art4_pushButton")
        self.art4_pushButton.setGeometry(QRect(610, 0, 141, 151))
        self.art4_pushButton.setFont(font4)
        self.art4_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.art4_pushButton.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);\n"
"Text-align:bottom")
        self.art5_pushButton = QPushButton(self.artista_groupBox)
        self.art5_pushButton.setObjectName(u"art5_pushButton")
        self.art5_pushButton.setGeometry(QRect(810, 0, 141, 151))
        self.art5_pushButton.setFont(font4)
        self.art5_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.art5_pushButton.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);\n"
"Text-align:bottom")
        self.art6_pushButton = QPushButton(self.artista_groupBox)
        self.art6_pushButton.setObjectName(u"art6_pushButton")
        self.art6_pushButton.setGeometry(QRect(1010, 0, 141, 151))
        self.art6_pushButton.setFont(font4)
        self.art6_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.art6_pushButton.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);\n"
"Text-align:bottom")
        self.art7_pushButton = QPushButton(self.artista_groupBox)
        self.art7_pushButton.setObjectName(u"art7_pushButton")
        self.art7_pushButton.setGeometry(QRect(1210, 0, 141, 151))
        self.art7_pushButton.setFont(font4)
        self.art7_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.art7_pushButton.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid white;\n"
"background-color: rgb(240, 240, 240);\n"
"Text-align:bottom")

        self.horizontalLayout.addWidget(self.artista_groupBox)

        self.artista_crollArea.setWidget(self.artista_scrollAreaWidgetContents)
        self.Artistas_2 = QLabel(self.home_groupBox)
        self.Artistas_2.setObjectName(u"Artistas_2")
        self.Artistas_2.setGeometry(QRect(70, 610, 161, 31))
        self.Artistas_2.setFont(font3)
        self.Artistas_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.publicaciones_scrollArea = QScrollArea(self.home_groupBox)
        self.publicaciones_scrollArea.setObjectName(u"publicaciones_scrollArea")
        self.publicaciones_scrollArea.setGeometry(QRect(90, 660, 1121, 511))
        self.publicaciones_scrollArea.setStyleSheet(u"border-radius: 0px;\n"
"border: 1px solid white;\n"
"")
        self.publicaciones_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1109, 1068))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.publicaciones_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.publicaciones_groupBox.setObjectName(u"publicaciones_groupBox")
        self.publicaciones_groupBox.setMinimumSize(QSize(0, 1050))
        self.publicaciones_groupBox.setStyleSheet(u"border-radius: 0px;\n"
"border: 0px solid white;\n"
"")
        self.pushButton_2 = QPushButton(self.publicaciones_groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(520, 940, 51, 51))
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.publicaciones_groupBox_2 = QGroupBox(self.publicaciones_groupBox)
        self.publicaciones_groupBox_2.setObjectName(u"publicaciones_groupBox_2")
        self.publicaciones_groupBox_2.setGeometry(QRect(140, 0, 811, 1050))
        self.publicaciones_groupBox_2.setMinimumSize(QSize(0, 1050))
        self.publicaciones_groupBox_2.setStyleSheet(u"border-radius: 0px;\n"
"border: 0px solid white;\n"
"")
        self.publicaciones_more_pushButton = QPushButton(self.publicaciones_groupBox_2)
        self.publicaciones_more_pushButton.setObjectName(u"publicaciones_more_pushButton")
        self.publicaciones_more_pushButton.setGeometry(QRect(380, 990, 51, 51))
        icon7 = QIcon()
        icon7.addFile(u":/buttons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.publicaciones_more_pushButton.setIcon(icon7)
        self.publicaciones_more_pushButton.setIconSize(QSize(50, 50))
        self.publicacion1 = QGroupBox(self.publicaciones_groupBox_2)
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
        font5 = QFont()
        font5.setPointSize(18)
        self.tituloP1.setFont(font5)
        self.descrP1 = QLabel(self.publicacion1)
        self.descrP1.setObjectName(u"descrP1")
        self.descrP1.setGeometry(QRect(280, 60, 461, 81))
        font6 = QFont()
        font6.setPointSize(12)
        self.descrP1.setFont(font6)
        self.descrP1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP1 = QPushButton(self.publicacion1)
        self.up_pushButtonP1.setObjectName(u"up_pushButtonP1")
        self.up_pushButtonP1.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP1.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_pushButtonP1.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        icon8 = QIcon()
        icon8.addFile(u":/buttons/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.up_pushButtonP1.setIcon(icon8)
        self.up_pushButtonP1.setIconSize(QSize(35, 50))
        self.publicacion2 = QGroupBox(self.publicaciones_groupBox_2)
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
        self.tituloP2.setFont(font5)
        self.descrP2 = QLabel(self.publicacion2)
        self.descrP2.setObjectName(u"descrP2")
        self.descrP2.setGeometry(QRect(280, 60, 460, 81))
        self.descrP2.setFont(font6)
        self.descrP2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP2 = QPushButton(self.publicacion2)
        self.up_pushButtonP2.setObjectName(u"up_pushButtonP2")
        self.up_pushButtonP2.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP2.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_pushButtonP2.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        self.up_pushButtonP2.setIcon(icon8)
        self.up_pushButtonP2.setIconSize(QSize(35, 50))
        self.publicacion3 = QGroupBox(self.publicaciones_groupBox_2)
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
        self.tituloP3.setFont(font5)
        self.descrP3 = QLabel(self.publicacion3)
        self.descrP3.setObjectName(u"descrP3")
        self.descrP3.setGeometry(QRect(280, 60, 461, 81))
        self.descrP3.setFont(font6)
        self.descrP3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP3 = QPushButton(self.publicacion3)
        self.up_pushButtonP3.setObjectName(u"up_pushButtonP3")
        self.up_pushButtonP3.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP3.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_pushButtonP3.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        self.up_pushButtonP3.setIcon(icon8)
        self.up_pushButtonP3.setIconSize(QSize(35, 50))
        self.publicacion4 = QGroupBox(self.publicaciones_groupBox_2)
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
        self.tituloP4.setFont(font5)
        self.descrP4 = QLabel(self.publicacion4)
        self.descrP4.setObjectName(u"descrP4")
        self.descrP4.setGeometry(QRect(280, 60, 461, 81))
        self.descrP4.setFont(font6)
        self.descrP4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP4 = QPushButton(self.publicacion4)
        self.up_pushButtonP4.setObjectName(u"up_pushButtonP4")
        self.up_pushButtonP4.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP4.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_pushButtonP4.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        self.up_pushButtonP4.setIcon(icon8)
        self.up_pushButtonP4.setIconSize(QSize(35, 50))
        self.publicacion5 = QGroupBox(self.publicaciones_groupBox_2)
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
        self.tituloP5.setFont(font5)
        self.descrP5 = QLabel(self.publicacion5)
        self.descrP5.setObjectName(u"descrP5")
        self.descrP5.setGeometry(QRect(280, 60, 461, 81))
        self.descrP5.setFont(font6)
        self.descrP5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.up_pushButtonP5 = QPushButton(self.publicacion5)
        self.up_pushButtonP5.setObjectName(u"up_pushButtonP5")
        self.up_pushButtonP5.setGeometry(QRect(740, 20, 50, 41))
        self.up_pushButtonP5.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_pushButtonP5.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"border: 0px solid white;")
        self.up_pushButtonP5.setIcon(icon8)
        self.up_pushButtonP5.setIconSize(QSize(35, 50))

        self.verticalLayout_2.addWidget(self.publicaciones_groupBox)

        self.publicaciones_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.home_groupBox)

        self.main_scrollArea.setWidget(self.home_scrollAreaWidgetContents)
        self.marca = QLabel(self.groupBox)
        self.marca.setObjectName(u"marca")
        self.marca.setGeometry(QRect(40, 150, 51, 51))
        self.marca.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.233, y1:0.176, x2:1, y2:1, stop:0 rgba(255, 35, 79, 40%), stop:1 rgba(255, 129, 62, 40%));\n"
"border-radius: 43px;")
        self.logo.raise_()
        self.star_pushButton.raise_()
        self.heart_pushButton.raise_()
        self.message_pushButton.raise_()
        self.bell_pushButton.raise_()
        self.person_pushButton.raise_()
        self.main_scrollArea.raise_()
        self.marca.raise_()
        self.home_pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1700, 22))
        self.menuLogIn = QMenu(self.menubar)
        self.menuLogIn.setObjectName(u"menuLogIn")
        self.menuGrafo = QMenu(self.menubar)
        self.menuGrafo.setObjectName(u"menuGrafo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuLogIn.menuAction())
        self.menubar.addAction(self.menuGrafo.menuAction())
        self.menuLogIn.addAction(self.actionAcceder)
        self.menuLogIn.addAction(self.actionSalir)
        self.menuGrafo.addAction(self.actionAbrir_Vertices)
        self.menuGrafo.addAction(self.actionGuardar_Vertices)
        self.menuGrafo.addAction(self.actionAbrir_Aristas)
        self.menuGrafo.addAction(self.actionGuardar_Aristas)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAcceder.setText(QCoreApplication.translate("MainWindow", u"Acceder", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionAbrir_Vertices.setText(QCoreApplication.translate("MainWindow", u"Abrir Vertices", None))
        self.actionGuardar_Vertices.setText(QCoreApplication.translate("MainWindow", u"Guardar Vertices", None))
        self.actionAbrir_Aristas.setText(QCoreApplication.translate("MainWindow", u"Abrir Aristas", None))
        self.actionGuardar_Aristas.setText(QCoreApplication.translate("MainWindow", u"Guardar Aristas", None))
        self.groupBox.setTitle("")
        self.logo.setText("")
        self.star_pushButton.setText("")
        self.home_pushButton.setText("")
        self.heart_pushButton.setText("")
        self.message_pushButton.setText("")
        self.bell_pushButton.setText("")
        self.person_pushButton.setText("")
        self.home_groupBox.setTitle("")
        self.eventos_radioButton_5.setText("")
        self.eventos_radioButton_1.setText("")
        self.eventos_radioButton_3.setText("")
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"     Busca el nombre de un Artista", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"MESSENGERS", None))
        self.eventos_radioButton_2.setText("")
        self.eventos_label.setText("")
        self.eventos_radioButton_4.setText("")
        self.eventos_radioButton_6.setText("")
        self.Artistas.setText(QCoreApplication.translate("MainWindow", u"Artistas", None))
        self.Eventos.setText(QCoreApplication.translate("MainWindow", u"Eventos", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.artista_groupBox.setTitle("")
        self.pushButton.setText("")
        self.art1_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.art2_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.art3_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.art4_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.art5_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.art6_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.art7_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Artistas_2.setText(QCoreApplication.translate("MainWindow", u"Publicaciones", None))
        self.publicaciones_groupBox.setTitle("")
        self.pushButton_2.setText("")
        self.publicaciones_groupBox_2.setTitle("")
        self.publicaciones_more_pushButton.setText("")
        self.publicacion1.setTitle("")
        self.ImagenP1.setText("")
        self.tituloP1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.descrP1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.up_pushButtonP1.setText("")
        self.publicacion2.setTitle("")
        self.ImagenP2.setText("")
        self.tituloP2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.descrP2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.up_pushButtonP2.setText("")
        self.publicacion3.setTitle("")
        self.ImagenP3.setText("")
        self.tituloP3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.descrP3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.up_pushButtonP3.setText("")
        self.publicacion4.setTitle("")
        self.ImagenP4.setText("")
        self.tituloP4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.descrP4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.up_pushButtonP4.setText("")
        self.publicacion5.setTitle("")
        self.ImagenP5.setText("")
        self.tituloP5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.descrP5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.up_pushButtonP5.setText("")
        self.marca.setText("")
        self.menuLogIn.setTitle(QCoreApplication.translate("MainWindow", u"LogIn", None))
        self.menuGrafo.setTitle(QCoreApplication.translate("MainWindow", u"Grafo", None))
    # retranslateUi

