from random import randint

class Automovil:
    def __init__(self) -> None:
        self.placas = ""
        self.modelo = 0
        self.marca = ""
        self.km = 0
    def __str__(self) -> str:
        return "{0:6} {1:4} {2:6} {3:4}".format(self.placas,self.modelo,self.marca,self.km)
    def __lt__(self,other):
        return self.placas < other.placas


marcas = ["Audi","VM","BMW","Toyota","Nissan"]
placas = ["ABC","JVC","HGY","TAL","OLP","WAN","UTO","UDG"] 

autos = []

for i in range(10):
    auto = Automovil()
    auto.placas = placas[randint(0,len(placas)-1)]\
        + str(randint(100,999))
    auto.modelo = randint(2000,2023)
    auto.marca = marcas[randint(0,len(marcas)-1)]
    auto.km = randint(0,1000)

    autos.append(auto)

def sort_by_modelo(auto):
    return auto.modelo

autos.sort()
print('\n')

for auto in autos:
    print(auto)

autos.sort(reverse=True)
print('\n')

for auto in autos:
    print(auto)

autos.sort(key=sort_by_modelo)
print('\n')

for auto in autos:
    print(auto)

autos.sort(key=sort_by_modelo, reverse=True)
print('\n')

for auto in autos:
    print(auto)

autos.sort(key=lambda auto: auto.marca)
print('\n')

for auto in autos:
    print(auto)

autos.sort(key=lambda auto: auto.marca,reverse=True)
print('\n')

for auto in autos:
    print(auto)

autos.sort(key=lambda auto: auto.km)
print('\n')

for auto in autos:
    print(auto)