#include<stdio.h>
#include<stdlib.h>

int main()
{
    int cont, acum, num;
    cont=2;
    acum=0;
    printf("Dame un numero: \n");
    scanf("%i",&num);
    while(acum==0 && cont<(num/2)){
        printf("%i\n",num%cont);
        if((num%cont)==0){
            acum++;
        }
        cont++;
    }
    if(acum==0){
        printf("Es un numero primo\n");
    }
    else
        printf("No es un numero primo\n");
}
