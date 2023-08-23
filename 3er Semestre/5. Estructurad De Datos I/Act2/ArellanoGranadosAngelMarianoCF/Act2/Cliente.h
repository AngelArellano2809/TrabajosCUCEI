#ifndef CLIENTE_H
#define CLIENTE_H

#include <iostream>
using namespace std;

class Cliente
{
    private:
        string nombre;
        int id;
    public:
        Cliente();
        Cliente(string name);
        string getNombre();
        int getId();
};

#endif // CLIENTE_H
