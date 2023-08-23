import json

d = dict()

while (True):
    print('1) Agregar llave y valor')
    print('2) Saca un value')
    print('3) Mostrar Keys')
    print('4) Mostrar Key - value')
    print('5) Eliminar Key')
    print('6) Vaciar')#vaciar diccionario
    print('7) Mostrar valores')
    print('8) respaldar')
    print('9) recuperar')
    print('0) slair')
    op = input('<')#espera respuesta

    if op=='1':
        key = input('key: ')
        value = int(input('Value: '))
        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]

    elif op == '2':
        key = input('key: ')
        if key in d:
            print(d[key])
        else:
            print(f'{key} no existe')

    elif op == '3':
        for key in d.keys():
            print(key)
    
    elif op == '4':
        for key, value in d.items():
            print(key,value)

    elif op == '5':
        key = input('key: ')
        if key in d:
            d.pop(key)#del d[key]
        else:
            print(f'{key} no existe')
    
    elif op == '6':
        d.clear()
    
    elif op == '7':
        for value in d.values():
            print(value)
    
    elif op == '8':
        with open('dict.json','w') as file:
            json.dump(d,file,indent = 5)
    
    elif op == '9':
        with open('dict.json','r') as file:
            d = json.load(file)

    elif op == '0':
        break

