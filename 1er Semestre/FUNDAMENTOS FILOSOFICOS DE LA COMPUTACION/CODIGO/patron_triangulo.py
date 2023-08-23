#ARELLANO GRANADOS ANGEL MARIANO
#Este programa imprime un patron de triangulo.
BASE_SIZE = 8

for r in range(BASE_SIZE,-1,-1):
    for c in range(r + 1):
        print('*', end='')
    print()
