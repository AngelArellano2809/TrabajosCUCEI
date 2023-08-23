#Equipo No.1
#Arellano Granados Angel Mariano
#Programa para calcular el promedio de 5 calificaciones
calif=prom=acum=0.0
cont=1#inicializando variable de control
#ciclo while
while cont<=5:#condicion
    #Entrada
    calif=float(input("Dame una calificación: "))
    acum=acum+calif
    cont=cont+1 #incremento de la variable de control
#calculamos el promedio
prom=acum/(cont-1)
#Salida
print("El promedio es: ",prom)
