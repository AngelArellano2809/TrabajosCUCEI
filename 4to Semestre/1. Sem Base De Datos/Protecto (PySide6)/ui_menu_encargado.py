# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_encargado.ui'
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
        MainWindow.resize(1623, 1066)
        self.actionAvisos = QAction(MainWindow)
        self.actionAvisos.setObjectName(u"actionAvisos")
        self.actionContactar_Administrados = QAction(MainWindow)
        self.actionContactar_Administrados.setObjectName(u"actionContactar_Administrados")
        self.actionConfiguracion = QAction(MainWindow)
        self.actionConfiguracion.setObjectName(u"actionConfiguracion")
        self.actionSing_Out = QAction(MainWindow)
        self.actionSing_Out.setObjectName(u"actionSing_Out")
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
        self.groupBox.setGeometry(QRect(420, 120, 781, 851))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"font: 14pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(68, 68, 68)\n"
"\n"
"}")
        self.eleminar_graphicsView = QGraphicsView(self.groupBox)
        self.eleminar_graphicsView.setObjectName(u"eleminar_graphicsView")
        self.eleminar_graphicsView.setGeometry(QRect(36, 345, 361, 221))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(36, 593, 711, 27))
        self.label_5.setStyleSheet(u"QLabel{\n"
"\n"
"font: 18pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(98, 138, 76)\n"
"\n"
"}")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(36, 312, 711, 27))
        self.label_4.setStyleSheet(u"QLabel{\n"
"\n"
"font: 18pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(98, 138, 76)\n"
"\n"
"}")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(36, 32, 711, 27))
        self.label_3.setStyleSheet(u"QLabel{\n"
"\n"
"font: 18pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(98, 138, 76)\n"
"\n"
"}")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(36, 65, 709, 215))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"\n"
"background-color:rgb(162, 162,162)\n"
"\n"
"}")
        self.add_nom_lineEdit = QLineEdit(self.groupBox_2)
        self.add_nom_lineEdit.setObjectName(u"add_nom_lineEdit")
        self.add_nom_lineEdit.setGeometry(QRect(50, 30, 291, 31))
        self.add_nom_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.add_des_lineEdit = QLineEdit(self.groupBox_2)
        self.add_des_lineEdit.setObjectName(u"add_des_lineEdit")
        self.add_des_lineEdit.setGeometry(QRect(50, 80, 291, 31))
        self.add_des_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.add_tem_lineEdit = QLineEdit(self.groupBox_2)
        self.add_tem_lineEdit.setObjectName(u"add_tem_lineEdit")
        self.add_tem_lineEdit.setGeometry(QRect(50, 130, 291, 31))
        self.add_tem_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.add_fec_ini_lineEdit = QLineEdit(self.groupBox_2)
        self.add_fec_ini_lineEdit.setObjectName(u"add_fec_ini_lineEdit")
        self.add_fec_ini_lineEdit.setGeometry(QRect(400, 130, 131, 31))
        self.add_fec_ini_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.add_fec_fin_lineEdit = QLineEdit(self.groupBox_2)
        self.add_fec_fin_lineEdit.setObjectName(u"add_fec_fin_lineEdit")
        self.add_fec_fin_lineEdit.setGeometry(QRect(550, 130, 131, 31))
        self.add_fec_fin_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.per_radioButton = QRadioButton(self.groupBox_2)
        self.per_radioButton.setObjectName(u"per_radioButton")
        self.per_radioButton.setGeometry(QRect(480, 30, 111, 31))
        self.per_radioButton.setStyleSheet(u"QRadioButton{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"}")
        self.tem_radioButton = QRadioButton(self.groupBox_2)
        self.tem_radioButton.setObjectName(u"tem_radioButton")
        self.tem_radioButton.setGeometry(QRect(480, 80, 111, 31))
        self.tem_radioButton.setStyleSheet(u"QRadioButton{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"}")
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 174, 101, 30))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"font: 14pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"}")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(404, 345, 341, 221))
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
"\n"
"background-color:rgb(162, 162,162)\n"
"\n"
"}")
        self.eli_col_lineEdit = QLineEdit(self.groupBox_3)
        self.eli_col_lineEdit.setObjectName(u"eli_col_lineEdit")
        self.eli_col_lineEdit.setGeometry(QRect(30, 60, 291, 31))
        self.eli_col_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.eli_col_pushButton = QPushButton(self.groupBox_3)
        self.eli_col_pushButton.setObjectName(u"eli_col_pushButton")
        self.eli_col_pushButton.setGeometry(QRect(120, 120, 101, 41))
        self.eli_col_pushButton.setStyleSheet(u"QPushButton{\n"
"font: 14pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"}")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(36, 626, 710, 215))
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"\n"
"background-color:rgb(162, 162,162)\n"
"\n"
"}")
        self.mod_nom_lineEdit = QLineEdit(self.groupBox_4)
        self.mod_nom_lineEdit.setObjectName(u"mod_nom_lineEdit")
        self.mod_nom_lineEdit.setGeometry(QRect(40, 40, 291, 31))
        self.mod_nom_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.mod_pushButton = QPushButton(self.groupBox_4)
        self.mod_pushButton.setObjectName(u"mod_pushButton")
        self.mod_pushButton.setGeometry(QRect(310, 170, 101, 31))
        self.mod_pushButton.setStyleSheet(u"QPushButton{\n"
"font: 14pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"}")
        self.mod_ubi_lineEdit = QLineEdit(self.groupBox_4)
        self.mod_ubi_lineEdit.setObjectName(u"mod_ubi_lineEdit")
        self.mod_ubi_lineEdit.setGeometry(QRect(380, 40, 291, 31))
        self.mod_ubi_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.mod_con_lineEdit = QLineEdit(self.groupBox_4)
        self.mod_con_lineEdit.setObjectName(u"mod_con_lineEdit")
        self.mod_con_lineEdit.setGeometry(QRect(380, 110, 291, 31))
        self.mod_con_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.mod_hor_lineEdit = QLineEdit(self.groupBox_4)
        self.mod_hor_lineEdit.setObjectName(u"mod_hor_lineEdit")
        self.mod_hor_lineEdit.setGeometry(QRect(40, 110, 291, 31))
        self.mod_hor_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1623, 21))
        self.menuEncargado_Museo = QMenu(self.menubar)
        self.menuEncargado_Museo.setObjectName(u"menuEncargado_Museo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEncargado_Museo.menuAction())
        self.menuEncargado_Museo.addAction(self.actionAvisos)
        self.menuEncargado_Museo.addAction(self.actionContactar_Administrados)
        self.menuEncargado_Museo.addAction(self.actionConfiguracion)
        self.menuEncargado_Museo.addSeparator()
        self.menuEncargado_Museo.addAction(self.actionSing_Out)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAvisos.setText(QCoreApplication.translate("MainWindow", u"Avisos", None))
        self.actionContactar_Administrados.setText(QCoreApplication.translate("MainWindow", u"Contactar Administrador", None))
        self.actionConfiguracion.setText(QCoreApplication.translate("MainWindow", u"Configuracion", None))
        self.actionSing_Out.setText(QCoreApplication.translate("MainWindow", u"Sing Out", None))
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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Acciones Encargados de Museos", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Modificar Informaci\u00f3n de Museo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Eliminar Colecci\u00f3n Temporal", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Colecci\u00f3n Temporal", None))
        self.groupBox_2.setTitle("")
        self.add_nom_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre museo", None))
        self.add_des_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n Museo", None))
        self.add_tem_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tema Museo", None))
        self.add_fec_ini_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha Inicio", None))
        self.add_fec_fin_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha Final", None))
        self.per_radioButton.setText(QCoreApplication.translate("MainWindow", u"Permanente", None))
        self.tem_radioButton.setText(QCoreApplication.translate("MainWindow", u"Temporal", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.groupBox_3.setTitle("")
        self.eli_col_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre Colecci\u00f3n", None))
        self.eli_col_pushButton.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.groupBox_4.setTitle("")
        self.mod_nom_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre Museo", None))
        self.mod_pushButton.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.mod_ubi_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ubicaci\u00f3n Museo", None))
        self.mod_con_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contacto Museo", None))
        self.mod_hor_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Horario Museo", None))
        self.menuEncargado_Museo.setTitle(QCoreApplication.translate("MainWindow", u"Encargado\ufeff Museo", None))
    # retranslateUi

