//ARELLANO GRANADOS ANGEL MARIANO
//Programa que administra en inventario de una tienda
#include <stdio.h>
#include <stdlib.h>
#define MAX 5

struct ITEM{
char nombre[20];
float precio;
int cantidad;
};

void capturar(struct ITEM prod[], int index);
void mostrar(struct ITEM prod[],int capt);
int buscar(struct ITEM prod[], char name_buscar[20],int capt, int encontrado);
void modificar(struct ITEM prod[]);
int eliminar(struct ITEM prod[],int capt);

int main (){
    struct ITEM producto[MAX];
    int opc,capturado=0,indice=0,i,encontrado,modifica,indice_modificado;
    char nombre_buscar[20];

    do{
        printf("\nINVENTARIO DE TENDA\n1.Capturar\n2.Mostrar\n3.Buscar\n4.Modificar\n5.Eliminar\n6.Salir\n");
        printf("Selecciona una opcion :\n");
        scanf("%d",&opc);
        switch(opc){
            case 1: if(capturado==MAX){
                    printf("\nYa se lleno la base de datos\n");
                }
                else{
                    capturar(producto,indice);
                    indice++;
                    capturado++;
                }
                break;
            case 2: if (capturado==0){
                    printf("No se han capturado registros \n");
                    break;
                }
                mostrar(producto,capturado);
                break;
            case 3: if (capturado==0){
                    printf("No se han capturado registros \n");
                    break;
                }
                printf("Dame un producto a buscar: \n");
                scanf("%s",&nombre_buscar);
                encontrado=0;
                encontrado=buscar(producto,nombre_buscar,capturado,encontrado);

                if (encontrado==0)
                    printf("No se encontro ninguna coincidencia\n");
                break;
            case 4: if (capturado==0){
                    printf("No se han capturado registros \n");
                    break;
                }
                printf("Dame un producto a modificar: \n");
                scanf("%s",&nombre_buscar);
                encontrado=0;
                encontrado=buscar(producto,nombre_buscar,capturado,encontrado);

                if(encontrado==0)
                    printf("No se encontro ninguna coincidencia\n");
                if(encontrado==1){
                    modificar(producto);
                    printf("Datos actualizados: \n");
                    mostrar(producto,capturado);
                    }
                break;
            case 5: if (capturado==0){
                    printf("No se han capturado registros \n");
                    break;
                }
                printf("Dame el producto a eliminar: \n");
                scanf("%s",&nombre_buscar);
                encontrado=0;
                encontrado=buscar(producto,nombre_buscar,capturado,encontrado);

                if (encontrado==0)
                    printf("No se encontro ninguna coincidencia\n");
                if(encontrado==1){
                    capturado=eliminar(producto,capturado);
                    indice=capturado;
                    printf("Datos actualizados: \n");
                    mostrar(producto,capturado);
                }
                break;
            case 6:printf("Gracias por usar");
                break;
            default:printf("Opcion equivocada, selecciona otra vez\n");
        }
    }while(opc!=6);
    return 0;
}

void capturar(struct ITEM prod[], int index){
    printf("Introduce el nombre del producto(sin espacios):\n");
    scanf("%s",prod[index].nombre);
    printf("Introduce su precio por unidad:\n");
    scanf("%f",&prod[index].precio);
    printf("Introduce la cantidad en existencia:\n");
    scanf("%i",&prod[index].cantidad);
}

void mostrar(struct ITEM prod[],int capt){
        int i;
        for(i=0;i<capt;i++)
        printf("Producto:\n%s\nVale: %.2f c/u\nTenemos %i en existencia \n\n",prod[i].nombre,prod[i].precio,prod[i].cantidad);
}

int buscar(struct ITEM prod[], char name_buscar[20],int capt, int encontro){
        int i;
        for(i=0;i<capt;i++){
            if (strcmp(name_buscar,prod[i].nombre)==0){
                printf("[%i]Producto: %s \n Vale: %f \n Tenemos: %i \n",i+1,prod[i].nombre,prod[i].precio,prod[i].cantidad);
                encontro=1;
                }
            }
        return encontro;
}

void modificar(struct ITEM prod[]){
        int indice_modificado,modifica;
        printf("Cual indice deseas modificar: ");
        scanf("%i",&indice_modificado);
        printf("Deseas modificar el (1) nombre, el (2) precio o la (3) cantidad :");
        scanf("%i",&modifica);
        switch(modifica){
        case 1:printf("Introduce el nuevo nombre : ");
            scanf("%s",prod[indice_modificado-1].nombre);
            break;
        case 2:printf("Introduce el nuevo precio : ");
            scanf("%f",&prod[indice_modificado-1].precio);
            break;
        case 3:printf("Introduce la nueva cantidad : ");
            scanf("%i",&prod[indice_modificado-1].cantidad);
            break;
        default:printf("Opcion equivocada \n");
        }
}

int eliminar(struct ITEM prod[],int capt){
        int indice_modificado,i;
        printf("Cual indice deseas eliminar: ");
        scanf("%i",&indice_modificado);
        for(i=indice_modificado-1;i<capt;i++){
            strcpy(prod[i].nombre,prod[i+1].nombre);
            prod[i].precio=prod[i+1].precio;
            prod[i].cantidad=prod[i+1].cantidad;
            }
        return capt=capt-1;
}
