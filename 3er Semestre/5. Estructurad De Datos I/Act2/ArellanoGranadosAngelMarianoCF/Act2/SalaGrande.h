#ifndef SALAGRANDE_H
#define SALAGRANDE_H

#include "Sala.h"
#include "Asiento.h"

#include<iostream>
#include<string>
#include <sstream>
using namespace std;

class SalaGrande :public  Sala
{
    private:
        int contAsientos=0;//140 max
        Asiento asientos [10][14][5];
    public:
        SalaGrande();
        void EliminarAsientos();
        void AsignarAsiento(int,char);
        void BuscaId(int);
        void BuscaNombre(string);
};

#endif // SALAGRANDE_H
