class Nodo:
    def __init__(self, id=0, nombre='', origen_x=0, origen_y=0):
        self.__id = id
        self.__nombre = nombre
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        #aributos para aplicar el metodo dijkstra
        self.visitado = False
        self.padre = None
        self.distancia = float('inf')
    
    def __str__(self):
        return(
            "ID: "+ str(self.__id) + "\n"+
            "Distancia: "+ str(self.__nombre) + "\n"+
            "Origen x: "+ str(self.__origen_x) + "\n"+
            "Origen y: "+ str(self.__origen_y) + "\n"
        )
    
    def to_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "origen_x": self.origen_x,
            "origen_y": self.origen_y
        }

    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre
    @property
    def origen_x(self):
        return self.__origen_x
    @property
    def origen_y(self):
        return self.__origen_y