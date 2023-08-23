class Vuelo:
    def __init__(self, id="", origen="", destino="",peso=0):
        self.__id = id
        self.__origen = origen
        self.__destino = destino
        self.__peso = peso
    def __str__(self):
        return(
            "Identificador: "+ self.__id + "\n"+
            "origen: " + self.__origen + "\n"+
            "Destino: " + self.__destino + "\n"+
            "Peso: " + str(self.__peso) + "\n"
        )

# v01 = Vuelo(id="0",origen="GDL",destino="MTY",peso=20)
# print(v01)

# v02 = Vuelo(id="2",origen="CDMX",destino="GDL",peso=30)
# print(v02)