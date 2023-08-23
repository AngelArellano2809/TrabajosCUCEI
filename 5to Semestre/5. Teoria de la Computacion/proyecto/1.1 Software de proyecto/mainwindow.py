from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox
from PySide6.QtCore import Slot
from ui_MainWindow import Ui_MainWindow
from matriz import Matriz
from pila import Pila
from random import randrange

class MainWindow(QMainWindow):
    def __init__(self):                              
        super(MainWindow,self).__init__()

        self.ui = Ui_MainWindow()   #Iniciador
        self.ui.setupUi(self)
        self.M = Matriz()

        #Pestania Validar
        self.ui.val_pushButton.clicked.connect(self.validar)

        #Pestania Crear
        self.ui.cre_pushButton.clicked.connect(self.crear)

    #Funcion para buscar un artista en la base de datos
    @Slot( )
    def validar(self):
        valido = True  #bandera de aceptacion final
        estado = 0  #definimos es estado inicial
        pila = Pila()   #creamos una pila

        cadena = self.ui.val_lineEdit.text()    #obtenemos la cadena ingresada

        if self.M.matriz[estado][0][0] == 'lam':    #trato unico para q0
            for char in self.M.matriz[estado][0][2]:    #apilar
                pila.apilar(char)
            print('pila Inicial: ' + str(pila.show()))
            estado = self.M.matriz[estado][0][3]    #nuevo estado

        for char in cadena:     #for que itera sobre los caracteres de la cadena
            print()
            print('Entra: ' + str(char))
            if valido is False:     #si la cadena se descarta para todo
                break
            else:
                print('estado q'+ str(estado) + ':' + str(self.M.matriz[estado]))

                if len(self.M.matriz[estado]) == 1: #Reglas para los estdados con 1 transicion 
                    if self.M.matriz[estado][0] == '-':    #trato unico para q18
                        valido = False#condicion de exceso de caracteres
                        break
                    else:           #reglas de estados q4 a q17
                        if char == self.M.matriz[estado][0][0]: #coinside el caracter
                            estado = self.M.matriz[estado][0][3]    #nuevo estado
                            continue
                        else:   #no coinside el caracter (no valido)
                            valido = False
                            continue
                
                elif len(self.M.matriz[estado]) == 4:#Reglas para los estdados con 4 transiciones q1 y q2
                    print('Pila: ' + str(pila.show()) + str(estado))
                    if pila.show()[0] == 'P': #hay una P al top de la pila
                        if ord(char)>ord('`') and ord(char)<ord('{'):
                            pila.desapilar()
                            estado = self.M.matriz[estado][0][3]
                            continue
                        else:
                            valido = False
                            continue
                    elif pila.show()[0] == 'L': #hay una L al top de la pila
                        if ord(char)>ord('`') and ord(char)<ord('{'):
                            pila.desapilar()
                            estado = self.M.matriz[estado][1][3]
                            continue
                        elif (char == '.' and estado == 1) or (ord(char)>ord('/') and ord(char)<ord(':') and estado == 2):
                            while pila.show()[0] == 'L':
                                pila.desapilar()
                            for char in self.M.matriz[estado][3][2]:    #apilar
                                pila.apilar(char)
                            print('pila: ' + str(pila.show()))
                            estado = self.M.matriz[estado][3][3]#nuevo estado
                        else:
                            valido = False
                            continue
                    else:       #hay un # al top de la pila, uso todas las L's
                        if (char == '.' and estado == 1) or (ord(char)>ord('/') and ord(char)<ord(':') and estado == 2):
                            for char in self.M.matriz[estado][4][2]:    #apilar
                                pila.apilar(char)
                            print('pila: ' + str(pila.show()))
                            estado = self.M.matriz[estado][4][3]#nuevo estado
                        else:
                            valido = False
                            continue

                else:   #reglas del estado q3 con 2 transiciones
                    if pila.show()[0] == 'N': #hay una N al top de la pila
                        print('Pila: ' + str(pila.show()) + str(estado))
                        if ord('0') <= ord(char) <= ord('9'):
                            pila.desapilar()
                            estado = self.M.matriz[estado][0][3]
                            continue
                        else:
                            valido = False
                            continue
                    else:   #hay un # al top de la pila, uso todas las N's
                        if char == '@':
                            pila.desapilar()
                            print('pila: ' + str(pila.show()))
                            estado = self.M.matriz[estado][1][3]#nuevo estado           

        if valido == False:
            QMessageBox.warning(self,"Invalida","La cadena NO cumple con el formato")
        else:
            QMessageBox.warning(self,"Valida","La cadena cumple con el formato")

    @Slot( )
    def crear(self):
        valido = True  #bandera de aceptacion final
        estado = 0  #definimos es estado inicial
        pila = Pila()   #creamos una pila

        nombre = self.ui.cre_nom_lineEdit.text()
        apellido = self.ui.cre_ape_lineEdit.text()
        cadena = nombre + '.' + apellido + 'V' # V para validar
        print(cadena)

        if self.M.matriz[estado][0][0] == 'lam':    #trato unico para q0
            for char in self.M.matriz[estado][0][2]:    #apilar
                pila.apilar(char)
            print('pila Inicial: ' + str(pila.show()))
            estado = self.M.matriz[estado][0][3]    #nuevo estado

        for char in cadena:     #for que itera sobre los caracteres de la cadena
            print()
            print('Entra: ' + str(char))
            if valido is False:     #si la cadena se descarta para todo
                break
            else:
                print('estado q'+ str(estado) + ':' + str(self.M.matriz[estado]))
                
                if len(self.M.matriz[estado]) == 4:#Reglas para los estdados con 4 transiciones q1 y q2
                    print('Pila: ' + str(pila.show()) + str(estado))
                    if pila.show()[0] == 'P': #hay una P al top de la pila
                        if ord(char)>ord('`') and ord(char)<ord('{'):
                            pila.desapilar()
                            estado = self.M.matriz[estado][0][3]
                            continue
                        else:
                            valido = False
                            continue
                    elif pila.show()[0] == 'L': #hay una L al top de la pila
                        if ord(char)>ord('`') and ord(char)<ord('{'):
                            pila.desapilar()
                            estado = self.M.matriz[estado][1][3]
                            continue
                        elif char == '.' and estado == 1:
                            while pila.show()[0] == 'L':
                                pila.desapilar()
                            for char in self.M.matriz[estado][3][2]:    #apilar
                                pila.apilar(char)
                            print('pila: ' + str(pila.show()))
                            estado = self.M.matriz[estado][3][3]#nuevo estado
                        elif char == 'V' and estado == 2:
                            while pila.show()[0] == 'L':
                                pila.desapilar()
                            num1 = randrange(10)
                            num2 = randrange(10)
                            num3 = randrange(10)
                            num4 = randrange(10)
                            cadena = cadena[:-1] + str(num1) + str(num2) + str(num3) + str(num4) + '@alumnos.udg.mx'
                        else:
                            valido = False
                            continue
                    elif pila.show()[0] == '#': #hay una H al top de la pila 
                        valido = False
                        continue  

        if valido == False:
            QMessageBox.warning(self,"Invalida","Los datos NO cumplen con el formato")
        else:
            QMessageBox.warning(self,"Valida","Tu correro seria: " + cadena)

