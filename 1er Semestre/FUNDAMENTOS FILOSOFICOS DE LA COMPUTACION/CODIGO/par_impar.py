#Equipo 1:
#Arellano Granados Angel Mariano
#Barrera Alejo Maria Galilea
#Cervantes Zavala Joahan Siddharta
#Correa Navarro Brandon Misael
#Sección D13 Calendario 2021A
#Programa para identificar si un número es par o impar
#ENTRADA DE DATOS
num = int(input("Dame un número: "))
#PROCESO
residuo = num % 2
print (num," % 2 =", residuo)
#Estructura de control selectiva doble o compuesta
if residuo == 0:
    print("Se trata de un número PAR")
else:
    print("Se trata de un número IMPAR")
