from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id, origen:dict, destino:dict, velocidad,color:dict)->None:
        self.__id = id
        self.__origen = origen
        self.__destino = destino
        self.__velocidad = velocidad
        self.__color = color
        self.__distancia = distancia_euclidiana(origen["x"],destino["x"],origen["y"],destino["y"])

    def __str__(self):
        return(
            "Id: "+ str(self.__id) + "\n"+
            "Origen: ("+ str(self.__origen["x"]) + "," + str(self.__origen["y"]) + ")\n"+
            "Destino: ("+ str(self.__destino["x"]) + "," + str(self.__destino["y"]) + ")\n"+
            "Velocidad: " + str(self.__velocidad) + "\n"+
            "Color: (" + str(self.__color["red"]) + "," + str(self.__color["green"]) + "," + str(self.__color["blue"]) + ")\n"+
            "Distancia: "+ str(self.__distancia) + "\n"
        )
    def to_dict(self):
        return{
            "id":self.__id,
            "origen":{
                "x": self.__origen["x"],
                "y": self.__origen["y"]
            },
            "destino":{
                "x": self.__destino["x"],
                "y": self.__destino["y"]
            },
            "velocidad":self.__velocidad,
            "color":{
                "red":self.__color["red"],
                "green":self.__color["green"],
                "blue":self.__color["blue"]
            }
        }

    @property
    def id(self):
        return self.__id
    @property
    def origen(self):
        return "("+ str(self.__origen["x"]) + "," + str(self.__origen["y"]) + ")"
    @property
    def destino(self):
        return "("+ str(self.__destino["x"]) + "," + str(self.__destino["y"]) + ")"
    @property
    def color(self):
        return "(" + str(self.__color["red"]) + "," + str(self.__color["green"]) + "," + str(self.__color["blue"]) + ")"
    @property
    def origen_x(self):
        return self.__origen["x"]
    @property
    def origen_y(self):
        return self.__origen["y"]
    @property
    def destino_x(self):
        return self.__destino["x"]
    @property
    def destino_y(self):
        return self.__destino["y"]
    @property
    def velocidad(self):
        return self.__velocidad
    @property
    def red(self):
        return self.__color["red"]
    @property
    def green(self):
        return self.__color["green"]
    @property
    def blue(self):
        return self.__color["blue"]
    @property
    def distancia(self):
        return self.__distancia