#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float main(){
    float bruto,neto,iva,total;
    printf("Dame el importe bruto: \n");
    scanf("%f",&bruto);
    if (bruto>15000)
        iva=1.16;
        else
            iva=1.10;
    total=(bruto*iva);
    printf("El total a pagar es: %.2f",total);
    return 0;
}

