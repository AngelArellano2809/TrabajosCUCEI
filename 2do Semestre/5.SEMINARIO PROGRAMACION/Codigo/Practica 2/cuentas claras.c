//ARELLANO GRANADOS ANGEL MARIANO
//Programa que nos auxilie en el cálculo de las cuentas en una venta
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
float main (){
    float productos,precio,sub_total,total,iva,paga;
    int cambio;
    printf("Dame la cantidad de productos que va a comprar: \n");
    scanf("%f",&productos);
    printf("Dame el precio unitario de producto: \n");
    scanf("%f",&precio);
    sub_total=productos*precio;
    iva=1.16;
    total=sub_total*iva;
    printf("El total a pagar es: %.2f\n",total);

    printf("Con que cantidad de dinero va a pagar: \n");
    scanf("%f",&paga);
    cambio=paga-total;
    printf("El cambio es de: %.2d\n",cambio);

    //Billetes:
    printf("Su cambio sera en: \n");
    printf("Billetes de 1000:\t %d \n",cambio/1000);
    cambio %= 1000;
    printf("Billetes de 500:\t %d \n",cambio/500);
    cambio %= 500;
    printf("Billetes de 200:\t %d \n",cambio/200);
    cambio %= 200;
    printf("Billetes de 100:\t %d \n",cambio/100);
    cambio %= 100;
    printf("Billetes de 50:\t\t %d \n",cambio/50);
    cambio %= 50;
    printf("Billetes de 20:\t\t %d \n",cambio/20);
    cambio %= 20;
    //monedas
    printf("Monedas de 10:\t\t %d \n",cambio/10);
    cambio %= 10;
    printf("Monedas de 5:\t\t %d \n",cambio/5);
    cambio %= 5;
    printf("Monedas de 2:\t\t %d \n",cambio/2);
    cambio %= 2;
    printf("Monedas de 1:\t\t %d \n",cambio/1);
    cambio %= 1;
    //centavos
    printf("Centavos:\t\t %d \n",cambio);
    return 0;
}
