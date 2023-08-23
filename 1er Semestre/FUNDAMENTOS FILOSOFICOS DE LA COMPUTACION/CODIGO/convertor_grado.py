#Arellano Granados Angel Mariano
#Programa para convertir grados C° a F°
#Entrada:
def main ():
    cel= float(input('Tecla los grados C° a convertir: '))
    convertidor_grado(cel)

def convertidor_grado (cantidad):
	fah = (cantidad * (9/5))+32
	print('La conversión son',fah,'F°')

main()
