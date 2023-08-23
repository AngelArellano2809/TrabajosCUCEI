//Arellano Granados Angel Mariano
//D07   30/11/2022

#include <iostream>
#include <string.h>
#include <fstream>
#include <stdio.h>

using namespace std;

//archivos por usar
ifstream Prod;//Productos.txt Lectura
ofstream Arb;//INDICE.txt Escribir
int raiz = 0;//Raiz del arbol
bool generado = false; //bandera para que solo se genera una vez

void inserta(char[4],int,bool);

//struct Pagina
struct PaginaAB{
    int contL = 0;//contador de llaves
    int padre = -1;//padre de la hoja
    char arrL[3][4] = {{"---"},{"---"},{"---"}};//arreglo de llaves
    int hijos[4] = {-1,-1,-1,-1};//arreglo de hijos
}PAGINA[30];

void promocion(int NRR_original,int NRR_nuevo){//funcion que promueve una llave
    int NRR_prom = 0;
    if (PAGINA[NRR_original].padre == -1){// si la pagina original no tiene padre le buscamos uno
        for(int i = 0; i< 30; i++){//recorremos todo el arreglo en busca de una pagina vacia
            if (PAGINA[i].contL == 0){
                NRR_prom = i;//se encuentra el NRR donde se colocara la llave
                PAGINA[NRR_original].padre = i;//se le asigna un padre
                raiz = i;//actualizamos la raiz
                break;
            }
        }
    }
    else{//si ya tiene un padre se usa como NRR de promocion
        NRR_prom = PAGINA[NRR_original].padre;
    }
    PAGINA[NRR_nuevo].padre = NRR_prom;//se le asigna el mismo padre a la pagina nueva
    char llave_prom[4];//se guada la llave a promover y acomodamos las llaves en la pagina nueva
    strcpy(llave_prom,PAGINA[NRR_nuevo].arrL[0]);
    strcpy(PAGINA[NRR_nuevo].arrL[0],PAGINA[NRR_nuevo].arrL[1]);
    strcpy(PAGINA[NRR_nuevo].arrL[1],"---");
    //actualiozamos el arreglo de hijos
    for(int j = 0;j < 4;j++){//recorremos su arreglo de hijo para ver si el NRR original ya exite
        if(PAGINA[NRR_prom].hijos[j] == NRR_original){
            if(PAGINA[NRR_prom].hijos[j+1] == -1 ){//si la posicion al lado de la original esta vacia,
                PAGINA[NRR_prom].hijos[j+1] = NRR_nuevo;//ingresamos el hijo nuevo directamente
                break;
            }
            else{//si no movemos los hijos para que la posicion siguiente este disponible
                if(PAGINA[NRR_prom].hijos[j+2] != -1){//se previene que no se pierda el ultimo hijo
                    PAGINA[NRR_nuevo+1].hijos[0] = PAGINA[NRR_prom].hijos[j+2];
                }
                PAGINA[NRR_prom].hijos[j+2] = PAGINA[NRR_prom].hijos[j+1];
                PAGINA[NRR_prom].hijos[j+1] = NRR_nuevo;
                break;
            }
        }
        else if(PAGINA[NRR_prom].hijos[j] == -1){//Si el NRR de la pagina original no esta en el arreglo de hijos buscamos el primero disponible
            //insertamos ambos hijos directamente
            PAGINA[NRR_prom].hijos[j] = NRR_original;
            PAGINA[NRR_prom].hijos[j+1] = NRR_nuevo;
            break;
        }
    }
    inserta(llave_prom,NRR_prom,true);//llamamos a inserta pero para que no llegue a las hojas marcamos PORM como TRUE
}

void division(int NRR, char llave[4], int POS){//funcion que se llama para dividir las llaves de una pagina llena en dos nuevas
    int NRR_nuevo = 0;
    for(int i = 0; i< 30; i++){//buscamos la primera pagina vacia
        if (PAGINA[i].contL == 0){
            NRR_nuevo = i;
            break;
        }
    }
    //Dependiendo de la posicion donde deberia ir la llave nueva se hace un acomodo direrente
    if(POS == 0){//se mueve la llave 1 y 2 a la pagina nueva y la 0 se mueve a la posicion 1 de
                //la pagina original para insertar la nueva llave en la posicion 0
        strcpy(PAGINA[NRR_nuevo].arrL[1],PAGINA[NRR].arrL[2]);
        strcpy(PAGINA[NRR_nuevo].arrL[0],PAGINA[NRR].arrL[1]);
        strcpy(PAGINA[NRR].arrL[1],PAGINA[NRR].arrL[0]);
        strcpy(PAGINA[NRR].arrL[2],"---");
        strcpy(PAGINA[NRR].arrL[0],llave);
        PAGINA[NRR_nuevo].contL = 1;
        PAGINA[NRR].contL = 2;
    }
    else if(POS == 1){//se mueve la llave 1 y 2 a la pagina nueva y se insera la llave nueva en la posicion 1 de la pagina original
        strcpy(PAGINA[NRR_nuevo].arrL[0],PAGINA[NRR].arrL[1]);
        strcpy(PAGINA[NRR_nuevo].arrL[1],PAGINA[NRR].arrL[2]);
        strcpy(PAGINA[NRR].arrL[2],"---");
        strcpy(PAGINA[NRR].arrL[1],llave);
        PAGINA[NRR_nuevo].contL = 1;
        PAGINA[NRR].contL = 2;
    }
    else if(POS == 2){//se mueve la llave 2 a la posicion 1 de la pagina nueva y la llave nueva se inserta en la posicion 0 de la pagina nueva
        strcpy(PAGINA[NRR_nuevo].arrL[1],PAGINA[NRR].arrL[2]);
        strcpy(PAGINA[NRR].arrL[2],"---");
        strcpy(PAGINA[NRR_nuevo].arrL[0],llave);
        PAGINA[NRR_nuevo].contL = 1;
        PAGINA[NRR].contL = 2;
    }
    else if(POS == 3){//se mueve la llave 2 a la posicion 0 de la pagina nueva y la llave nueva se inserta en la posicion 1 de la pagina nueva
        strcpy(PAGINA[NRR_nuevo].arrL[0],PAGINA[NRR].arrL[2]);
        strcpy(PAGINA[NRR].arrL[2],"---");
        strcpy(PAGINA[NRR_nuevo].arrL[1],llave);
        PAGINA[NRR_nuevo].contL = 1;
        PAGINA[NRR].contL = 2;
    }
    promocion(NRR,NRR_nuevo);//se llama a promocion padando los NRRs de ambas paginas
}

void busca (int &NRR, char llave[4], int &POS, bool PROM){//obtiene las variables como referencia y devuelve el NRR y posicion donde
                                                        //deberia de estar la llave ingresada, si PROM es TRUE no bajara hasta el nivel hoja
    for(int i = 0; i < 3 ; i++){//recorre todo el arrglo de llaves de la pagina NRR
        if(strcmp(PAGINA[NRR].arrL[i],"---")==0){//si la llave esta vacia la ignora
            continue;
        }
        else {
            if(strcmp(PAGINA[NRR].arrL[i],llave)>0){//si la llave encontrada es mayor a la ingresada no se presentan cambios en la posicion
                POS = POS;
            }
            else{
                if(strcmp(PAGINA[NRR].arrL[i],llave)<0){//si la llave encontrada es menor la posion se le sima uno
                    POS = POS + 1;
                }
            }
        }
    }
    if (PAGINA[NRR].hijos[POS]!=-1 && PROM == false){//Si no se trata de una promocion se vuelve a llamar a la funcion hasta que se llegue al nivel hoja
        NRR = PAGINA[NRR].hijos[POS];//de declara el nuevo NRR como el hijo que este en la posion donde deberia ser insertada la llave
        POS = 0;//se reinicia la posicion
        busca(NRR,llave,POS,PROM);//se aplica la recursividad con los nuevos valores
    }
}

void inserta(char llave[4], int NRR,bool PROM){//funcion que inserta una llave en el nivel hoja o en la pagina indicada si es una promocion
    int POS = 0;
    busca(NRR,llave,POS,PROM);//buscamos la pagina y posiion donde deberia ir la llave
    //cout<<POS<<" "<<NRR<<endl;//testeo
    if (PAGINA[NRR].contL == 3){//si la pagina esta llena se llama a la funcion divison
        division(NRR,llave,POS);
        return;
    }
    if(strcmp(PAGINA[NRR].arrL[POS],"---")!=0){//si la posion deseada no esta vacia entonces
        PAGINA[NRR].contL++;
        if(POS == 0){//si la posicion deseada es 0 se mueven ambas llaves una posicion a la derecha para poder insertarla
            strcpy(PAGINA[NRR].arrL[POS+2],PAGINA[NRR].arrL[POS+1]);
            strcpy(PAGINA[NRR].arrL[POS+1],PAGINA[NRR].arrL[POS]);
            strcpy(PAGINA[NRR].arrL[POS],llave);
        }
        else if(POS == 1){//si la posicion deseada es 1 se mueve la llave uno a la derecha para poder insertarla
            strcpy(PAGINA[NRR].arrL[POS+1],PAGINA[NRR].arrL[POS]);
            strcpy(PAGINA[NRR].arrL[POS],llave);
        }
    }
    else{// si si esta vacia la llave se inserta directamente
        PAGINA[NRR].contL++;
        strcpy(PAGINA[NRR].arrL[POS],llave);
    }
}

void crearIndice(){//funcion que crea el archivo INDICE.txt
    Arb.open("INDICE.txt",ios::out);// se abre el archivo en modo escritura borrando todo lo anterior
    for (int i=0; i<30;i++){// se corre todo el arrglo de paginas
        if(PAGINA[i].contL == 0){// si se encuentra una pagina vacia el ciclo termina
            break;
        }
        Arb<<i<<"|"<<PAGINA[i].contL<<"|";//se agraga el numero de la pagina
        for (int j=0;j<3;j++){//se recorre el arreglo de llaves
            Arb<<PAGINA[i].arrL[j]<<" ";//se agrega cada una de las llaves
        }
        Arb<<"|";
        for (int k=0;k<4;k++){// se recorre el arreglo de hijos
            if(PAGINA[i].hijos[k] != -1){//si el hijo no esta vacio se agrega un espacio de mas (detalle visual)
                Arb<<" "<<PAGINA[i].hijos[k]<<" ";//se agrega el hijo
            }
            else{
                Arb<<PAGINA[i].hijos[k]<<" ";//se agrega el hijo vacio
            }
        }
        Arb<<"|\n";
    }
    Arb.close();// se cierra el archivo
}

void generar(){//funcion que genera el arbol B paginado en RAM
    Prod.open("Productos.txt",ios::in);//se abre el archivo Productos.txt en lectura
    char llave[4];
    while(Prod.getline(llave,4,'|')){//se toma los primeros 3 caracteres y el ciclo para hasta que esta accion no sea posible
        //cout<<llave<<endl;//testeo
        inserta(llave, raiz,false);//se inserta en el arbol la llave encontrada, NRR es la raiz al inicio
        Prod.ignore(120,'\n');//se ignoran el resto de caracteres hasta encontrar un salto de pagina
    }
    crearIndice();//se llama a la funcion que crea el archivo INDICE.txt
    Prod.close();//se cierra en archivo Productos.txt
}

void mostrar(){//funcion que muestra en consola una tabla con el arbol B Paginado
    cout<<"|NP|CL|Arreglo Llaves|Arreglo Hijos|"<<endl;
    for (int i=0; i<30;i++){//se recorre el arreglo de paginas
        if(PAGINA[i].contL == 0){//si se encuentra una pagina vacia el ciclo termina
            break;
        }
        cout<<"|"<<i<<" |"<<PAGINA[i].contL<<" | ";//se muestran el numero de pagina y su contador de llaves
        for (int j=0;j<3;j++){
            cout<<PAGINA[i].arrL[j]<<" ";//se muestran las llaves de la pagina
        }
        cout<<" | ";
        for (int k=0;k<4;k++){
            if(PAGINA[i].hijos[k] != -1){
                cout<<" "<<PAGINA[i].hijos[k]<<" ";// se muestran los hijos
            }
            else{
                cout<<PAGINA[i].hijos[k]<<" ";// se muestran los hijos vacios
            }
        }
        cout<<"|"<<endl;
    }
}

int main()
{
    int opc;
    do{
        //Menu de usuario
       cout<<"1. Generar indice(arbol binario paginado)."<<endl;
       cout<<"2. Mostrar indice"<<endl;
       cout<<"3. Salir"<<endl;
       cin>>opc;

       //casos de menu
       switch(opc){
       case 1:
           //Generar Arbol B solo una vez
           if (!generado){
                generar();
                generado = true;
           }
        break;
       case 2:
           //Mostrar tabla de Arbol B
           mostrar();
        break;
       case 3:
           //Salir
        break;
       default:
           cout<<"Opcion incorrecta"<<endl;
        break;
       }
    }while(opc!=3);
    cout << "Exito!" << endl;
    return 0;
}

