AO = open("carRadio",'r')
AC = open("carRadio_C",'w')
AD = open("carRadio_D",'w')

#Codificar Archivo original
char = AO.read(1)
cont = 1
while (char != ""):
    temp = ord(char)
    if (temp >= 97 and temp <= 122):
        if(temp == 122):
            AC.write("a")
        else:
            temp = chr(ord(char)+1)
            AC.write(str(temp))
    else:
        AC.write(char)
    cont+=1
    char = AO.read(1)
AC.close()

#Decodificar Archivo Codificado
AC = open("carRadio_C",'r')
char = AC.read(1)
cont = 1
while (char != ""):
    temp = ord(char)
    if (temp >= 97 and temp <= 122):
        if(temp == 97):
            AD.write("z")
        else:
            temp = chr(ord(char)-1)
            AD.write(str(temp))
    else:
        AD.write(char)
    cont+=1
    char = AC.read(1)

AO.close()
AC.close()
AD.close()