#ifndef LISTA_H
#define LISTA_H

#include "Libro.h"

#include <iostream>
using namespace std;

class Lista
{
    public:
        Lista();
        void inserta();
        void inserta10(string,string,string,string,string,string,int,float);
        int buscar();
        void mostrar(int);
        void modificar();
        void eliminar(int);
        void ventas(int);
        int getCont();
    private:
        Libro libros[100];
        int cont;
};

#endif // LISTA_H
