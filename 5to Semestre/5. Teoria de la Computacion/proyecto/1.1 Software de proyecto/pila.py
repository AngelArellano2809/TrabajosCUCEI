class Pila:
    #Representa una pila con operaciones de apilar, desapilar yverificar si está vacía. 

    def __init__(self):
        #Crea una pila vacía. 
        # La pila vacía se representa con una lista vacía
        self.items = []

    def apilar(self, x):
        #Agrega el elemento x a la pila, Apilar es agregar al final de la lista.
        self.items.insert(0, x)

    def desapilar(self):
        #Devuelve el elemento tope y lo elimina de la pila.Si la pila está vacía levanta una excepción.
        print('POP: ' + str(self.items[0]))
        return self.items.pop(0)

    
    def show(self):
        #Devuelve una cedena con su contenido
        return self.items