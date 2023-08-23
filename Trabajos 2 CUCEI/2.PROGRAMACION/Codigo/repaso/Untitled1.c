#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int a,b,c;
    printf("esto es un repaso\n");
    printf("Dame el valor de a: \n");
    scanf("%i",&a);
    printf("Dame el valor de b: \n");
    scanf("%i",&b);
    c=(a+a)*(b+b)-a*b;
    printf("El resultado es: %i",c);
    return 0;
}
