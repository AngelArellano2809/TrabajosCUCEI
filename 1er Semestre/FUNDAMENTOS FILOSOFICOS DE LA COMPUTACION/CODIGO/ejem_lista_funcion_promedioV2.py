#ARELLANO GARNADOS ANGEL MARIANO
#Programa que guarda 5 calificaciones en una lista,
#y en unca funcion calcula en promedio y lo devolvera.

def main():
    materias=int(input('¿Cuantas calificaciones se van a promediar? '))
    califs=[0.0]*materias #lista vacia con m elementos
    indice=0
    while indice < len(califs):
        califs[indice]=float(input('Dame una calificación: '))
        indice += 1
        
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
