//Arellano Granados Angel Mariano
//Programa que calcula el Volumen de un Prisma Triangular
//Formula del prisma: Ab x h
//Formula del triangulo: (b x h)/2

#include <stdio.h>
#include <stdlib.h>

int main(){
    printf("CALCULARDOR DEL VOLUMEN DE UN PRISMA TRIANGULAR\n");
    printf("\n");//arreglo visual
    float base, altura_t, area, altura_p, volumen;
	printf("Dame la base del triangulo: ");
	scanf("%f",&base);
	printf("Dame la altura del triangulo: ");
	scanf("%f",&altura_t);
	area=base*altura_t/2.0;
	printf("El area del triangulo es: %f ",area);
	printf("\n");//arreglo visual
	printf("\nDame la altura del prisma: ");
	scanf("%f",&altura_p);
	volumen=area*altura_p;
    printf("El volumen del prisma es: %f ",volumen);
    printf("\n");//arreglo visual
    return 0;
}
