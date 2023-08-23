#ifndef MENUCIRCULAR_H
#define MENUCIRCULAR_H

#include <windows.h>
#include <iostream>
using namespace std;

#include "ListaCircular.h"

class MenuCircular
{
    public:
        MenuCircular();
        void inserta(string);
        void subir();
        void bajar();
        int ingresa();
        void gotoxy(int x,int y);
        void M();
    private:
        class Opcion {
            public:
                string opcion;
                int id;
                Opcion *next;
                Opcion *back;
        };
        Opcion *ptrHead;
        Opcion *selecc;
        int cont=1;
};

#endif // MENUCIRCULAR_H
