#ifndef AEROPUERTO_H
#define AEROPUERTO_H

#include<Lista.h>
#include<Vuelos.h>

class Aeropuerto
{
    public:
        Aeropuerto();
        void addVuelo();
        void modVuelo();
        void removeVuelo();
        void printVuelo();
        void selecVuelo();
        void selecPasajero();

        void addPasajero();
        void modPasajero();
        void printPasajero();
        void removePasajero();
        void ordena();

    protected:

    private:
        List <Vuelos> LV;
};

#endif // AEROPUERTO_H
