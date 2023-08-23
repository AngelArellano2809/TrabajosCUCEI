def agregar():
    Archivo = open("Agenda",'a')
    nombre = input("Dame el nombre del estudiante: ")
    codigo = input("Dame el codigo del estudiante: ")
    carrera = input("Dame la carrera del estudiante: ")
    cadena = nombre + '|' + codigo + '|' + carrera + '\n'
    Archivo.write(cadena)
    Archivo.close()
    return

def buscar(cad):
    AO = open("Agenda",'r')
    AR = open("AuxAg", 'w')
    encon = False
    for line in AO:
        if cad in line:
            print(line)
            print("ENCONTRADO:\n"
                  "1) Editar\n"
                  "2) Eliminar\n"
                  "3) Siguiente\n"
                  "0) Salir")
            opc3 = int(input("Selecciona una opcion: "))
            if opc3 == 0:
                return
            elif opc3 == 1:
                nombre = input("Dame el nombre nuevo del estudiante: ")
                codigo = input("Dame el codigo nuevo del estudiante: ")
                carrera = input("Dame la carrera nueva del estudiante: ")
                cadena = nombre + '|' + codigo + '|' + carrera + '\n'
                AR.write(cadena)
                encon = True
            elif opc3 == 2:
                encon = True
        else:
            AR.write(line)
    AO.close()
    AR.close()
    if encon == True:
        AO = open("Agenda", 'w')
        AR = open("AuxAg", 'r')
        for linea in AR:
            AO.write(linea)
        AO.close()
        AR.close()
    elif encon == False:
        print("NO ENCONTRADO")
        return

opc = 1
while opc:
    print("\tMENU\n"
          "1) Agregar un alumno\n"
          "2) Buscar un alumno\n"
          "0) Salir")
    opc = int(input("Selecciona una opcion: "))

    if opc == 1:
        agregar()
    elif opc == 2:
        print("Metodo de busqueda:\n"
              "1) Por Nombre\n"
              "2) Por Codigo")
        opc2 = int(input("Selecciona una opcion: "))
        if opc2 == 1:
            cad = input("Nombre a buscar: ")
            buscar(cad)
        elif opc2 == 2:
            cad = input("Codigo a buscar: ")
            buscar(cad)


"""AO = open("Agenda",'r')
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
AR.close()"""