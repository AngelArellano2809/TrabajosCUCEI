#ifndef LIBRO_H
#define LIBRO_H

#include <iostream>
using namespace std;

class Libro
{
    public:
        Libro();
        void setNombre(string);
        void setAutor(string);
        void setEditorial(string);
        void setIsbn(string);
        void setCategoria(string);
        void setCategoriaSec(string);
        void setEjemDisp(int);
        void setEjemVend(int);
        void setPrecio(float);
        string getNombre();
        string getAutor();
        string getEditorial();
        string getIsbn();
        string getCategoria();
        string getCategoriaSec();
        int getEjemDisp();
        int getEjemVend();
        float getPrecio();
    private:
        string nombre;
        string autor;
        string editorial;
        string isbn;
        string categoria;
        string categoriaSec;
        int ejemDisp;
        int ejemVend;
        float precio;
};

#endif // LIBRO_H
