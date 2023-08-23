#ifndef VUELOS_H
#define VUELOS_H
#include <iostream>
#include <stdlib.h>
using namespace std;

#include<Lista.h>
#include<Pasajero.h>

class Vuelos
{
    public:
        Vuelos();
        Vuelos(string,string,string,string,int,int,int);
        void show();
        string getNombre();
        List <Pasajero> getLP();
        void venderPasaje();
        void modPasaje();
        void removePasajero();
        int getAsientosDisp();

    private:
        List <Pasajero> LP;

        string cuidadOrigen;//nombre
        string cuidadDestino;
        string fechaSalida;//investigar
        string fechaArribo;
        int distanciaVuelo;
        int capacidadPasajeros;
        int capacidadCarga;
        int asientosDisp;
};

#endif // VUELOS_H
