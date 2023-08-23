#include "MenuCircular.h"

void MenuCircular::gotoxy(int x,int y){
      HANDLE hcon;
      hcon = GetStdHandle(STD_OUTPUT_HANDLE);
      COORD dwPos;
      dwPos.X = x;
      dwPos.Y= y;
      SetConsoleCursorPosition(hcon,dwPos);
 }

MenuCircular::MenuCircular()
{
    ptrHead = NULL;
    inserta("1) ISERTAR CANCION");
    inserta("2) CARGAR CANCIONES");
    inserta("3) ELIMINAR CANCION");
    inserta("4) EDITAR CANCION");
    inserta("5) INVERTIR LISTA");
    inserta("6) ELIMINAR PRIMERA");
    inserta("7) ELIMINAR ULTIMA");
    inserta("8) SALIR");
    selecc=ptrHead;
}


void MenuCircular::inserta(string opc) {
    Opcion *new_opc = new Opcion();
    new_opc->opcion = opc;
    new_opc->id=cont;
    if (ptrHead == NULL){
        new_opc->next = new_opc;
        new_opc->back = new_opc;
        ptrHead = new_opc;
    }
    else{
        Opcion *last_opc = ptrHead->back;
        new_opc->next = ptrHead;
        new_opc->back = last_opc;
        ptrHead->back = new_opc;
        last_opc->next = new_opc;
    }
    cont++;
}

void MenuCircular::M(){
    Opcion *temp = ptrHead;
            //Marco 110
        gotoxy(0,0);printf("%c",201);for(int i=0;i<82;i++)printf("%c",205);printf("%c",203);for(int i=0;i<26;i++)printf("%c",205);printf("%c",187);
        for(int i=1;i<=24;i++){
            gotoxy(0,i);printf("%c",186);for(int i=0;i<82;i++)printf("%c",' ');printf("%c",186);for(int i=0;i<26;i++)printf("%c",' ');printf("%c",186);
        }
        gotoxy(0,25);printf("%c",204);for(int i=0;i<82;i++)printf("%c",205);printf("%c",206);for(int i=0;i<26;i++)printf("%c",205);printf("%c",185);
        for(int i=26;i<=29;i++){
            gotoxy(0,i);printf("%c",186);for(int i=0;i<82;i++)printf("%c",' ');printf("%c",186);for(int i=0;i<26;i++)printf("%c",' ');printf("%c",186);
        }
        gotoxy(0,30);printf("%c",200);for(int i=0;i<82;i++)printf("%c",205);printf("%c",202);for(int i=0;i<26;i++)printf("%c",205);printf("%c",188);

    //Menu
        gotoxy(84,1);cout<<"   REPRODUCTOR DE MUSICA";
        gotoxy(84,3);cout<<"     MENU DE OPCIONES";
        for(int i=5;i<=19;i=i+2){
                if(temp==selecc){
                    gotoxy(84,i);cout<<">> "<<temp->opcion;}
                else{
                    gotoxy(84,i);cout<<"   "<<temp->opcion;}
                temp = temp->next;
        }
    for(int k=26;k<30;k++){
        gotoxy(84,k);for(int i=0;i<26;i++)printf("%c",' ');
    }
}

void MenuCircular::subir(){
    selecc=selecc->back;
}

void MenuCircular::bajar(){
    selecc=selecc->next;
}

int MenuCircular::ingresa(){
    return selecc->id;
}
