//Arellano Granados Angel Mariano
// Hacer un programa para calcular el factorial de un numero
#include <stdio.h>
#include <stdlib.h>

int main (){
    int cont, num, cuenta;
    printf("Dame un numero: \n");
    scanf("%i",&num);
    cont=num;
    cuenta=1;
    printf("%i!=",num);
    while(cont>0){
        printf("%i x ",cont);
        cuenta=cuenta*cont;
        cont--;
    }
    printf("= %i",cuenta);
    return 0;
}
