#ifndef SALAMEDIANA_H
#define SALAMEDIANA_H

#include "Sala.h"
#include "Asiento.h"

#include<iostream>
#include<string>
#include <sstream>
using namespace std;

class SalaMediana  : public Sala
{
    private:
        int contAsientos=0;//56 max
        Asiento asientos[7][8][5];
    public:
        SalaMediana();
        void EliminarAsientos();
        void AsignarAsiento(int,char);
        void BuscaId(int);
        void BuscaNombre(string);
};

#endif // SALAMEDIANA_H
