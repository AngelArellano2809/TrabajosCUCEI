//Nombre: Angel Mariano Arellano Granados
//Fecha: 23 de agosto de 2021
//Descripcion: Calcula el area de un circulo
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]) {
	float radio, pi, area;
	printf("Dame el radio: \n");
	scanf("%f",&radio);
	pi = 3.1416;
	area = pi*pow(radio,2);
	printf("El area es: %.2f ",area);
	return 0;
}
