#include <iostream>
#include <cstdlib>
#include <string.h>
#include <fstream>
#include <stdio.h>
#include<time.h>
#include <cmath>
#include <locale.h>

using namespace std;

//prototipos de funciones
void insertar(ofstream &A,ifstream &B,ofstream &I);
void mostrar (ifstream &A,ifstream &I);

//Estructura de registros
struct Producto{
    char codigo[7] = {0};
    char dinero[5] = {0};
    char nombre[25] = {0};
    char descripcion[180] = {0};
    char especialidad[18] = {0};
};

//Estructura de Indices
class Indice{
    public:
        char codigo[7] = {0};
        int NRR;
        Indice *next;
        Indice(char cod[7],int n);
};

Indice::Indice(char cod[7],int n){
    strcat (codigo,cod);
    NRR = n;
    next = NULL;
}

class Lista{
    public:
        Indice *ptrHead;
        friend class Indice;
        Lista();
        void add(char cod[7],int n);
        void Ordenar();
};

Lista::Lista(){
    ptrHead = NULL;
}

void Lista::add(char cod[7], int n){
    Indice *new_nodo = new Indice(cod,n);
    if(!ptrHead){
        ptrHead = new_nodo;
    }
    else{
        Indice *ptr = ptrHead;
        while(ptr->next!=NULL){
            ptr = ptr->next;
        }
        ptr->next = new_nodo;
    }
}

void Lista::Ordenar(){
    Indice*a,*b;
    for(a=ptrHead;a->next!=NULL;a=a->next){
        for(b=a->next;b->next!=NULL;b=b->next){
            if(strcmp(a->codigo,b->codigo)>0){
                char auxC1[7] = {0};
                int auxN = 0;
                //intercambia el codigo
                strcat(auxC1,a->codigo);
                strcpy(a->codigo,b->codigo);
                strcpy(b->codigo,auxC1);
                //intercambia NRR
                auxN = a->NRR;
                a->NRR = b->NRR;
                b->NRR = auxN;
            }
        }
    }
}

int main()
{
    //Declaracion de archivos de lectura y escrritura
    setlocale(LC_ALL, "spanish");
    ofstream Esc;
    ifstream Lec;
    ofstream Ind;
    ifstream IndL;
    int opc;
    do{
        //Menu de usuario
       cout<<"1. Insertar Registro"<<endl;
       cout<<"2. Mostrar Registro"<<endl;
       cout<<"3. Salir"<<endl;
       cin>>opc;

       //casos de menu
       switch(opc){
       case 1:
           insertar(Esc,Lec,Ind);
        break;
       case 2:
           mostrar(Lec,IndL);
        break;
       case 3:
        break;
       default:
           cout<<"Opcion incorrecta"<<endl;
        break;
       }
    }while(opc!=3);
    cout << "Exito!" << endl;
    return 0;
}

//fincion que agrega un registro al archivo
void insertar(ofstream &A,ifstream &A2, ofstream &I)
{
    //abrimos el archivo MENU para escribir
    A.open("MENU.txt",ios::app);

    //Declaracion de estructura
    Producto p;

    //solicitud de datos
    fflush(stdin);
    cout<<"Nombre del Producto:"<<endl;
    cin.getline(p.nombre, 25);
    fflush(stdin);
    cout<<"Descripcion del Producto:"<<endl;
    cin.getline(p.descripcion, 180);
    fflush(stdin);
    cout<<"Precio del Producto:"<<endl;
    cin.getline(p.dinero,5);
    fflush(stdin);
    cout<<"Selecciona la Especialidad del Producto:"<<endl;
    int opc;
    bool pi = false;//Bandera para saber si se elije Picar y compartir
    cout<<"\t"<<"1) PIZZAS"<<endl;
    cout<<"\t"<<"2) PICAR Y COMPARTIR"<<endl;
    cout<<"\t"<<"3) HELADOS"<<endl;
    cout<<"\t"<<"4) BEBIDAS"<<endl;
    cin>>opc;
    switch (opc){
    case 1:
        strcat (p.especialidad,"PIZZAS            ");
        break;
    case 2:
        strcat (p.especialidad,"PICAR Y COMPARTIR ");
        pi = true;
        break;
    case 3:
        strcat (p.especialidad,"HELADOS           ");
        break;
    case 4:
        strcat (p.especialidad,"BEBIDAS           ");
        break;
    }
    fflush(stdin);

    //rellenar con espacios
    //nombre
    int i=0,cont=0;
    while(p.nombre[i]){
        cont++;
        i++;
    }
    for(int j=cont;j<24;j++){
        p.nombre[j]=' ';
    }
    //descripcion
    i=0,cont=0;
    while(p.descripcion[i]){
        cont++;
        i++;
    }
    for(int j=cont;j<179;j++){
        p.descripcion[j]=' ';
    }
    //precio
    i=0,cont=0;
    while(p.dinero[i]){
        cont++;
        i++;
    }
    for(int j=cont;j<4;j++){
        p.dinero[j]=' ';
    }

    //Creacion de codigo
    //2 numeros aleatorios
    int n1,n2;
    srand(time(NULL));
    n1 = rand()%10;
    n2 = rand()%10;

    //Fragmentos de especialidad y nombre
    char c1[5]= {0},c2[5]= {0};
    if (pi){
        strncpy(c1,p.especialidad,2);
    }
    else{
        strncpy(c1,p.especialidad,1);
    }
    strncpy(c2,p.nombre,3);


    //escrivir en el archivo MENU.txt
    if(pi){
        A<<n1<<n2<<c1<<c2<<"|"<<p.nombre<<"|"<<p.descripcion<<"|"<<p.dinero<<"|"<<p.especialidad<<"|"<<"\n";
    }
    else{
        A<<n1<<n2<<c1<<c2<<" "<<"|"<<p.nombre<<"|"<<p.descripcion<<"|"<<p.dinero<<"|"<<p.especialidad<<"|"<<"\n";
    }
    A.close();
    //Abrimos el MEnu en lectura para extraer el indice desordendo
    A2.open("MENU.txt",ios::in);

    //Declara la lista para cargar el indice en esta de manera desordenada
    Lista lista;

    char c4[10];
    int k = 0;
    A2.getline(c4,8,'|');
    do{
        lista.add(c4,k);
        k++;
        A2.ignore(236,'\n');
    }while(A2.getline(c4,8,'|'));
    lista.add(c4,k);
    A2.close();

    //abrimos el archivo INDICE para escribir el indice ordenado
    I.open("INDICE.txt",ios::out);
    //ordenamos el indice
    lista.Ordenar();

    //ingresamos el indice ordenado en su archivo
    Indice *ptr;
    for(ptr = lista.ptrHead;ptr->next!=NULL;ptr = ptr->next){
        I<<ptr->codigo<<"|"<<ptr->NRR<<"\n";
    }
    I.close();
}

//funcion que busca y muestra un registro por su codigo
void mostrar (ifstream &A,ifstream &I)
{
    //recibimos el codigo por consola
    char codB[10] = {0},codR[10] = {0},nrrR[5] = {0},rR[237] = {0};
    fflush(stdin);
    cout<<"Codigo de producto a Buscar:"<<endl;
    cin.getline(codB, 10);
    fflush(stdin);

    //Rellenamos con esparcios para comparar directamenta
    int i=0,cont=0;
    while(codB[i]){
        cont++;
        i++;
    }
    for(int j=cont;j<7;j++){
        codB[j]=' ';
    }

    //abrimos el archivo INDICE y MENU como lectura
    I.open("INDICE.txt",ios::in);
    A.open("MENU.txt",ios::in);

    //recupermos secuencialmente los codigos del indice
    I.getline(codR,8,'|');
    do{
        //comparamos codigo buscado con el codigo recuperado
        if(strcmp(codB,codR)==0){
            I.getline(nrrR,5,'\n');
            A.ignore(238*atoi(nrrR));
            A.getline(rR,240,'\n');
            cout<<"CODIGO:|NOMBRE:                 |DESCRIPCION:                                                                                                                                                                       |$:  |ESPECIALIDAD:     |";
            cout<<rR<<endl;
            return;
        }
        I.ignore(10,'\n');
    }while(I.getline(codR,8,'|'));
}

