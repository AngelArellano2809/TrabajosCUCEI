//Nombre: Angel Mariano Arellano Granados
//Fecha: 20 de Septiembre de 2021
//Descripcion: Calcula el area de un circulo
#include <stdio.h>
#include <stdlib.h>

float main(){
    float pulgadas,milimetros,yardas,metros,millas,kilometros;
    int opc;
    printf("DIME QUE OPCION QUIERE EJECUTAR:\n"
           "1. Para convertir de pulgadas a milimetros.\n"
           "2. Para convertir de yardas a metros.\n"
           "3. Para convertir de millas a kilometros\n\n"
           "Elija la opcion:\n");
    scanf("%i",&opc);
    switch(opc){
        case 1:
            printf("\nDame la cantidad de pulgadas a convertir: \n");
            scanf("%f",&pulgadas);
            milimetros=pulgadas*25.40;
            printf("\t%.2f pulgadas es igual a %.2f milimetros",pulgadas,milimetros);
            break;
        case 2:
            printf("\nDame la cantidad de yardas a convertir: \n");
            scanf("%f",&yardas);
            metros=yardas*0.9144;
            printf("\t%.2f yardas es igual a %.2f metros",yardas,metros);
            break;
        case 3 :
            printf("\nDame la cantidad de millas a convertir: \n");
            scanf("%f",&millas);
            kilometros=millas*1.6093;
            printf("\t%.2f millas es igual a %.2f kilometros",millas,kilometros);
            break;
        }
}
