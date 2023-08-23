class Arista:
    def __init__(self, pesos=[]):
        #self.__distancias = []
        #self.__distancias = [distancia for distancia in distancias]
        self.__pesos = list(pesos)


    #funcion para agregar distacias vacias al arreglo
    def agrega_distancia_vacia(self, lim):
        while len(self.__pesos) <= lim-1:
            self.__pesos.append(0)

    #funcion para agregar distacias al arreglo
    def agrega_distancia(self, final:int):
        self.__pesos[final] += 1

    #funciones que permite iterar en el objeto arista
    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__pesos):
            peso = self.__pesos[self.cont]
            self.cont += 1
            return peso
        else:
            raise StopIteration

    def to_dict(self):
        return{
            "pesos": self.pesos
        }

    @property
    def pesos(self):
        return self.__pesos