# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_in.ui'
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
        MainWindow.resize(1619, 1091)
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
        self.nombre_usuario_lineEdit = QLineEdit(self.centralwidget)
        self.nombre_usuario_lineEdit.setObjectName(u"nombre_usuario_lineEdit")
        self.nombre_usuario_lineEdit.setGeometry(QRect(610, 320, 391, 51))
        self.nombre_usuario_lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        self.log_in_pushButton = QPushButton(self.centralwidget)
        self.log_in_pushButton.setObjectName(u"log_in_pushButton")
        self.log_in_pushButton.setGeometry(QRect(770, 600, 91, 41))
        self.log_in_pushButton.setStyleSheet(u"QPushButton{\n"
"font: 14pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"}")
        self.contasea_lineEdid = QLineEdit(self.centralwidget)
        self.contasea_lineEdid.setObjectName(u"contasea_lineEdid")
        self.contasea_lineEdid.setGeometry(QRect(610, 480, 391, 51))
        self.contasea_lineEdid.setStyleSheet(u"QLineEdit{\n"
"font: 12pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(122, 122, 122)\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1619, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.nombre_usuario_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de Usuario", None))
        self.log_in_pushButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.contasea_lineEdid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
    # retranslateUi

