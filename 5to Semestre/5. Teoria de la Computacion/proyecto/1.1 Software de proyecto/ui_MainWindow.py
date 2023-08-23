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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Titulo = QLabel(self.centralwidget)
        self.Titulo.setObjectName(u"Titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Titulo.setFont(font)
        self.Titulo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Titulo, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Val = QWidget()
        self.Val.setObjectName(u"Val")
        self.gridLayout_2 = QGridLayout(self.Val)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 4, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 2, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 2, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 3, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 3, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 4, 2, 1, 1)

        self.val_pushButton = QPushButton(self.Val)
        self.val_pushButton.setObjectName(u"val_pushButton")
        self.val_pushButton.setMinimumSize(QSize(50, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.val_pushButton.setFont(font1)

        self.gridLayout_2.addWidget(self.val_pushButton, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.val_lineEdit = QLineEdit(self.Val)
        self.val_lineEdit.setObjectName(u"val_lineEdit")
        self.val_lineEdit.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setPointSize(12)
        self.val_lineEdit.setFont(font2)

        self.gridLayout_2.addWidget(self.val_lineEdit, 2, 2, 1, 1)

        self.titulo_Val = QLabel(self.Val)
        self.titulo_Val.setObjectName(u"titulo_Val")
        self.titulo_Val.setMinimumSize(QSize(0, 50))
        self.titulo_Val.setFont(font1)
        self.titulo_Val.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.titulo_Val, 1, 2, 1, 1)

        self.tabWidget.addTab(self.Val, "")
        self.Cre = QWidget()
        self.Cre.setObjectName(u"Cre")
        self.gridLayout_3 = QGridLayout(self.Cre)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(648, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.titulo_Val_2 = QLabel(self.Cre)
        self.titulo_Val_2.setObjectName(u"titulo_Val_2")
        self.titulo_Val_2.setMinimumSize(QSize(0, 50))
        self.titulo_Val_2.setFont(font1)
        self.titulo_Val_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.titulo_Val_2, 1, 2, 1, 1)

        self.cre_nom_lineEdit = QLineEdit(self.Cre)
        self.cre_nom_lineEdit.setObjectName(u"cre_nom_lineEdit")
        self.cre_nom_lineEdit.setMinimumSize(QSize(0, 50))
        self.cre_nom_lineEdit.setFont(font2)

        self.gridLayout_3.addWidget(self.cre_nom_lineEdit, 3, 2, 1, 1)

        self.cre_ape_lineEdit = QLineEdit(self.Cre)
        self.cre_ape_lineEdit.setObjectName(u"cre_ape_lineEdit")
        self.cre_ape_lineEdit.setMinimumSize(QSize(0, 50))
        self.cre_ape_lineEdit.setFont(font2)

        self.gridLayout_3.addWidget(self.cre_ape_lineEdit, 4, 2, 1, 1)

        self.cre_pushButton = QPushButton(self.Cre)
        self.cre_pushButton.setObjectName(u"cre_pushButton")
        self.cre_pushButton.setMinimumSize(QSize(50, 50))
        self.cre_pushButton.setFont(font1)

        self.gridLayout_3.addWidget(self.cre_pushButton, 5, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(648, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 6, 2, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 341, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_14, 2, 3, 4, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 285, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_9, 5, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 74, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_10, 5, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_12, 5, 4, 1, 1)

        self.tabWidget.addTab(self.Cre, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"Validador y creador de cadenas en el formato de correos institucionales de UDG", None))
        self.val_pushButton.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.val_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Ingresa un correo de la UDG", None))
        self.titulo_Val.setText(QCoreApplication.translate("MainWindow", u"Ingresa un correo para validar si tiene el formato requerido ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Val), QCoreApplication.translate("MainWindow", u"Validar", None))
        self.titulo_Val_2.setText(QCoreApplication.translate("MainWindow", u"Ingresa tu nombre para generar un correo con formato de la UDG", None))
        self.cre_nom_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Ingresa tu Nombre", None))
        self.cre_ape_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Ingresa tu primer Apellido", None))
        self.cre_pushButton.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cre), QCoreApplication.translate("MainWindow", u"Crear", None))
    # retranslateUi

