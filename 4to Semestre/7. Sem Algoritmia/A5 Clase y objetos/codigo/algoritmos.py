import math 

def distancia_euclidiana(x_1,x_2,y_1,y_2) -> float:
    distancia:float = math.sqrt(((x_2-x_1)**2)+((y_1-y_2)**2))
    #print(distancia)
    return distancia
