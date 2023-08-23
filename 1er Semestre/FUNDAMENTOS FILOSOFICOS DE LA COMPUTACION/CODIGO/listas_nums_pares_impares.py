#Arellano Granados Angel Mariano
#Programa para generar dos listas con limites elejidos por el usuario
#una de pares y otra de nones
#ENTRADA DE DATOS
lim_par = int(input("Dame el límite para los números pares: "))
lim_non = int(input("Dame el límite para los números nones: "))
#Ciclo for pares
for num in range (1, lim_par +1):
    if num %2==0:
        print(num,end="  ")
print( )
#Ciclo for nones
for num in range (1, lim_non +1):
    if num %2!=0:
        print(num,end="  ")
