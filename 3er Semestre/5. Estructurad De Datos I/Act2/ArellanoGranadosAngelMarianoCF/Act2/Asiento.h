#ifndef ASIENTO_H
#define ASIENTO_H

#include "Sala.h"
#include "Cliente.h"

#include<iostream>
#include<string>
#include <sstream>
using namespace std;

class Asiento
{
    private:
        string sala;
        float horario;
        Cliente cliente;
        bool ocupado=false;
        char fila;
        int columna;
    public:
        Asiento();
        Asiento(string sala,float horario,string name,char,int);
        virtual ~Asiento();
        int getId();
        string getNombre();
        bool getOcupado();
        string Detalles();
};

#endif // ASIENTO_H
