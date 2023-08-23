#estructura
if True:
    print ("Es verdadero")
elif False:
   print ("No es verdadero")
else:
    print ("Es falso")

#ejemplo 1
numero = int(input("Edad: "))
if numero % 2 == 0:
    print(numero, " es par")
else:
    print(numero, " es impar")

#ejemplo 2
temperatura = int(input("Temperatura: "))
if temperatura <=0:
    print(temperatura, " esta frio")
elif temperatura > 0 and temperatura <= 12:
    print(temperatura, " esta fresco")
elif temperatura < 18:
    print(temperatura, " es agradable")
else:
    print(temperatura, " esta calido")