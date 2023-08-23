#include <windows.h>
#include <iostream>
#include<conio.h>
#include <stdio.h>

using namespace std;

#include "MenuCircular.h"
#include "ListaCircular.h"

#define UP 72
#define DOWN 80
#define DER 77
#define IZQ 75
#define ENTER 13
#define SPACE 32

#pragma comment(lib, "Winmm.lib")

//linker settings -lwinmm

  void ShowConsoleCursor(bool showFlag){
    HANDLE out = GetStdHandle(STD_OUTPUT_HANDLE);

    CONSOLE_CURSOR_INFO     cursorInfo;

    GetConsoleCursorInfo(out, &cursorInfo);
    cursorInfo.bVisible = showFlag; // set the cursor visibility
    SetConsoleCursorInfo(out, &cursorInfo);
}

//TOCAR CANCION
bool first=false;
void playSong(string  song,int flag){
/*
    char soundfile1[]="open \"C:/SEDDI/musicProject/1x1.mp3\" type mpegvideo alias mp3";
    string meh;
    //open \"C:/SEDDI/musicProject/1x1.mp3\" type mpegvideo alias mp3
    strcpy(soundfile1,song.c_str());
    mciSendString((LPCSTR)soundfile1, NULL, 0, NULL);
    if (!first){
        mciSendString("play mp3", NULL, 0, NULL);
        first=true;
        return;
    }
    if(flag==-1){
    mciSendString("pause mp3", NULL, 0, NULL);
    }
    if(flag==1){
    mciSendString("resume mp3", NULL, 0, NULL);
    }
*/
    if(flag==1){
        PlaySound(song.c_str() , NULL, SND_ASYNC); //SND_FILENAME or SND_LOOP
    }
    if(flag==-1){
        PlaySound(NULL, 0, 0);
    }
    else{
        PlaySound(NULL, 0, 0);
    }

}

int main()
{

    MenuCircular mc;
    ListaCircular lc;

    char  tecla;
    bool repite=true;
    int pos,play=-1,ch;

    do{
        int opc=0;
        ShowConsoleCursor(false);
        mc.M();
        mc.gotoxy(2,26);cout<<"CANCION EN REPRODUCCION:";
        if(!lc.empty()){
            mc.gotoxy(30,1);cout<<"LISTA DE CANCIONES";
            mc.gotoxy(1,2);printf("%c%c%c%c",201,205,205,203);for(int i=0;i<13;i++){printf("%c",205);}printf("%c",203);for(int i=0;i<15;i++){printf("%c",205);}printf("%c",203);
                        for(int i=0;i<13;i++){printf("%c",205);}printf("%c",203);for(int i=0;i<10;i++){printf("%c",205);}printf("%c",203);for(int i=0;i<22;i++){printf("%c",205);}printf("%c",187);
            mc.gotoxy(1,3);printf("%c",186);cout<<"N ";printf("%c",186);cout<<"    NOMBRE   ";printf("%c",186);cout<<"     ALBUM     ";printf("%c",186);cout<<"   ARTISTA   ";
                        printf("%c",186);cout<<"  GENERO  ";printf("%c",186);cout<<"      DIRECCION       ";printf("%c",186);
            mc.gotoxy(1,4);printf("%c%c%c%c",204,205,205,206);for(int i=0;i<13;i++){printf("%c",205);}printf("%c",206);for(int i=0;i<15;i++){printf("%c",205);}printf("%c",206);
                        for(int i=0;i<13;i++){printf("%c",205);}printf("%c",206);for(int i=0;i<10;i++){printf("%c",205);}printf("%c",206);for(int i=0;i<22;i++){printf("%c",205);}printf("%c",185);

            for(int i=5;i<=23;i++){
                mc.gotoxy(1,i);printf("%c",186);cout<<"  ";printf("%c",186);cout<<"             ";printf("%c",186);cout<<"               ";printf("%c",186);cout<<"             ";
                        printf("%c",186);cout<<"          ";printf("%c",186);cout<<"                      ";printf("%c",186);
            }
            mc.gotoxy(1,24);printf("%c%c%c%c",200,205,205,202);for(int i=0;i<13;i++){printf("%c",205);}printf("%c",202);for(int i=0;i<15;i++){printf("%c",205);}printf("%c",202);
                        for(int i=0;i<13;i++){printf("%c",205);}printf("%c",202);for(int i=0;i<10;i++){printf("%c",205);}printf("%c",202);for(int i=0;i<22;i++){printf("%c",205);}printf("%c",188);

            //Lista de Canciones
            for(int j=5;j<lc.getCont()+5;j++){
                mc.gotoxy(2,j);cout<<j-4;
                mc.gotoxy(5,j);cout<<lc.getNombre(j-5).substr(0, 13);
                mc.gotoxy(19,j);cout<<lc.getAlbum(j-5).substr(0, 15);
                mc.gotoxy(35,j);cout<<lc.getArtista(j-5).substr(0, 13);
                mc.gotoxy(49,j);cout<<lc.getGenero(j-5).substr(0, 10);
                mc.gotoxy(60,j);cout<<lc.getDirecc(j-5).substr(0, 22);
            }
            //Reproductor
            mc.gotoxy(2,27);cout<<lc.getNombre(lc.findSelecc());
            mc.gotoxy(2,28);cout<<lc.getAlbum(lc.findSelecc());
            mc.gotoxy(2,29);cout<<lc.getArtista(lc.findSelecc());
        }
        else{
            mc.gotoxy(30,1);cout<<"NO HAY CANCIONES REGISTRADAS";
            mc.gotoxy(2,27);cout<<"NO HAY CANCIONES REGISTRADAS";
        }
        tecla = getch();
        switch (tecla) {
            case UP:{
                mc.subir();
            }break;
            case DOWN:{
                mc.bajar();
            }break;
            case ENTER:{
                 opc=mc.ingresa();
            }break;
            case DER:{
                if(!lc.empty())
                    lc.sig();
            }break;
            case IZQ:{
                if(!lc.empty())
                    lc.prev();
            }break;
            case SPACE:{
                if(!lc.empty()){
                    play=play*-1;
                    playSong(lc.getSong(),play);
                }
            }break;
        }
        switch (opc){
            case 0:{
            }break;
            case 1:{
                string nombre, album, artista, genero,direcc;
                mc.gotoxy(84,26);cout<<"Ingresa el nombre:       "<<endl;
                mc.gotoxy(84,27);cout<<">>                       ";mc.gotoxy(86,27);getline(cin,nombre);
                mc.gotoxy(84,26);cout<<"Ingresa el album:        "<<endl;
                mc.gotoxy(84,27);cout<<">>                       ";mc.gotoxy(86,27);getline(cin,album);
                mc.gotoxy(84,26);cout<<"Ingresa el artista:      "<<endl;
                mc.gotoxy(84,27);cout<<">>                       ";mc.gotoxy(86,27);getline(cin,artista);
                mc.gotoxy(84,26);cout<<"Ingresa el genero:       "<<endl;
                mc.gotoxy(84,27);cout<<">>                       ";mc.gotoxy(86,27);getline(cin,genero);
                mc.gotoxy(84,26);cout<<"Ingresa la direccion:    "<<endl;
                mc.gotoxy(84,27);cout<<">>                       ";mc.gotoxy(86,27);getline(cin,direcc);
                lc.insgresar(nombre,album,artista,genero,direcc);
            }break;
            case 2:{
                lc.insgresar("Star","12_00","LOONA","Dance","C:/Users/Usuario/Downloads/Star.wav");
                lc.insgresar("Bang","OkOrchesta","AJR","Synth","C:/Users/Usuario/Downloads/Bang.wav");
                lc.insgresar("InstantCrush","RAM","DaftPunk","Elect","C:/Users/Usuario/Downloads/InstantCrush.wav");
                lc.insgresar("FeelItStill","WoodStock","PTM","Alt","C:/Users/Usuario/Downloads/FeelItStill.wav");
                lc.insgresar("TheOutside","ScaleAndIcy","TOP","Alt","C:/Users/Usuario/Downloads/TheOutside.wav");
            }break;
            case 3:{
                mc.gotoxy(84,26);cout<<"Que cancion se eliminara? "<<endl;
                mc.gotoxy(84,27);cout<<">>";cin>>pos;
                lc.remove(pos);
            }break;
            case 4:{
                string str;
                mc.gotoxy(84,26);cout<<"Que cancion se editara?   "<<endl;
                mc.gotoxy(84,27);cout<<">>                        ";mc.gotoxy(86,27);cin>>pos;
                mc.gotoxy(84,26);cout<<"Que dato?1=nombre/2=album/"<<endl;
                mc.gotoxy(84,27);cout<<"3=artista/4=genero/5=direc"<<endl;
                mc.gotoxy(84,28);cout<<">>                        ";mc.gotoxy(86,28);cin>>ch;
                mc.gotoxy(84,26);cout<<"Ingresa el nuevo dato:    "<<endl;
                mc.gotoxy(84,27);cout<<">>                        ";
                mc.gotoxy(84,28);cout<<"                          ";mc.gotoxy(86,27);cin>>str;
                lc.edit(pos,ch,str);
            }break;
            case 5:{
                lc.invert();
            }break;
            case 6:{
                lc.remove(1);
            }break;
            case 7:{
                lc.remove(lc.getCont());
            }break;
            case 8:{
                repite = false;
            }break;
        }
    }while(repite);
    //mc.gotoxy(84,26);cout <<"Stan LOONA!" << endl;
    return 0;
}
