//ARELLANO GRANADOS ANGEL MARIANO
//programa que solicite las medidas de los lados de un triangulo y
//determine el tipo de triángulo correspondiente, indique cual de sus lados es el mayor
//y por ultimo, despliegue las medidas en orden ascendente
#include <stdio.h>
#include <stdlib.h>

int main(){
    int lado1,lado2,lado3;
    printf("Dame el primer lado del triangulo: \n");
    scanf("%i",&lado1);
    printf("Dame el segundo lado del triangulo: \n");
    scanf("%i",&lado2);
    printf("Dame el tercer lado del triangulo: \n");
    scanf("%i",&lado3);

    if(lado1==lado2 && lado1==lado3 && lado2==lado3){
        printf("El triangulo es ESQUILATERO\n");
    }
    else if(lado1==lado2 || lado1==lado3 || lado2==lado3){
        printf("El triangulo es ISOCELES\n");
    }
    else if(lado1!=lado2 && lado1!=lado3 && lado2!=lado3){
        printf("El triangulo es ESCALENO\n");
    }

    printf("\nEL MAYOR DE SUS LADOS ES: \n");
    if(lado1>lado2 && lado1>lado3){
        printf("%i",lado1);
    }
    else if(lado2>lado1 && lado2>lado3){
        printf("%i",lado2);
    }
    else if(lado3>lado1 && lado3>lado2){
        printf("%i",lado3);
    }
    else if (lado1==lado2 && lado1==lado3){
        printf("%i",lado1);
    }
    else if ((lado1==lado2) && lado1>lado3){
        printf("%i",lado1);
    }
    else if ((lado2==lado3) && lado3>lado1){
        printf("%i",lado3);
    }
    else if ((lado1==lado3) && lado1>lado2){
        printf("%i",lado1);
    }

    printf("\n\nEL ORDEN ACENDENTE DE SUS LADOS ES: \n");
    if(lado1<lado2 && lado1<lado3){
        if(lado2<lado3){
            printf("%i",lado1);
            printf("%i",lado2);
            printf("%i",lado3);
        }
        else{
            printf("%i",lado1);
            printf("%i",lado3);
            printf("%i",lado2);
        }
    }
    else if(lado2<lado1 && lado2<lado3){
        if(lado1<lado3){
            printf("%i",lado2);
            printf("%i",lado1);
            printf("%i",lado3);
        }
        else{
            printf("%i",lado2);
            printf("%i",lado3);
            printf("%i",lado1);
        }
    }
    else if(lado3<lado1 && lado3<lado2){
        if(lado1<lado2){
            printf("%i",lado3);
            printf("%i",lado1);
            printf("%i",lado2);
        }
        else{
            printf("%i",lado3);
            printf("%i",lado2);
            printf("%i",lado1);
        }
    }
    else if(lado1==lado2 && lado1==lado3){
        printf("%i",lado1);
        printf("%i",lado2);
        printf("%i",lado3);
    }
    else if(lado1==lado2){
        if(lado1<lado3){
            printf("%i",lado1);
            printf("%i",lado2);
            printf("%i",lado3);
        }
        else{
            printf("%i",lado3);
            printf("%i",lado1);
            printf("%i",lado2);
        }
    }
    else if(lado1==lado3){
        if(lado1<lado2){
            printf("%i",lado1);
            printf("%i",lado3);
            printf("%i",lado2);
        }
        else{
            printf("%i",lado2);
            printf("%i",lado1);
            printf("%i",lado3);
        }
    }
    else if(lado2==lado3){
        if(lado2<lado1){
            printf("%i",lado2);
            printf("%i",lado3);
            printf("%i",lado1);
        }
        else{
            printf("%i",lado1);
            printf("%i",lado2);
            printf("%i",lado3);
        }
    }
    return 0;
}
