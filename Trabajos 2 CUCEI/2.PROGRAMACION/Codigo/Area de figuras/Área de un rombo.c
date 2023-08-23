//Nombre: Angel Mariano Arellano Granados
//Fecha: 23 de agosto de 2021
//Descripcion: Calcula el area de un triangulo
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	//Declaracion de variables
	//Utiliza el tipo de dato flotante: float, que es para
	//utilizar números con punto decimal
	float diagonal_1, diagonal_2, area;
	printf("Dame la diagonal 1: ");
	 //el %f es para indicar la captura de un número flotante
	scanf("%f",&diagonal_1);
	printf("Dame la diagonal 2: ");
	scanf("%f",&diagonal_2);
	area=(diagonal_1*diagonal_2)/2.0;
	//imprime los resultados
	//el %f indica que se imprime en pantalla un número flotante
	printf("El area es: %f ",area);
	return 0;
}
