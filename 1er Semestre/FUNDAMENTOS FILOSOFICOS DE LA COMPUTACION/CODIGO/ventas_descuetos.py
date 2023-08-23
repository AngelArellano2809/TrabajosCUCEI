#Arellano Granados Angel Mariano
#Programa qpara calcular que descuento tendrá una compra y el total a pagar
#Entrada
num=int(input("Teclea la cantidad de productos comprados: "))
#Selectiva Doble Anidada
if num >=10 and num <=19:
    print ("Tu descuento es de 20% y pagaras $",num*99*0.8)
elif num >=20 and num <=49:
    print ("Tu descuento es de 30% y pagaras $",num*99*0.7)
elif num >=50 and num <=99:
    print ("Tu descuento es de 40% y pagaras $",num*99*0.6)
else:
    print ("La cantidad esta fuera de la promoción")
