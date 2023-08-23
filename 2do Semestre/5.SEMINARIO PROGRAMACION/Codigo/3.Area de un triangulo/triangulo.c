#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    float altura,area,base;
    printf("Dame el lado del triangulo: \n");
    scanf("%f",&base);
    altura=((sqrt(3))*base)/2;
    area=(base*altura)/2;
    printf("El area del triangula es: %.2f", area);
    return 0;
}
