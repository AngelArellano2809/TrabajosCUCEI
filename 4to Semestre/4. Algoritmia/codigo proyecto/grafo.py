from nodo import Nodo
from arista import Arista

class Grafo:
    #inicializador de los objetos
    def __init__(self):
        self.__vertices = []
        self.__artistas =[]
    
    #funcion para agregar nodos al arreglo
    def agrega_nodo(self,nodo:Nodo):
        self.__vertices.append(nodo)

    #funcion para rellenar la tabla de ayacencia con NULL
    def rellenar (self):
        for arista in self.__artistas:
            arista.agrega_distancia_vacia(len(self.__vertices))
    
    #funcion para agregar aristas al arreglo
    def agrega_aristas_vacia(self):
        self.__artistas.append(Arista())
        self.rellenar()

    def agrega_arista(self,inicio:int ,final:int ,distancia:float):
        self.__artistas[inicio].agrega_distancia(final,distancia)

    #funcion para mostrar los registros como cadenas
    def __str__(self) -> str:
        return"".join(
            str(i) + "\n" for i in self.__vertices
        )
    
    #funcion que retorna el numero de noodos registrados
    def __len__(self):
        return(
            len(self.__vertices)
        )
    
    #funciones que permite iterar en el objeto grafo
    def __iter__(self):
        self.cont = 0
        return self
    def __next__(self):
        if self.cont < len(self.__artistas):
            arista = self.__artistas[self.cont]
            self.cont += 1
            return arista
        else:
            raise StopIteration
    
    @property
    def vertices(self):
        return self.__vertices
    
    @property
    def artistas(self):
        return self.__artistas
