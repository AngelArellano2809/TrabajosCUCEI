#include "Vuelos.h"

Vuelos::Vuelos()
{
    //ctor
}
Vuelos::Vuelos(string CO, string CD, string FS, string FA, int DV, int CP, int CC)
{
    this->cuidadOrigen=CO;
    this->cuidadDestino=CD;
    this->fechaSalida=FS;
    this->fechaArribo=FA;
    this->distanciaVuelo=DV;
    this->capacidadPasajeros=CP;
    this->capacidadCarga=CC;
    this->asientosDisp=CP;
}

void Vuelos::venderPasaje()
{
    string AP,NO,CO,CD;
    int ED,A;
    cout<<"Apellido:"<<endl;
    cin>>AP;
    cout<<"Nombre"<<endl;
    cin>>NO;
    cout<<"Edad"<<endl;
    cin>>ED;
    cout<<"Ciudad de Origen"<<endl;
    cin>>CO;
    cout<<"Ciudada de Destino"<<endl;
    cin>>CD;
    cout<<"Asiento"<<endl;
    cin>>A;
    LP.Add(Pasajero(AP,NO,ED,CO,CD,A));
}
void Vuelos::show()
{
    cout<<endl;
    cout<<"Cuidad de Oirgen: "<<cuidadOrigen<<endl;
    cout<<"Ciudad de Destino: "<<cuidadDestino<<endl;
    cout<<"Fecha de Salida: "<<fechaSalida<<endl;
    cout<<"Fecha de Arribo: "<<fechaArribo<<endl;
    cout<<"Distancia de Vuelo: "<<distanciaVuelo<<endl;
    cout<<"Capacidad de pasajeros: "<<capacidadPasajeros<<endl;
    cout<<"Capacidad de Carga: "<<capacidadCarga<<endl;
    cout<<"Asientos Disponibles: "<<asientosDisp<<endl;
    cout<<endl;
}

string Vuelos::getNombre(){
    return cuidadOrigen;
}

List <Pasajero> Vuelos::getLP()
{
    return LP;
}

void Vuelos::modPasaje()
{
    string AP,NO,CO,CD;
    int ED,A;
    cout<<"Apellido:"<<endl;
    cin>>AP;
    cout<<"Nombre"<<endl;
    cin>>NO;
    cout<<"Edad"<<endl;
    cin>>ED;
    cout<<"Ciudad de Origen"<<endl;
    cin>>CO;
    cout<<"Ciudada de Destino"<<endl;
    cin>>CD;
    cout<<"Asiento"<<endl;
    cin>>A;
    LP.modif(Pasajero(AP,NO,ED,CO,CD,A));
}

void Vuelos::removePasajero()
{
    LP.remove();
}

int Vuelos::getAsientosDisp()
{
    return asientosDisp;
}
