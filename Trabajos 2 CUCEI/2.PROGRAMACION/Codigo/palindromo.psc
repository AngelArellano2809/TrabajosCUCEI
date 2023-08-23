//Elaborar un algoritmo en pseudocódigo, para analizar una frase, letra por letra y determinar si es un palíndromo
Algoritmo palíndromo
	Definir  frase como cadena;
	Escribir "Escrive tu palíndromo sin espacios para comprobar:"
	leer frase;	
	j=Longitud(frase)
	acum=0
	Para i<-1 Hasta Longitud(frase) Con Paso 1 Hacer
		Si (subcadena(frase,i,i)=Subcadena(frase,j,j)) Entonces
			acum=acum+1
		Fin Si
		j=j-1
		Escribir acum
	Fin Para
	Si acum=Longitud(frase) Entonces
		Escribir "es un palindromo"
	SiNo
		Escribir "no es un palindromo"
	Fin Si
FinAlgoritmo
