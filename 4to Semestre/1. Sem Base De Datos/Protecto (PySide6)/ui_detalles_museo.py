# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detalles_museo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1602, 1092)
        self.actionVolver_al_inicio = QAction(MainWindow)
        self.actionVolver_al_inicio.setObjectName(u"actionVolver_al_inicio")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1620, 1080))
        self.label.setMinimumSize(QSize(931, 0))
        self.label.setPixmap(QPixmap(u"C:/Users/Usuario/Downloads/albert-vincent-wu-hAWs6oHfhms-unsplash (2).jpg"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 1621, 71))
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"	font: 28pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(170, 130, 1271, 901))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"font: 14pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(68, 68, 68)\n"
"\n"
"}")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"\n"
"font: 18pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(98, 138, 76)\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_8, 7, 3, 1, 1)

        self.col_tem_graphicsView = QGraphicsView(self.groupBox)
        self.col_tem_graphicsView.setObjectName(u"col_tem_graphicsView")

        self.gridLayout.addWidget(self.col_tem_graphicsView, 8, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"\n"
"font: 18pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(98, 138, 76)\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_5, 7, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"\n"
"font: 18pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(98, 138, 76)\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_7, 4, 3, 1, 1)

        self.desc_mus_graphicsView = QGraphicsView(self.groupBox)
        self.desc_mus_graphicsView.setObjectName(u"desc_mus_graphicsView")

        self.gridLayout.addWidget(self.desc_mus_graphicsView, 5, 1, 1, 1)

        self.col_per_graphicsView = QGraphicsView(self.groupBox)
        self.col_per_graphicsView.setObjectName(u"col_per_graphicsView")

        self.gridLayout.addWidget(self.col_per_graphicsView, 5, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 6, 1)

        self.act_esp_graphicsView = QGraphicsView(self.groupBox)
        self.act_esp_graphicsView.setObjectName(u"act_esp_graphicsView")

        self.gridLayout.addWidget(self.act_esp_graphicsView, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"\n"
"font: 18pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(98, 138, 76)\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.horarios_graphicsView = QGraphicsView(self.groupBox)
        self.horarios_graphicsView.setObjectName(u"horarios_graphicsView")

        self.gridLayout.addWidget(self.horarios_graphicsView, 2, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"\n"
"font: 18pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(98, 138, 76)\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 2, 8, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 1, 1, 1)

        self.acc_mus_graphicsView = QGraphicsView(self.groupBox)
        self.acc_mus_graphicsView.setObjectName(u"acc_mus_graphicsView")

        self.gridLayout.addWidget(self.acc_mus_graphicsView, 8, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 9, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"\n"
"font: 18pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(98, 138, 76)\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1602, 21))
        self.menuRegresar = QMenu(self.menubar)
        self.menuRegresar.setObjectName(u"menuRegresar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuRegresar.menuAction())
        self.menuRegresar.addAction(self.actionVolver_al_inicio)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionVolver_al_inicio.setText(QCoreApplication.translate("MainWindow", u"Volver al inicio", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Muesos Jalisco</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"   Muesos Jalisco", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Acciones Administrador BD", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Colecciones Temporales", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Accesibilidad del Museo", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Colecciones Permanentes", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Actividades Especiales ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Horarios", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n del Museo", None))
        self.menuRegresar.setTitle(QCoreApplication.translate("MainWindow", u"Regresar", None))
    # retranslateUi

