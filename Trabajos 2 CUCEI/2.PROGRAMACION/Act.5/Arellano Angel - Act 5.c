#include<stdio.h>
#include<stdlib.h>

int main(){
    int i,j,opc;
    float num[3][3]={0},acum=0,aux;

    do{
        printf("ELIJE UNA OPCION:\n\
               1. Capturar la matriz\n\
               2. Mostrar la matriz \n\
               3. La suma de los elementos de la matriz\n\
               4. El valor menor de toda la matriz\n\
               5. Salir\n");
        scanf("%i",&opc);
        switch(opc){
            case 1:
                for(i=0;i<3;i++){
                    for(j=0;j<3;j++){
                        printf("%i,%i :",i,j);
                        scanf("%f",&num[i][j]);
                    }
                }
                aux=num[0][0];
                break;
            case 2:
                for(i=0;i<3;i++){
                    for(j=0;j<3;j++){
                        printf(" %.2f ",num[i][j]);
                    }
                    printf("\n");
                }
                break;
            case 3:
                for(i=0;i<3;i++){
                    for(j=0;j<3;j++){
                        acum+=num[i][j];
                    }
                }
                printf("La suma de los valores de la matriz es: %f\n",acum);
                break;
            case 4:
                for(i=0;i<3;i++){
                    for(j=0;j<3;j++){
                        if(num[i][j]<aux)
                            aux=num[i][j];
                    }
                }
                printf("El valor menor de la matriz es: %f\n",aux);
                break;
            case 5:
                printf("Gracias por usar\n");
                break;
        }
    }while(opc!=5);
}
