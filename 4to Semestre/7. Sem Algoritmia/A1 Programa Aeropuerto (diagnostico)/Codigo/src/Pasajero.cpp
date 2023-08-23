#include "Pasajero.h"

Pasajero::Pasajero()
{
    //ctor
}
Pasajero::Pasajero(string AP, string NO, int ED, string CO, string CD, int A)
{
    this->apellido=AP;
    this->nombre=NO;
    this->edad=ED;
    this->ciudadOrigen=CO;
    this->ciudadDestino=CD;
    this->asiento=A;
}

void Pasajero::show()
{
    cout<<endl;
    cout<<"Apellido: "<<apellido<<endl;
    cout<<"Nombre: "<<nombre<<endl;
    cout<<"Edad: "<<edad<<endl;
    cout<<"Cuidad de Origen: "<<ciudadOrigen<<endl;
    cout<<"Cuidad de Destino: "<<ciudadDestino<<endl;
    cout<<"Asiento: "<<asiento<<endl;
    cout<<endl;
}

string Pasajero::getNombre()
{
    return nombre;
}
