#ifndef PELICULA_H
#define PELICULA_H

#include <iostream>
using namespace std;

class Pelicula
{
    private:
        string nombre;
        string director;
        int duracion;//minutos
    public:
        Pelicula();
        Pelicula(string nombre,string director, int duracion);
        int getDuracion();
        string getNombre();
};

#endif // PELICULA_H
