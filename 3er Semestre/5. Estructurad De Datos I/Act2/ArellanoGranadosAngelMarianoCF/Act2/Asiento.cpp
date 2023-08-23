#include "Asiento.h"

Asiento::Asiento()
{
    //ctor
}

Asiento::Asiento(string sala,float horario,string name,char fil, int col)
{
    this->sala=sala;
    this->horario=horario;
    this->cliente=Cliente(name);
    this->ocupado=true;
    this->fila=fil;
    this->columna=col;
}

Asiento::~Asiento()
{
    //dtor
}

bool Asiento::getOcupado(){
    return ocupado;
}

int Asiento::getId(){
    return cliente.getId();
}

string Asiento::getNombre(){
    return cliente.getNombre();
}

string Asiento::Detalles(){
    stringstream cad;
    cad<<"Detalles Del Boleto:"<<endl<<"Nombre: "<<cliente.getNombre()<<endl<<"ID: "<<cliente.getId()<<endl<<"Sala: "<<sala<<endl<<"Asiento: "<<fila<<columna<<endl<<"Horario: "<<horario<<endl;
    return cad.str();
}
