from asyncore import write
#from vuelo import Vuelo
import json

from vuelo import Vuelo

class Aeropuerto:
    def __init__(self):
        self.__vuelos = []

    def agrega_final(self,vuelo:Vuelo):
        self.__vuelos.append(vuelo)

    def agrega_inicio (self,vuelo:Vuelo):
        self.__vuelos.insert(0,vuelo)

    def mostrar(self):
        for v in self.__vuelos:
            print(v)
    
    def __str__(self) -> str:
        return"".join(
            str(v) + "\n" for v in self.__vuelos #programacion Funcional
        )

    def abrir(self, ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista = json.load(archivo)
                self.__vuelos = [Vuelo(**vuelo) for vuelo in lista]
            return 1
        except:
            return 0

    def guardar (self, ubicacion):
        try:
            with open(ubicacion,'w') as archivo:
                lista = [vuelo.to_dict() for vuelo in self.__vuelos]
                print(lista)
                json.dump(lista,archivo,indent=5)
            return 1
            #archivo.write(str(self))
        except:
            return 0

'''v01 = Vuelo(id="0",origen="GDL",destino="MTY",peso=20)
v02 = Vuelo(id="2",origen="CDMX",destino="GDL",peso=30)
aeropuerto = Aeropuerto()
aeropuerto.agrega_final(v01)
aeropuerto.agrega_inicio(v02)
aeropuerto.mostrar()'''