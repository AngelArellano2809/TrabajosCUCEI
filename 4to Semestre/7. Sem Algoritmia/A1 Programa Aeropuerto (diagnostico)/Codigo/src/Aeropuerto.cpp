#include "Aeropuerto.h"

Aeropuerto::Aeropuerto()
{
    //ctor
}

void Aeropuerto::addVuelo()
{
    string CO,CD,FS,FA;
    int DV,CP,CC;
    cout<<"Ciudad de Origen:"<<endl;
    cin>>CO;
    cout<<"Ciudad Destino"<<endl;
    cin>>CD;
    cout<<"Fecha de Salida"<<endl;
    cin>>FS;
    cout<<"Fecha de Arribo"<<endl;
    cin>>FA;
    cout<<"Distancia de Vuelo"<<endl;
    cin>>DV;
    cout<<"Capacidad de Pasajeros"<<endl;
    cin>>CP;
    cout<<"Capacidad de Carga"<<endl;
    cin>>CC;
    LV.Add(Vuelos(CO,CD,FS,FA,DV,CP,CC));
}

void Aeropuerto::modVuelo()
{
    selecVuelo();
    string CO,CD,FS,FA;
    int DV,CP,CC;
    cout<<endl;
    cout<<"Ciudad de Origen:"<<endl;
    cin>>CO;
    cout<<"Ciudad Destino"<<endl;
    cin>>CD;
    cout<<"Fecha de Salida"<<endl;
    cin>>FS;
    cout<<"Fecha de Arribo"<<endl;
    cin>>FA;
    cout<<"Distancia de Vuelo"<<endl;
    cin>>DV;
    cout<<"Capacidad de Pasajeros"<<endl;
    cin>>CP;
    cout<<"Capacidad de Carga"<<endl;
    cin>>CC;
    LV.modif(Vuelos(CO,CD,FS,FA,DV,CP,CC));
}

void Aeropuerto::removeVuelo()
{
    selecVuelo();
    LV.remove();
}

void Aeropuerto::printVuelo()
{
    LV.print();
}

void Aeropuerto::selecVuelo()
{
    if(!LV.Empty()){
          string CO;
          LV.print();
          cout<<"Ingrese la Ciudad de Origen del Vuelo:"<<endl;
          cin>>CO;
          LV.buscar(CO);
      }
}

void Aeropuerto::addPasajero()
{
    selecVuelo();
    LV.getList().getElem().venderPasaje();
}

void Aeropuerto::modPasajero()
{
    selecPasajero();
    LV.getList().getElem().modPasaje();

}

void Aeropuerto::printPasajero()
{
    selecVuelo();
    LV.getList().getElem().getLP().print();
}

void Aeropuerto::removePasajero()
{
    selecPasajero();
    LV.getList().getElem().removePasajero();
}

void Aeropuerto::selecPasajero()
{
    selecVuelo();
    if(!LV.getList().getElem().getLP().Empty()){
          string NO;
          LV.getList().getElem().getLP().print();
          cout<<"Ingrese El Nombre del Pasajero:"<<endl;
          cin>>NO;
          LV.getList().getElem().getLP().buscar(NO);
      }
}

void Aeropuerto::ordena()
{
    LV.arregloApunt();
}

