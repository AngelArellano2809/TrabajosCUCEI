class Nodo():
    def __init__(self, id=0,real=0, tipo='',peso=0):
        self.__id = id
        self.__real = real
        self.__tipo = tipo
        self.__peso = peso
        self.visitado = False
    
    def __str__(self):
        return(
            "ID: "+ str(self.__id) + "\n"+
            "Real: "+ str(self.__real) + "\n"+
            "Tipo: "+ str(self.__tipo) + "\n"+
            "Peso: "+ str(self.__peso) + "\n"
        )
    
    def to_dict(self):
        return{
            "id": self.id,
            "real": self.real,
            "tipo": self.tipo,
            "peso": self.peso
        }
    
    def incPeso(self):
        self.__peso+=1


    @property
    def id(self):
        return self.__id
    
    @property
    def real(self):
        return self.__real
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def peso(self):
        return self.__peso