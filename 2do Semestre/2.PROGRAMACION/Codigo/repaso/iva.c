#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float main(){
    float presio,unidades,iva,total;
    printf("Dame el presio del producto: \n");
    scanf("%f",&presio);
    printf("Dame la cantidad de unidades: \n");
    scanf("%f",&unidades);
    iva=1.16;
    total=(presio*unidades)*iva;
    printf("El total a pagar es: %.2f",total);
    return 0;
}
