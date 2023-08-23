#ifndef PASAJERO_H
#define PASAJERO_H
#include <iostream>
#include <stdlib.h>
using namespace std;


class Pasajero
{
    public:
        Pasajero();
        Pasajero(string,string,int,string,string,int);
        string getNombre();
        void show();

    protected:

    private:
        string apellido;
        string nombre;
        int edad;
        string ciudadOrigen;
        string ciudadDestino;
        int asiento;
};

#endif // PASAJERO_H
