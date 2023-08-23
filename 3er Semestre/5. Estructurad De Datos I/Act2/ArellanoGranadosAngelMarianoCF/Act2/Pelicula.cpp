#include "Pelicula.h"

Pelicula::Pelicula()
{
    //ctor
}

Pelicula::Pelicula(string nombre,string director, int duracion){
    this->nombre=nombre;
    this->director=director;
    this->duracion=duracion;
}

int Pelicula::getDuracion(){
    return this->duracion;
}

string Pelicula::getNombre(){
    return this->nombre;
}
