#Arellano Granados Angel Mariano
#Algoritmo para mostrar la sumatoria de números con un límite elegido por el usuario.
#iniciando variables
suma=0
#Entrada:
lim = int(input('Dame un número entero (limite): '))
#Estructura de control repetitiva
for num in range (1, lim):
    print(num,'+',end="  ")

print(lim,end="  ")

for num in range (1, lim +1):
    suma += num
#Salida
print('=',suma)
