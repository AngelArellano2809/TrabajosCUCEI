#include <stdio.h>
#include <stdlib.h>
#define MAX 5
struct PET{
char nombre[20];
int edad;
};

void capturar(struct PET pets[], int index);
void mostrar(struct PET pets[],int capt);
int buscar(struct PET pets[], char name_buscar[20],int capt, int encontrado);
void modificar(struct PET pets[]);
int eliminar(struct PET pets[],int capt);

void main(int argc, char *argv[]) {
    struct PET mascotas[MAX];
    int opc,capturado=0,indice=0,i,encontrado,modifica,indice_modificado;
    char nombre_buscar[20];
    do{
        printf("1.Capturar\n2.Mostrar\n3.Buscar\n4.Modificar\n5.Eliminar\n6.Salir\n");
        printf("Selecciona una opcion :");
        scanf("%d",&opc);
        switch(opc){
        case 1:if (capturado==MAX){
            printf("\nYa se lleno la base de datos\n");
            }
            else{
            capturar(mascotas,indice);
            indice++;
            capturado++;
            }
            break;
        case 2:if (capturado==0){
            printf("No se han capturado registros \n");
            break;
            }
            mostrar(mascotas,capturado);
            break;
        case 3:if (capturado==0){
                printf("No se han capturado registros \n");
                break;
                }
            printf("Dame un nombre a buscar: ");
            scanf("%s",&nombre_buscar);
            encontrado=0;
            encontrado=buscar(mascotas,nombre_buscar,capturado,encontrado);

        if(encontrado==0)
            printf("No se encontro ninguna coincidencia\n");
            break;
        case 4:if (capturado==0){
            printf("No se han capturado registros \n");
            break;
            }
            printf("Dame un nombre a buscar: ");
            scanf("%s",&nombre_buscar);
            encontrado=0;
            encontrado=buscar(mascotas,nombre_buscar,capturado,encontrado);

            if(encontrado==0)
                printf("No se encontro ninguna coincidencia\n");
            if(encontrado==1){
                modificar(mascotas);
                printf("Datos actualizados: \n");
                mostrar(mascotas,capturado);
                }
            break;
        case 5:if (capturado==0){
            printf("No se han capturado registros \n");
            break;
            }
            printf("Dame un nombre a eliminar: ");
            scanf("%s",&nombre_buscar);
            encontrado=0;
            encontrado=buscar(mascotas,nombre_buscar,capturado,encontrado);

            if(encontrado==0)
                printf("No se encontro ninguna coincidencia\n");
            if(encontrado==1){
                capturado=eliminar(mascotas,capturado);
                indice=capturado;
                printf("Datos actualizados: \n");
                mostrar(mascotas,capturado);
                }
                break;
        case 6:break;
        default:printf("Opcion equivocada, selecciona otra vez\n");
        }
        } while(opc!=6);
        system("PAUSE");
        return 0;
}

void capturar(struct PET pets[], int index){
        printf("Introduce un nombre y una edad\n");
        scanf("%s",pets[index].nombre);
        scanf("%i",&pets[index].edad);
}

void mostrar(struct PET pets[],int capt){
        int i;
        for(i=0;i<capt;i++)
        printf("%s tiene %i a#os\n",pets[i].nombre,pets[i].edad);
}

int buscar(struct PET pets[], char name_buscar[20],int capt, int encontro){
        int i;
        for(i=0;i<capt;i++){
            if (strcmp(name_buscar,pets[i].nombre)==0){
                printf("[%i]La mascota %s tiene %i a#os\n",i+1,pets[i].nombre,pets[i].edad);
                encontro=1;
                }
            }
        return encontro;
}

void modificar(struct PET pets[]){
        int indice_modificado,modifica;
        printf("Cual indice deseas modificar: ");
        scanf("%i",&indice_modificado);
        printf("Deseas modificar el (1) nombre o la (2) edad :\n");
        scanf("%i",&modifica);
        switch(modifica){
        case 1:printf("Introduce el nuevo nombre : ");
            scanf("%s",pets[indice_modificado-1].nombre);
            break;
        case 2:printf("Introduce la nueva edad : ");
            scanf("%i",&pets[indice_modificado-1].edad);
            break;
        default:printf("Opcion equivocada \n");
        }
}

int eliminar(struct PET pets[],int capt){
        int indice_modificado,i;
        printf("Cual indice deseas eliminar: ");
        scanf("%i",&indice_modificado);
        for(i=indice_modificado-1;i<capt;i++){
            strcpy(pets[i].nombre,pets[i+1].nombre);
            pets[i].edad=pets[i+1].edad;
            }
        return capt=capt-1;
}
