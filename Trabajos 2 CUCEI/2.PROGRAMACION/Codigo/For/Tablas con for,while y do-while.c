#include<stdio.h>
#include<stdlib.h>

int main(){
    int cont,res,num,lim,opc;
    do{
        printf("\tMENU\n");
        printf("1. Do-While\n");
        printf("2. While\n");
        printf("3. For\n");
        printf("Salir\n");
        printf("Slecciona una opcion: \n");
        scanf("%i",&opc);
        switch(opc){
            case 1:
                cont=1;
                printf("Dame un numero: \n");
                scanf("%i",&num);
                printf("Dame el limite de la tapla: \n");
                scanf("%i",&lim);
                do{
                    res=num*cont;
                    printf("%i x %i = %i\n",num,cont,res);
                    cont++;
                }while(cont<=lim);
                break;
            case 2:
                cont=1;
                printf("Dame un numero: \n");
                scanf("%i",&num);
                printf("Dame el limite de la tapla: \n");
                scanf("%i",&lim);
                while(cont<=lim){
                    res=num*cont;
                    printf("%i x %i = %i\n",num,cont,res);
                    cont++;
                }
                break;
            case 3:
                printf("Dame un numero: \n");
                scanf("%i",&num);
                printf("Dame el limite de la tapla: \n");
                scanf("%i",&lim);
                for (cont=1;cont<=lim;cont++){
                    res=num*cont;
                    printf("%i x %i = %i\n",num,cont,res);
                }
                break;

        }
    }while(opc!=4);
    return 0;
}
