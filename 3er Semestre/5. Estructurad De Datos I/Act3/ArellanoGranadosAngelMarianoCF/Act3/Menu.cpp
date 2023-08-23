#include "Menu.h"

Menu::Menu()
{
    //ctor
}

Menu::~Menu()
{
    //dtor
}

int Menu::menuPrincipal(){
    int opc;
    cout<<"1.- Ingresar Nuevo Libro"<<endl;
    cout<<"2.- Buscar y Mostrar"<<endl;
    cout<<"3.- Modificar Informacion de Libro"<<endl;
    cout<<"4.- Ventas"<<endl;
    cout<<"5.- Mostrar Todo"<<endl;
    cout<<"6.- Eliminar del Catalogo"<<endl;
    cout<<"7.- Crear 10 Libros"<<endl;
    cout<<"0.- Salir"<<endl;
    cout<<"Seleciona una opcion: "<<endl;
    cin>>opc;
    return opc;
}
