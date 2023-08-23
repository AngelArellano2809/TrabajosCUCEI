#ifndef LISTACIRCULAR_H
#define LISTACIRCULAR_H

#include <windows.h>
#include <iostream>
using namespace std;

class ListaCircular
{
    public:
        ListaCircular();
        ~ListaCircular();
        void insgresar(string,string,string,string,string );
        bool empty();
        int getCont();
        int getId(int);
        string getNombre(int);
        string getAlbum(int);
        string getArtista(int);
        string getGenero(int);
        string getDirecc(int);
        void remove(int);
        void search (int pos);
        void edit (int pos,int tipo,string newStr);
        void invert();
        void sig();
        void prev();
        string  getSong();
        int findSelecc();
    private:
        class Song {
            public:
                string nombre;
                string album;
                string artista;
                string genero;
                string direcc;
                int id;
                Song *next;
                Song *back;
        };
        int cont=0;
        Song *ptrHead;
        Song *selecc;
};



#endif // LISTACIRCULAR_H
