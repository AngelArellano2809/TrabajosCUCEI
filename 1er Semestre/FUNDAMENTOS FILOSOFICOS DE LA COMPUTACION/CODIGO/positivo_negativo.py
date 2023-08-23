#ARELLANO GRANADOS ANGEL MARIANO
# PROGRAMA PARA CONTAR EL NUMERO DE NÚMEROS POSITIVOS Y NEGATIVOS INSERTADOS
posi=nega=0
#ENTRDA
num=int(input("Dame un número, o CERO para salir: "))
#Estructura de control repetitiva
while num != 0:
    if num > 0:
       posi = posi + 1
    elif num < 0:
        nega = nega + 1
    num=int(input("Dame un número, o CERO para salir: "))
print("Total de números positivos: ", posi,
      "\nTotal de números negativos: ", nega)
