//Nombre: Angel Mariano Arellano Granados
//Fecha: 17 de Octubre de 2021
//Descripcion: Calcular la potencia de un número
#include <stdio.h>
#include <stdlib.h>

int main (){
    int base, exponente, cont,acum;
    acum=1;
    printf("Dame el numero que corresponde a la base: \n");
    scanf("%i",&base);
    printf("Dame el numero de la potencia que sera elevado el numero: \n");
    scanf("%i",&exponente);
    for (cont=1;cont<=exponente;cont++){
        acum=acum*base;
    }
    printf("El resultado es %i",acum);
    return 0;
}
