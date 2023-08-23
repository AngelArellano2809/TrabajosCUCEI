AO = open("Agenda",'r')
AR = open("AuxAg",'w')
for linea in AO:
    AR.write(linea)
AO.close()
AR.close()

AO = open("Agenda",'w')
AR = open("AuxAg",'r')
for linea in AR:
    AO.write(linea)
nombre = input("Dame el nombre del estudiante: ")
codigo = input("Dame el codigo del estudiante: ")
carrera = input("Dame la carrera del estudiante: ")
cadena = nombre + '|' + codigo + '|' + carrera + '\n'
AO.write(cadena)
AO.close()
AR.close()