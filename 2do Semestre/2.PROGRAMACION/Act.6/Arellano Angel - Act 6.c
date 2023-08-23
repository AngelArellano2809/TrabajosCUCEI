//ARELLANO GRANADOS ANGEL MARIANO
//funciones CON paso de parametros
//CON retorno de valores
#include <stdio.h>
#include <stdlib.h>
//declaración de funciones
float cuadrado(float lado);
float triangulo(float base, float altura);
float rombo(float lado, float altura);
float trapecio(float altura,float base1,float base2);

int main() {
	//variables locales en el main
	int opc;
	float l,b,a,area,b1,b2;
	do
	{
		printf("1.Cuadrado\n2.Triangulo\n3.Rombo\n4.Trapecio\n5.Salir\n");
		printf("Dame una opcion: ");
		scanf("%i",&opc);
		switch (opc)
			{
			case 1:	printf("Lado: ");
					scanf("%f",&l);
					area=cuadrado(l);//llamada a función
					printf("Area es %f \n\n\n",area);
					break;
			case 2:	printf("Base: ");
					scanf("%f",&b);
					printf("Altura: ");
					scanf("%f",&a);
					area=triangulo(b,a);//llamada a función
					printf("Area es %f \n\n\n",area);
					break;
            case 3: printf("Lado: ");
                    scanf("%f",&l);
                    printf("Altura: ");
                    scanf("%f",&a);
                    area=rombo(l,a);
                    printf("Area es %f \n\n\n",area);
                    break;
            case 4: printf("Altura: ");
                    scanf("%f",&a);
                    printf("Base de arriba: ");
                    scanf("%f",&b1);
                    printf("Base de abajo: ");
                    scanf("%f",&b2);
                    area=trapecio(a,b1,b2);
                    printf("Area es %f \n\n\n",area);
                    break;
			case 5:	printf("Gracias \n\n\n");
					break;
			default: printf("Opcion incorrecta \n\n\n");
			}
	}while(opc!=5);
	return 0;
}

float cuadrado(float lado)
{	float a_cuadrado;//variable local
	a_cuadrado=lado*lado;
	return a_cuadrado;}//el return devuelve el resultado

float triangulo(float base, float altura)
{	float a_triangulo;//variable local
	a_triangulo=base*altura/2;
	return a_triangulo;}//el return devuelve el resultado

float rombo(float lado, float altura)
{   float a_rombo;
    a_rombo=lado*altura;
    return a_rombo;}

float trapecio(float altura,float base1,float base2)
{   float a_trapecio;
    a_trapecio=altura*((base1+base2)/2);
    return a_trapecio;}
