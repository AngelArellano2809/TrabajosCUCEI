//Nombre: Angel Mariano Arellano Granados
//Fecha: 3 de Noviembre de 2021
//Descripcion: Organizador de un arreglo de 10 elementos
#include<stdio.h>
#include<stdlib.h>

int main (){
    int num [10],ord[10]={0},i,j,opc,aux;

    do{
    printf("1.Capturar los datos del vector\n\
2.Ordenar y mostrar el contenido del vector en forma ascendente\n\
3.Ordenar y mostrar el contenido del vector en forma descendente\n\
4.Salir\n");
    scanf("%i",&opc);

    switch(opc){
        case 1:
            for(i=0;i<10;i++){
                printf("Dame el numero %i:\n",i+1);
                scanf("%i",&num[i]);
                ord[i]=num[i];
            }
            break;
        case 2:
            for(i=0;i<10;i++)
                printf(" %i ",num[i]);
            printf("\n");
            for(i=0;i<10;i++){
                for(j=0;j<i;j++){
                    if (ord[i]<ord[j]){
                    aux=ord[i];
                    ord[i]=ord[j];
                    ord[j]=aux;
                    }
                }
            }
            for(i=0;i<10;i++)
                printf(" %i ",ord[i]);
            printf("\n");
            break;
        case 3:
            for(i=0;i<10;i++){
                printf(" %i ",num[i]);
            }
            printf("\n");
            for(i=0;i<10;i++){
                for(j=0;j<i;j++){
                    if (ord[i]>ord[j]){
                    aux=ord[i];
                    ord[i]=ord[j];
                    ord[j]=aux;
                    }
                }
            }
            for(i=0;i<10;i++)
                printf(" %i ",ord[i]);
            printf("\n");
            break;
    }
    }while(opc!=4);
}
