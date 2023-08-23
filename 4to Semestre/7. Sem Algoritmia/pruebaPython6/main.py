from random import randint

numeros = []

for i in range(100):
    numeros.append(randint(0,1000))

print(numeros)

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)
