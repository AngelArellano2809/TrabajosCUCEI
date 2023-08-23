#Equipo 1:
#Arellano Granados Angel Mariano
#Barrera Alejo Maria Galilea
#Cervantes Zavala Joahan Siddharta
#Correa Navarro Brandon Misael
#Sección D13, Calendario 2021A
#Programa que muestra un menu donde cada opcion
#ejecuta una tarea diferente.
import random

#funcion principal donde se realizan las llamadas
def main():
    opc=0
    while opc !=6:
        #Imprimir la intefaz al usuario
        print('''MENÚ - LISTAS
        1. Llenar lista usuario (calificaciones)
        2. Calcular promedio lista usuario
        3. Llenar lista aleatoriamente (edades)
        4. Determinar la persona de menor edad
        5. Determinar la persona de mayor edad
        6. Salir''')
        opc=int(input('Elige tu opción: '))
        #El programa ejecutara una tarea segun la opción
        #elejida por el usuario
        if opc ==1:
            califs=llenar_lista_usuario()
            print('Las calificaciones son: ',califs)
        elif opc == 2:
            p = calcular_promedio(califs)
            print('El promedio es: ',format(p,'.2f'))
        elif opc == 3:
            edades=llenar_lista_aleatoriamente()
            print('Las edades son: ',edades)
        elif opc == 4:
            print('La persona mas joven tiene: '
                  ,determinar_menor(edades))
        elif opc == 5:
            print('La persona mas adulta tiene: '
                  ,determinar_mayor(edades))
        elif opc == 6:
            print('Gracias por usar este software')

#Funciones
#Funcion que permite llenar al usuario una lista de calificaciones
def llenar_lista_usuario():
    indice=0
    materias=int(input('¿Cuantas calificaciones se van a promediar? '))
    #Tamaño de lista depende del valor variable materias
    lista_califs=[0.0]*materias
    while indice < len(lista_califs):
        lista_califs[indice]=float(input('Dame una calificación: '))
        indice += 1
    return lista_califs#Regresamos la lista llena de calificaciones

#Funcion que recibe una lista, calcula el promedio
def calcular_promedio(califs):
    indice=acum=p=0 #tres variables iniciadas en 0
    while indice < len(califs):
        acum= acum + califs[indice]
        indice += 1
    p=acum/indice
    return p

#Funcion que genera una lista de edades aleatorias
def llenar_lista_aleatoriamente():
    indice=0
    edades=int(input('¿Cuantas edades vamos a procesar? '))
    #Tamaño de lista depende del valor variable edades
    lista_edades=[0]*edades
    while indice < edades:
        lista_edades[indice]=random.randint(1,100)
        indice += 1
    return lista_edades#Regresamos la lista llena de edades aleatorias

#Funcion que determina el valor mas pequeño de la lista
def determinar_menor(edades):
    menor=min(edades)
    return menor

#Funcion que determina el valor mas grande de la lista
def determinar_mayor(edades):
    mayor=max(edades)
    return mayor

#llamada al main
main()
