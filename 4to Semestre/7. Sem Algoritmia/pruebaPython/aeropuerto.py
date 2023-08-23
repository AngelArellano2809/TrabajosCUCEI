class Aeropuerto:
    def __init__(self) -> None:
        self.__lista = []
    
    def agregar (self, vuelo):
        self.__lista.append(vuelo)
    
    def mostrar (self):
        for vuelo in self.__lista:
            vuelo.imprimir()