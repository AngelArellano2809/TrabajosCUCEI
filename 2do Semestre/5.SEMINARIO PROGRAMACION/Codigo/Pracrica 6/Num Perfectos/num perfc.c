#include<stdio.h>
#include<stdlib.h>
//Programa que encuentra los numeros perfectos del 2 al 10,000
int main(){
    int N, cont, acum;

    for(N=2;N<=10000;N++){
        //printf("%i\n",N);
        cont=1;
        acum=0;
        while(cont<=(N/2)){
            //printf("\t%i\n",N%cont);
            if((N%cont)==0){
                acum=acum+cont;
            }
        cont++;
        }
        if (acum==N){
            printf("%i es un numero perfecto\n",N);
        }
    }
}
