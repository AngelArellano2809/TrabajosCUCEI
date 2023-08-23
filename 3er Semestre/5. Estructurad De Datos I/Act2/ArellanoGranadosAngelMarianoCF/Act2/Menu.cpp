#include "Menu.h"


Menu::Menu(){
}

int Menu::menuPrincipal(){
    int opc;
    cout<<"\tMENU"<<endl;
    cout<<"1. Mostrar catalogo"<<endl;
    cout<<"2. Vender un ticket"<<endl;
    cout<<"3. Buscar y mostrar cliente"<<endl;
    cout<<"4. Agregar Pelicula o Horario a Sala"<<endl;
    cout<<"5. Eliminar Pelicula de una sala"<<endl;
    cout<<"0. Salir"<<endl;
    cout<<"Seleccione una opcion"<<endl;
    cin>>opc;
    return opc;
}
int Menu::menuBusca(){
    int opc;
    cout<<"\t1. Buscar por id"<<endl;
    cout<<"\t2. Buscar por nombre"<<endl;
    cout<<"\t0. Salir"<<endl;
    cin>>opc;
    return opc;
}

int Menu::menuAgrega(){
    int opc;
    cout<<"\t1. Agregar Pelicula a Sala"<<endl;
    cout<<"\t2. Agregar Horario a Pelicula"<<endl;
    cin>>opc;
    return opc;
}
