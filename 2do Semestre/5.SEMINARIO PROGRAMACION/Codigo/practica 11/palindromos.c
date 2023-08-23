#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int main(){
    int control=0;
    do{
        int i,j,fin=0,len,acum=0,n=0;
        char frase[20];
        printf("Dame la frase a evaluar (omite los espacios): \n");
        fflush(stdin);
        gets(frase);
        len=strlen(frase);

        //quitar espacios
        /*for(i=0;i<len;++i)
            if(frase[i]!=' ')
                frase[n++]=frase[i];
        frase[n]='\0';

        //Control
        printf("\n");
        printf("'%s'",frase);*/

        //comparar ambas cadenas
         for(i=0,j=len-1;i<=len,j>=0;i++,j--){
            //printf("\n%c  %c  %i\n",frase[i],frase[j],len);
            if(frase[i]==frase[j])
                acum++;
         }
        if(acum==len){
            printf("La frase es un Palindromo");
            control=1;}
        else
            printf("La frase NO es un Palindromo");
             printf("\n");

    }while(control!=1);
}
