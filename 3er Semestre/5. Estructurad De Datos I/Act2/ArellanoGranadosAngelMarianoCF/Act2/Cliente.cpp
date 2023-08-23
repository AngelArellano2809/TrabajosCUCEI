#include "Cliente.h"

Cliente::Cliente()
{
    //ctor
}

Cliente::Cliente(string name)
{
    this->nombre=name;
    this->id=1+rand()%1000;
}

string Cliente::getNombre(){
    return nombre;
}

int Cliente::getId(){
    return id;
}
