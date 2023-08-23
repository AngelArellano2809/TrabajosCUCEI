#ARELLANO GARNADOS ANGEL MARIANO
#Programa que guarda 5 calificaciones en una lista,
#y en unca funcion calcula en promedio y lo devolvera.

def main():
    califs = [76.5,86.5,99.5,63.5,98.5] #lista 5 elementos
    p = calcular_promedio(califs) 
    print('El promedio es: ',p)

def calcular_promedio(califs):
    indice=acum=p=0 #tres variables iniciadas en 0
    while indice < len(califs):
        acum= acum + califs[indice]
        indice += 1

    p=acum/indice
    return p

#llamada al main
main()
