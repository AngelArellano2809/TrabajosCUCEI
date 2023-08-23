 //ARELLANO GRANADOS ANGEL MARIANO 218123444
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string.h>

#include "Cliente.h"
#include "Pelicula.h"
#include "SalaGrande.h"
#include "SalaMediana.h"
#include "Cine.h"
#include "Menu.h"
#include "Sala.h"

using namespace std;

void agregar(char tipo);

Menu menu;
Cine cine;

int main(){
    int opc,id;
    string nombre;
    do{
        opc=menu.menuPrincipal();
        switch(opc){
        case 1:{
            cine.MostrarTodo();
        }break;
        case 2:{
            cine.MostrarTodo();
            int opc;
            cout<<"A que tipo de sala? \n\t1) Grande\n\t2) Mediana"<<endl;
            cin>>opc;
            switch(opc){
                case 1:{
                    cout<<"En cual sala? \n1) SALA 1\n2) SALA 2"<<endl;
                    cin>>opc;
                    if(opc>=1&&opc<=2){
                        cine.venderAsiento(opc,'G');}
                    else
                        cout<<"esa sala no existe"<<endl;
                    break;
                }
                case 2:{
                    cout<<"En cual sala? \n1) SALA 1\n2) SALA 2\n3) SALA 3\n4) SALA 4\n5) SALA 5"<<endl;
                    cin>>opc;
                    if(opc>=1&&opc<=5){
                        cine.venderAsiento(opc,'M');}
                    else
                        cout<<"esa sala no existe"<<endl;
                    break;
                }
            }
        }break;
        case 3:{
            opc=menu.menuBusca();
            switch(opc){
                case 1:{
                    cout<<"\tIngresa un ID:"<<endl;
                    cin>>id;
                    cine.BuscarId(id);
                }break;
                case 2:{
                    cout<<"Ingresa un Nombre:"<<endl;
                    cin>>nombre;
                    cine.BuscarNombre(nombre);
                }break;
            }
        }break;
        case 4:{
            opc=menu.menuAgrega();
            if(opc==1){
                agregar('P');
            }
            else if(opc==2){
                agregar('H');
            }
        }break;
        case 5:{
            int opc;
            cout<<"A que tipo de sala? \n\t1) Grande\n\t2) Mediana"<<endl;
            cin>>opc;
            switch(opc){
                case 1:{
                    cout<<"En cual sala? \n1) SALA 1\n2) SALA 2"<<endl;
                    cin>>opc;
                    if(opc>=1&&opc<=2){
                        cine.eliminar(opc,'G');}
                    else
                        cout<<"esa sala no existe"<<endl;
                    break;
                }
                case 2:{
                    cout<<"En cual sala? \n1) SALA 1\n2) SALA 2\n3) SALA 3\n4) SALA 4\n5) SALA 5"<<endl;
                    cin>>opc;
                    if(opc>=1&&opc<=5){
                        cine.eliminar(opc,'M');}
                    else
                        cout<<"esa sala no existe"<<endl;
                    break;
                }
            }
        }break;
        }
    }while(opc);
    return 0;
}

void agregar(char tipo){
    int opc;
    cout<<"A que tipo de sala? \n\t1) Grande\n\t2) Mediana"<<endl;
    cin>>opc;
    switch(opc){
        case 1:{
            cout<<"En cual sala? \n1) SALA 1\n2) SALA 2"<<endl;
            cin>>opc;
            if(opc>=1&&opc<=2){
                if(tipo=='P'){
                    cine.Registrar(opc-1,'G',1);}
                else if(tipo=='H'){
                    cine.Registrar(opc-1,'G',2);}
            }
            else
                cout<<"esa sala no existe"<<endl;
            break;
        }
        case 2:{
            cout<<"En cual sala? \n1) SALA 1\n2) SALA 2\n3) SALA 3\n4) SALA 4\n5) SALA 5"<<endl;
            cin>>opc;
            if(opc>=1&&opc<=5){
                if(tipo=='P'){
                    cine.Registrar(opc-1,'M',1);}
                else if(tipo=='H'){
                    cine.Registrar(opc-1,'M',2);}
            }
            else
                cout<<"esa sala no existe"<<endl;
            break;
        }
    }
}

