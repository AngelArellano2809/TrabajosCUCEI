#include "Menu.h"

Menu::Menu(){
    //ctor
}

int Menu::menuPrincipal(){
    int opc;
    cout<<"\tMENU"<<endl;
    cout<<"1. Capturar Pasajeros"<<endl;//
    cout<<"2. Modificar Pasajeros"<<endl;//
    cout<<"3. Mostrar Pasajeros"<<endl;//
    cout<<"4. Capturar Vuleos"<<endl;//
    cout<<"5. Modificar Vuelos"<<endl;//
    cout<<"6. Mostrar Vuelos"<<endl;//
    cout<<"7. Eliminar Vuelos"<<endl;//
    cout<<"8. Eliminar Pasajeros"<<endl;
    cout<<"9. Ordenar Vuelos por Asientos Disponibles"<<endl;
    cout<<"0. Salir"<<endl;
    cout<<"Seleccione una opcion"<<endl;
    cin>>opc;
    return opc;
}
