#Arellano Granados Angel Mariano
#Programa para obtener la tabla de multiplicar de cualquier 
#número con cualquier limite inicial y final.
num=lim_inf=lim_sup=0
num=int(input("Teclea el num de la tabla: "))
lim_inf=int(input("Dame el límite inferior: "))
lim_sup=int(input("Dame el límite superior: "))
print(num,"*",lim_inf,"=",num*lim_inf)
#ciclo while
while lim_inf<=lim_sup-1:#condicion
    lim_inf= lim_inf + 1
    print(num,"*",lim_inf,"=",num*lim_inf)
