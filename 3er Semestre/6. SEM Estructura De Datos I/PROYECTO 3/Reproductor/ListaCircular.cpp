#include "ListaCircular.h"

ListaCircular::ListaCircular(){
    ptrHead = NULL;
}

ListaCircular::~ListaCircular(){
    if (ptrHead != NULL) {
        Song *temp = ptrHead->next;
        Song *temp_ptrHead;
        while (temp != ptrHead){
            temp_ptrHead = temp;
            temp = temp->next;
            delete temp_ptrHead;
        }
        delete ptrHead;
    }
}

void ListaCircular::insgresar(string nombre,string album,string artista,string genero,string  direcc) {
    Song *new_node = new Song();
    Song *temp=ptrHead;
    for(int i=0;i<cont;i++){
        if(direcc==temp->direcc){
            return;
        }
        temp=temp->next;
    }
    new_node->id = cont+1;
    new_node->nombre = nombre;
    new_node->album = album;
    new_node->artista = artista;
    new_node->genero  = genero;
    new_node->direcc = direcc;
    /*for(int i=0;i<40;i++){
        new_node->direcc[i]=direcc[i];
    }*/
    if (ptrHead == NULL){
        new_node->next = new_node;
        new_node->back = new_node;
        ptrHead = new_node;
        selecc=ptrHead;
    }
    else{
        Song *last_node = ptrHead->back;
        new_node->next = ptrHead;
        new_node->back = last_node;
        ptrHead->back = new_node;
        last_node->next = new_node;
    }
    cont++;
}

bool ListaCircular::empty() {
    if (ptrHead == NULL)
        return true;
    else
        return false;
}

void ListaCircular::remove(int position){
    if (position <= cont){
        if (position == 1){
            if (cont == 1){
                delete ptrHead;
                ptrHead = NULL;
                selecc = NULL;
            }
            else{
                if(selecc==ptrHead){
                    selecc=ptrHead->next;
                }
                Song *temp_ptrHead = ptrHead;
                Song *last_node = ptrHead->back;
                ptrHead = ptrHead->next;
                last_node->next = ptrHead;
                ptrHead->back = last_node;
                delete temp_ptrHead;
            }
        }
        else {
            Song *temp = ptrHead;
            for (int f = 1; f <= position- 1; f++){
                temp = temp->next;
            }
            Song *temp_ptrHead = temp;
            Song *back = temp->back;
            temp = temp->next;
            back->next = temp;
            temp->back = back;
            delete temp_ptrHead;
        }
        cont--;
    }
}

void ListaCircular::invert(){
    if(ptrHead != NULL) {
        Song* prevNode = ptrHead;
        Song* tempNode = ptrHead;
        Song* curNode = ptrHead->next;

        prevNode->next = prevNode;

        while(curNode != ptrHead) {
            tempNode = curNode->next;
            curNode->next = prevNode;
            ptrHead->next = curNode;
            prevNode = curNode;
            curNode = tempNode;
        }
        ptrHead = prevNode;
    }
}

void ListaCircular::edit (int pos,int tipo,string newStr){
    int aux=1;
    if (!empty()){
        Song *temp = ptrHead;
        do {
            temp = temp->next;
            aux++;
        } while (aux!=pos);

        switch(tipo){
            case 1:{
                temp->nombre=newStr;
            }break;
            case 2:{
                temp->album=newStr;
            }break;
            case 3:{
                temp->artista=newStr;
            }break;
            case 4:{
                temp->genero=newStr;
            }break;
            case 5:{
                temp->direcc=newStr;
            }break;
        }
    }
}

int ListaCircular::getCont(){
    return cont;
}

int ListaCircular::getId(int pos){
    Song *temp = ptrHead;
    for (int i=0;i<pos;i++){
        temp=temp->next;
    }
    return temp->id;
}

string ListaCircular::getNombre(int id){
    Song *temp = ptrHead;
    for (int i=0;i<id;i++){
        temp=temp->next;
    }
    return temp->nombre;
}

string ListaCircular::getAlbum(int id){
    Song *temp = ptrHead;
    for (int i=0;i<id;i++){
        temp=temp->next;
    }
    return temp->album;
}

string ListaCircular::getArtista(int id){
    Song *temp = ptrHead;
    for (int i=0;i<id;i++){
        temp=temp->next;
    }
    return temp->artista;
}

string ListaCircular::getGenero(int id){
    Song *temp = ptrHead;
    for (int i=0;i<id;i++){
        temp=temp->next;
    }
    return temp->genero;
}

string  ListaCircular::getDirecc(int id){
    Song *temp = ptrHead;
    for (int i=0;i<id;i++){
        temp=temp->next;
    }
    return temp->direcc;
}

void ListaCircular::sig(){
    mciSendString("close mp3", NULL, 0, NULL);
    selecc=selecc->next;
}
void ListaCircular::prev(){
    mciSendString("close mp3", NULL, 0, NULL);
    selecc=selecc->back;
}

string  ListaCircular::getSong(){
    return selecc->direcc;
}

int ListaCircular::findSelecc(){
    int aux=0;
    Song *temp = ptrHead;
    while(temp!=selecc){
        aux++;
        temp=temp->next;
    }
    return aux;
}
