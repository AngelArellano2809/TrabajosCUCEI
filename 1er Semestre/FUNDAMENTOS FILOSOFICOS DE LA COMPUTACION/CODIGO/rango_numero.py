#Arellano Granados Angel Mariano
#Programa para determinar si un número se encuentra en un rango
#Entrada
num=int(input("Dame un número entre 1 y 1000: "))
#Selectiva Doble Anidada
if num >=1 and num <=10:
    print ("El número", num, "se encuentra entre 1 y 10")
elif num >=11 and num <=100:
    print ("El número", num, "se encuentra entre 11 y 100")
elif num >=101 and num <=1000:
    print ("El número", num, "se encuentra entre 101 y 1000")
else:
    print ("El número", num, "está fuera de los rangos")
