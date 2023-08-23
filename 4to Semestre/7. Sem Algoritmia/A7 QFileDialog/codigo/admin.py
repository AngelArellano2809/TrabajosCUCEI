from particula import Particula
import json

class Admin:
    def __init__(self):
        self.__particulas = []

    def agrega_final(self,particula:Particula):
        self.__particulas.append(particula)

    def agrega_inicio (self,particula:Particula):
        self.__particulas.insert(0,particula)

    def mostrar(self):
        for v in self.__particulas:
            print(v)
    
    def __str__(self) -> str:
        return"".join(
            str(v) + "\n" for v in self.__particulas
        )

    def abrir(self, ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

    def guardar (self, ubicacion):
        try:
            with open(ubicacion,'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista,archivo,indent=5)
            return 1
        except:
            return 0