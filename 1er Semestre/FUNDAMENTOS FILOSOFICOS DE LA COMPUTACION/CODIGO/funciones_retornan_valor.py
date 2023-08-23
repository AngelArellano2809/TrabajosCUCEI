#Equipo 1:
#Arellano Granados Angel Mariano
#Barrera Alejo Maria Galilea
#Cervantes Zavala Joahan Siddharta
#Correa Navarro Brandon Misael
#Sección D13, Calendario 2021A
#Algoritmo para comprar la estación del año en la que nació
#el usuario segun el mes en el que nació.

def main():
    month= int(input('Dame tu mes (numero) de nacimiento: '))
    season = get_season (month)
    print ('Naciste en la temporada de', season)
    
def get_season(month):
    if month in (12,1,2):
        right_season=('Invierno')
    elif month in (3,4,5):
        right_season=('Primavera')
    elif month in (6,7,8):
        right_season =('Verano')
    elif month in (9,10,11):
        right_season=('Otoño')
    return right_season
    
main()
