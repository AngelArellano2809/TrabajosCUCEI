#include "Libro.h"

Libro::Libro()
{
    //ctor
}

void Libro::setNombre(string N){
    this->nombre=N;
}

void Libro::setAutor(string N){
    this->autor=N;
}

void Libro::setEditorial(string N){
    this->editorial=N;
}

void Libro::setIsbn(string N){
    this->isbn=N;
}

void Libro::setCategoria(string N){
    this->categoria=N;
}

void Libro::setCategoriaSec(string N){
    this->categoriaSec=N;
}

void Libro::setEjemDisp(int N){
    this->ejemDisp=N;
}

void Libro::setEjemVend(int N){
    this->ejemVend=N;
}

void Libro::setPrecio(float N){
    this->precio=N;
}
string Libro::getNombre(){
    return nombre;
}

string Libro::getAutor(){
    return autor;
}

string Libro::getEditorial(){
    return  editorial;
}

string Libro::getIsbn(){
    return isbn;
}

string Libro::getCategoria(){
    return categoria;
}

string Libro::getCategoriaSec(){
    return categoriaSec;
}

int Libro::getEjemDisp(){
    return ejemDisp;
}

int Libro::getEjemVend(){
    return ejemVend;
}

float Libro::getPrecio(){
    return precio;
}
