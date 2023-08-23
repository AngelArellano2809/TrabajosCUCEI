#ifndef CINE_H
#define CINE_H

#include "SalaGrande.h"
#include "SalaMediana.h"
class Cine
{
    private:
        SalaGrande salaG[2];
        SalaMediana salaM[5];
    public:
        Cine();
        void Registrar(int pos,char tipo,int opc);
        void MostrarTodo();
        void eliminar(int,char);
        void venderAsiento(int,char);
        void BuscarId(int);
        void BuscarNombre(string);
};

#endif // CINE_H
