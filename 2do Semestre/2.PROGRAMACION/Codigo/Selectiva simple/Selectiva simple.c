//Imprime aprobado si la calificación es mayor a 8
#include<stdio.h>
#include<stdlib.h>

int main (int argc, char *argv[]){
    int calif;
    printf("Dame la calificacion: ");
    scanf("%f",calif);
    if(calif>=8)
        printf("Aprobado\n");
    if(calif<8)
        printf("Reprobado\n");
    return 0;
}
