import threading
import numpy as np

# Solicitar al usuario que ingrese los valores de la matriz
print("Ingrese los valores de la matriz 4x4:")
matriz = []
for i in range(4):
    fila = []
    for j in range(4):
        valor = input(f"Valor en la fila {i+1}, columna {j+1}: ")
        fila.append(valor)
    matriz.append(fila)

# Valor por el cual multiplicar la matriz (ejemplo: 2)
valor_multiplicacion = 2

# Matriz resultante (inicialmente llena de ceros)
matriz_resultante = np.zeros_like(matriz)

# Función para multiplicar una porción de la matriz
def multiplicar_por_valor(inicio_fila, fin_fila):
    try:
        for i in range(inicio_fila, fin_fila):
            for j in range(4):
                matriz_resultante[i][j] = int(matriz[i][j]) * valor_multiplicacion
    except:
        print('Uno de los modulos a fallado')

# Crear dos hilos para multiplicar por valor en paralelo
thread1 = threading.Thread(target=multiplicar_por_valor, args=(0, 2))
thread2 = threading.Thread(target=multiplicar_por_valor, args=(2, 4))

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que todos los hilos terminen
thread1.join()
thread2.join()

# Imprimir la matriz original y la matriz resultante
print("\nMatriz original:")
for fila in matriz:
    print(fila)
print("\nMatriz resultante:")
for fila in matriz_resultante:
    print(fila)