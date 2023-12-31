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
    
    def __len__(self):
        return(
            len(self.__particulas)
        )

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration