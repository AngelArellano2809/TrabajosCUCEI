#ifndef SALA_H
#define SALA_H

#include "Pelicula.h"
#include "Cliente.h"

#include<iostream>
#include<string>
using namespace std;

class Sala
{
    private:
        Pelicula pelicula;
        float horarios[5];//-1 no hay horarios
        int cont=0;//contador de horarios registrados
        bool uso=false;
    public:
        Sala();
        virtual ~Sala();
        void AgregarPelicula();
        void AgregarHorario();
        void MostrarPelicula(char,int);
        void EliminarPelicula();
        int getHorario();
        bool getUso();
        int getCont();
        float getHorarioF(int);
        string getPelicula();
        char Letra(int);
        int Numero(char);
};

#endif // SALA_H
