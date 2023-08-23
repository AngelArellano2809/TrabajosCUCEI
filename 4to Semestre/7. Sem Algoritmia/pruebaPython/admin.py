from aeropuerto import Aeropuerto
from avion import Vuelo

ae = Aeropuerto()

while True:
    print("1) agregar")
    print("2) mostrar")
    print("0) salir")
    op = input()

    if (op == "1"):
        id = input("ID: ")
        origen = input("origen: ")
        destino = input("destino: ")
        peso = float(input("peso: "))

        vuelo = Vuelo(id, origen, destino, peso)

        ae.agregar(vuelo)
    
    elif(op == "2"):
        ae.mostrar()
    elif (op == "0"):
        break
    