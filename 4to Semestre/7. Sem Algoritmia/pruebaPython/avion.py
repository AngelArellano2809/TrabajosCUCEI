#definir una clase
class Vuelo:
    """def __init__(self) -> None:#contructor de clase
        self._id = ''#_protected
        self.__origen = ''#__private
        self.destino = ''
        self.peso = 0.0
        #pass para que el constructor este vacio"""
    def __init__(self,id,origen,destino,peso) -> None:#contructor de clase
        self._id = id #_protected
        self.__origen = origen#__private
        self.destino = destino
        self.peso = peso
    
    def imprimir(self)-> None:
        print("ID: ",self._id)
        print("origen: ",self.__origen)
        print("destino: ",self.destino)
        print("peso: ",self.peso)