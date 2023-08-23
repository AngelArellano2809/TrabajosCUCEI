#include <iostream>
#include <stdlib.h>
using namespace std;

#include<Vuelos.h>
#include<Menu.h>
#include<Pasajero.h>
#include<Aeropuerto.h>
#include<Lista.h>

Menu menu;
Aeropuerto aero;

int main(){
    int opc;
    do{
        opc=menu.menuPrincipal();
        switch(opc){
            case 1:{
                aero.addPasajero();
            }break;
            case 2:{
                aero.modPasajero();
            }break;
            case 3:{
                aero.printPasajero();
            }break;
            case 4:{
                aero.addVuelo();//
            }break;
            case 5:{
                aero.modVuelo();
            }break;
            case 6:{
                aero.printVuelo();//
            }break;
            case 7:{
                aero.removeVuelo();
            }break;
            case 8:{
                aero.removePasajero();
            }break;
            case 9:{
                aero.ordena();
            }break;
        }
    }while(opc);
    cout << "Hello world!" << endl;
    return 0;
}
