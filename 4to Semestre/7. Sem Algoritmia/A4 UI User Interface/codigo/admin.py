from particula import Particula

class Admin:
    def __init__(self):
        self.__particulas = []

    def agrega_final(self,particula:Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for v in self.__particulas:
            print(v)
    
    def __str__(self) -> str:
        return"".join(
            str(v) + "\n" for v in self.__particulas
        )