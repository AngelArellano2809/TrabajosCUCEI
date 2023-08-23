#Arellano Granados Angel Mariano
#Programa que imprime un mensaje acorde a la puntuacion obtenida en el curso
#Entrada
calif=int(input("Dame tu calificación final: "))
#Selectiva Doble Anidada
if calif >=90:
    print ("EXCELENTE")
else:
    if calif >=80:
        print ("BIEN")
    else:
        if calif >=70:
            print ("REGULAR")
        else:
            if calif >=60:
                print ("ESTUDIA MÁS")
            else:
                print ("SUERTE PARA LA PROXIMA")
