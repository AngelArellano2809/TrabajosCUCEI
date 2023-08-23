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

v01 = Vuelo(id="0",origen="GDL",destino="MTY",peso=20)
v02 = Vuelo(id="2",origen="CDMX",destino="GDL",peso=30)
aeropuerto = Aeropuerto()
aeropuerto.agrega_final(v01)
aeropuerto.agrega_inicio(v02)
aeropuerto.mostrar()