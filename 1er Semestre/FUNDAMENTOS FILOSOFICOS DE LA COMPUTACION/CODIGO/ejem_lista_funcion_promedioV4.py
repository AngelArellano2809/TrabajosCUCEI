#ARELLANO GARNADOS ANGEL MARIANO
#Programa que guarda 5 calificaciones en una lista,
#y en unca funcion calcula en promedio y lo devolvera.
import random
def main():
    califs=llenar_lista_usuario()
    edades=llenar_lista_aleatoriamente()
    #Punto de inspección (Imprimir la lista de calificaciones)
    print('Las calificaciones son: ',califs)
    print(edades)
        
    p = calcular_promedio(califs) 
    print('El promedio es: ',format(p,'.2f'))

def calcular_promedio(califs):
    indice=acum=p=0 #tres variables iniciadas en 0
    while indice < len(califs):
        acum= acum + califs[indice]
        indice += 1

    p=acum/indice
    return p

def llenar_lista_usuario():
    indice=0
    materias=int(input('¿Cuantas calificaciones se van a promediar? '))
    #Tamaño de lista depende del valor variable materias
    lista_califs=[0.0]*materias
    while indice < len(lista_califs):
        lista_califs[indice]=float(input('Dame una calificación: '))
        indice += 1
    return lista_califs#Regresamos la lista llena de calificaciones

def llenar_lista_aleatoriamente():
    indice=0
    cant_e=int(input('¿Cuantas edades vamos a procesar? '))
    #Tamaño de lista depende del valor variable edades
    lista_edades=[0]*cant_e
    while indice < cant_e:
        lista_edades[indice]=random.randint(1,100)
        indice += 1
    return lista_edades#Regresamos la lista llena de edades aleatorias

#llamada al main
main()
