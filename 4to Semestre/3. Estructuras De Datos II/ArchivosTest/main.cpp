#include <iostream>
#include <cstdlib>
#include <string.h>
#include <fstream>
#include <stdio.h>
#include<time.h>

using namespace std;

struct Producto{
    char codigo[7];
    char nombre[25];
    char descripcion[150];
    const char *especialidad[20];
    float precio;
};

int main()
{
    //Declaracion de archivos de lectura y escrritura
    ofstream Esc;
    ofstream Ind;
    ifstream Lec;

    Esc.open("test.txt",ios::app);

    /*char a[30] = "ANGEL";
    char b[30] = "MARIANO";
    float d = 1.99;*/

    char a[30]= {0},b[30]= {0},d[30]= {0};
    float c;
    bool pi = false;
    fflush(stdin);
    cout<<"Nombre del Producto:"<<endl;
    cin>>a;fflush(stdin);
    cout<<"Descripcion del Producto:"<<endl;
    cin>>b;fflush(stdin);
    cout<<"Precio del Producto:"<<endl;
    cin>>c;fflush(stdin);
    cout<<"Selecciona la Especialidad del Producto:"<<endl;
    int opc;
    cout<<"\t"<<"1) PIZZAS"<<endl;
    cout<<"\t"<<"2) PICAR Y COMPARTIR"<<endl;
    cout<<"\t"<<"3) HELADOS"<<endl;
    cout<<"\t"<<"4) BEBIDAS"<<endl;
    cin>>opc;
    switch (opc){
    case 1:
        strcat (d,"PIZZAS");
        break;
    case 2:
        strcat (d,"PICAR Y COMPARTIR");
        pi = true;
        break;
    case 3:
        strcat (d,"HELADOS");
        break;
    case 4:
        strcat (d,"BEBIDAS");
        break;
    }
    fflush(stdin);

    /*int auxNum;
    char num[1],part1[2], part2[2],cod[7];//partes del codigo
    srand(time(NULL));

    for(int i=0;i<2;i++){
        auxNum = 48 + rand () %10;
        num[i]= char(auxNum);
    }
    //especialidad
    if(strcmp(b,"PICAR Y COMPARTIR"))
        strncpy(part1,b,2);
    else
        strncpy(part1,b,1);
    fflush(stdin);
    //nombre
    strncpy(part2,a,3);
    fflush(stdin);

    //Esc<<num<<" "<<part1<<" "<<part2<<"|"<<a<<"|"<<b<<"|"<<d<<"|"<<"\n";*/

    int n1,n2;
    srand(time(NULL));
    n1 = rand()%10;
    n2 = rand()%10;

    char c1[5]= {0},c2[5]= {0};
    if (pi){
        strncpy(c1,d,2);
    }
    else{
        strncpy(c1,d,1);
    }
    strncpy(c2,a,3);

    Esc<<n1<<n2<<c1<<c2<<"|"<<a<<"|"<<b<<"|"<<c<<"|"<<d<<"\n";

    cout << "Stan LOONA!" << endl;
    return 0;
}
/*
//fincion que agrega un registro al archivo
void insertar(ofstream &A, ofstream &I)
{
    //abrimos el archivo MENU para escribir
    A.open("MENU.txt",ios::out);//no mantiene

    //Declaracion de estructura
    Producto p;

    //solicitud de datos
    fflush(stdin);
    cout<<"Nombre del Producto:"<<endl;
    //fgets(p.nombre,25,stdin);
    cin>>p.nombre;fflush(stdin);
    cout<<"Descripcion del Producto:"<<endl;
    //fgets(p.descripcion,150,stdin);
    cin>>p.descripcion;fflush(stdin);
    cout<<"Precio del Producto:"<<endl;
    cin>>p.precio;
    fflush(stdin);
    cout<<"Especialidad del Producto:"<<endl;
    //fgets(p.especialidad,20,stdin);
    cin>>p.especialidad;fflush(stdin);

    //Creacion de codigo
    //2 numeros aleatorios
    int auxNum;
    char auxCod[7], num[2],part1[2], part2[3];//partes del codigo
    for(int i=0;i<2;i++){
        auxNum = rand ()+48 %57;

        num[i]= char(auxNum);
    }
    //especialidad
    if(strcmp(p.especialidad,"PICAR Y COMPARTIR")){
        strncpy(part1,p.especialidad,2);
    }
    else{
        strncpy(part1,p.especialidad,1);
    }
    //nombre
    strncpy(part2,p.nombre,3);
    //union
    strcat(auxCod,num);
    strcat(auxCod,part1);
    strcat(auxCod,part2);
    strcat(p.codigo,auxCod);

    //escrivir en el archivo
    A<<p.codigo<<"|"<<p.nombre<<"|"<<p.descripcion<<"|"<<p.especialidad<<"|"<<p.precio<<"\n";

    //Cerramos archivos
    A.close();
    I.close();
}*/

