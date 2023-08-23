class Arista:
    def __init__(self):
        self.__distancias = []

    #funcion para agregar distacias vacias al arreglo
    def agrega_distancia_vacia(self, lim):
        while len(self.__distancias) <= lim-1:
            self.__distancias.append("-")

    #funcion para agregar distacias al arreglo
    def agrega_distancia(self, final:int,distancia:float):
        self.__distancias[final] = distancia

    #funciones que permite iterar en el objeto arista
    def __iter__(self):
        self.cont = 0
        return self
    def __next__(self):
        if self.cont < len(self.__distancias):
            distancia = self.__distancias[self.cont]
            self.cont += 1
            return distancia
        else:
            raise StopIteration

    @property
    def distancias(self):
        return self.__distancias