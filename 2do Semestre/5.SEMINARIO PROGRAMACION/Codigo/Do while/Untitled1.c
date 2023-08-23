//ARELLANO GRANADOS ANGEL MARIANO
//USO DE DO WHILE
#include <stdio.h>
#include <stdlib.h>

int main (){
    int cont;
    float num, prom, cuenta;
    cont=0;
    do{
        printf("Dame un numero: \n");
        scanf("%f",&num);
        cuenta=cuenta+num;
        cont++;
    }while(num!=0);
    prom=cuenta/(cont-1);
    printf("El promedio es: %.2f",prom);
}
