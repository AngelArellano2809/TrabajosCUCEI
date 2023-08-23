#Equipo No.1
#Arellano Granados Angel Mariano
#Programa para calcular el promedio de N calificaciones
#Inicializamos las variables
calif=acum=0.0
cont=0
#Entrada
calif=float(input("Teclea una calificacion o -1.0 para salir: "))
#ciclo while
while calif!= -1:
    acum=acum+calif
    cont=cont+1
    #entrda
    calif=float(input("Teclea una calificacion o -1.0 para salir: "))
if cont!=0:
    print("El promedio es: ",acum/cont)
else:
    print("No se introdujeron calificaciones")
