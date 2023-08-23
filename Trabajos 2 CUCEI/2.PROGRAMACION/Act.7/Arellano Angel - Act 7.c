//Arellano Granados Angel Mariano
#include <stdio.h>
#include <stdlib.h>

int main(){
    struct libros{
        char nombre[20];
        char autor[20];
        char edit[10];
        int year;
        int pags;
    }book[5];

    int opc,i;

    do{
        printf("ELIJE UNA OPCION:\n\
1. Capturar Datos\n\
2. Mostrar Datos\n\
3. Salir\n");

        scanf("%i",&opc);

        switch(opc){
            case 1:
                for(i=0;i<5;i++){
                    printf("Nombre del libro %i: \n",i+1);
                    fflush(stdin);
                    gets(book[i].nombre);
                    printf("Nombre del autor %i: \n",i+1);
                    fflush(stdin);
                    gets(book[i].autor);
                    printf("Editorial del libro i: \n",i+1);
                    fflush(stdin);
                    gets(book[i].edit);
                    printf("Año de publicacion1: \n");
                    scanf("%i",&book[i].year);
                    printf("Numero de paginas: \n");
                    scanf("%i",&book[i].pags);
                }
                break;
            case 2:
                for(i=0;i<5;i++){
                    printf("Nombre del libro %i: \n",i+1);
                    printf("%s \n",book[i].nombre);
                    printf("Nombre del autor %i: \n",i+1);
                    printf("%s \n",book[i].autor);
                    printf("Editorial del libro i: \n",i+1);
                    printf("%s \n",book[i].edit);
                    printf("Año de publicacion1: \n");
                    printf("%i \n",book[i].year);
                    printf("Numero de paginas: \n");
                    printf("%i \n",book[i].pags);
                }
                break;
            case 3:
                printf("Gracias por usar \n");
                break;
            default:
                printf("Esa no es una opcion \n");
        }
    }while(opc!=3);
}
