class Particula:
    def __init__(self, destino_x="", destino_y="", velocidad="",red=0,green=0,blue=0):
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue

    def __str__(self):
        return(
            "Destino x: "+ str(self.__destino_x) + "\n"+
            "Destino y: " + str(self.__destino_y) + "\n"+
            "Velocidad: " + str(self.__velocidad) + "\n"+
            "Red: " + str(self.__red) + "\n"+
            "Green: " + str(self.__green) + "\n"+
            "Blue: " + str(self.__blue) + "\n"
        )