//Nombre: Angel Mariano Arellano Granados
//Fecha: 23 de agosto de 2021
//Descripcion: Calcula el area de un triangulo
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	//Declaracion de variables
	//Utiliza el tipo de dato flotante: float, que es para
	//utilizar números con punto decimal
	float base, altura, area;
	printf("Dame la base: ");
	 //el %f es para indicar la captura de un número flotante
	scanf("%f",&base);
	printf("Dame la altura: ");
	scanf("%f",&altura);
	area=base*altura;
	//imprime los resultados
	//el %f indica que se imprime en pantalla un número flotante
	printf("El area es: %f ",area);
	return 0;
}
