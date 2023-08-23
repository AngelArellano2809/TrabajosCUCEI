archivo = open("CarRadio",'r')
char = archivo.read(1)
cont = 1
while (char != ""):
    temp = ord(char)
    if (temp >= 97 and temp <= 122):
        if(temp == 122):
            print('a', end ="")
        else:
            temp = chr(ord(char)+1)
            print(temp, end ="")
    else:
        print(char, end ="")
    cont+=1
    char = archivo.read(1)
archivo.close()