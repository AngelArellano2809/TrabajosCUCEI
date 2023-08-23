#ifndef LISTA_H_INCLUDED
#define LISTA_H_INCLUDED
#include <iostream>
#include <stdlib.h>
using namespace std;

template <class T>
class List;

template <class T>
class Node{
private:
    friend class List<T>;
    T elem;
    Node<T> *next;
    Node<T> *prev;

public:
    Node(T v, Node<T> *pnext = NULL, Node<T> *pprev = NULL) : elem(v), next(pnext), prev(pprev) {}

    T& getElem();
    void setPrev(Node<T>*);
    void setNext(Node<T>*);
    Node<T>* getNext();
    Node<T>* getPrev();
    /*Node();
    Node(T);
    void setElem(T);
    */
};

template <class T>
T& Node<T>::getElem(){
    return elem;
}

template <class T>
void Node<T>::setPrev(Node<T>* a){
    this->prev = a;
}

template <class T>
Node<T>* Node<T>::getNext(){
    return this->next;
}

template <class T>
Node<T>* Node<T>::getPrev(){
    return this->prev;
}

template <class T>
void Node<T>::setNext(Node<T>* a){
    this->next = a;
}

template <class T>
class List {
    private:
        Node<T> *ptrList; // puntero de la lista
    public:
        List(): ptrList(NULL) {}
        //~List();

        bool Empty(){ return ptrList == NULL; }

        void Add(T);
        void remove();
        void print();
        void buscar(string);
        void modif(T);

        void getNext();
        void getPrev();
        void getFirst();
        void getLast();
        Node<T>& getList();

        void arregloApunt();
        void IMerge(Node<T>** arr, Node<T>** arrTemp, int izq, int der);
        void mergeSort(Node<T>** arr, Node<T>** arrTemp, int izq, int der, int posFinal);
};

template<class T>
void List<T>::arregloApunt()
{
    Node<T>** arr;
    Node<T>** arrTemp;
    Node<T>* p;
    int counter = 0;
    int x;
    getFirst();
    p = ptrList;
    while (p != NULL)
    {
        counter ++;
        p = p->getNext();
    }
    if (counter < 2)
        return;
    arr = new Node<T> *[counter];
    arrTemp = new Node<T>* [counter];
    p = ptrList;
    counter = 0;
    while (p != NULL)
    {
        arr[counter++] = p;
        p = p->getNext();
    }
    IMerge(arr, arrTemp, 0, counter-1);

    getFirst();
    ptrList = arr[0];
    arr[0]->setPrev(NULL);
    for (x = 0; x < counter-1; x++)
    {
        arr[x]->setNext(arr[x+1]);
        arr[x+1]->setPrev(arr[x]);
    }
    arr[counter-1]->setNext(NULL);
    delete arr;
    delete arrTemp;
}

template<class T>
void List<T>::IMerge(Node<T>** arr, Node<T>** arrTemp, int izq, int der)
{
    int medio;
    if (izq < der)
    {
        medio = ((izq + der)/2);
        IMerge(arr, arrTemp, izq, medio);
        IMerge(arr, arrTemp, medio+1, der);
        mergeSort(arr, arrTemp, izq, medio+1, der);
    }
}

template<class T>
void List<T>::mergeSort(Node<T>** arr, Node<T>** arrTemp, int izq, int der, int posFinal)
{
    int fIzq = der;
    int pAux = izq;
    int numeroEleme = posFinal - izq+1;
    while (izq <= fIzq && der <= posFinal){
        if(arr[izq]->elem.getAsientosDisp() < arr[der]->elem.getAsientosDisp()){
            arrTemp[pAux] = arr[izq];
            pAux++;
            izq++;
        }
        else{
            arrTemp[pAux] = arr[der];
            pAux++;
            der++;
        }
    }

    while (izq <= fIzq){
        arrTemp[pAux] = arr[izq];
        pAux++;
        izq++;
    }
    while (der <= posFinal){
        arrTemp[pAux] = arr[der];
        pAux++;
        der++;
    }

    for (int i = 0; i <= numeroEleme; i++, posFinal--){
        arr[posFinal] = arrTemp[posFinal];
    }
}

template <class T>
Node<T>& List <T>::getList()
{
    return *ptrList;
}

template <class T>
void List <T>::Add(T e) // Agregar al Nodo
{
    Node<T> *ptrNew;
    getFirst(); // Metodo que permite insertar al inicio de la lista
    if(Empty()) {
        ptrNew = new Node<T>(e);
        if(!ptrList) ptrList = ptrNew;
        else ptrList->prev = ptrNew;
    }
    else {
        while(ptrList->next){
            getNext();
        }
        ptrNew = new Node<T>(e, ptrList->next, ptrList);
        ptrList->next = ptrNew;
        if(ptrNew->next) ptrNew->prev->prev = ptrNew;
    }
}

template <class T>
void List <T>::modif(T e)
{
    Node<T> *ptrNew;
    ptrNew = new Node<T>(e);
    ptrList->elem=ptrNew->elem;
}

template<class T>
void List<T>::remove(){

    if(ptrList->next&&ptrList->prev){
        ptrList->prev->next=ptrList->next;
        ptrList->next->prev=ptrList->prev;
    }
    if(ptrList->next&&!(ptrList->prev)){
        ptrList->next->prev=nullptr;
        ptrList=ptrList->next;
    }
    if(ptrList->prev&&!(ptrList->next)){
        ptrList->prev->next=nullptr;
        ptrList=ptrList->prev;
    }
}

template<class T>
void List<T>::getNext(){
    if(ptrList) {
        ptrList = ptrList->next;
    }
}

template<class T>
void List<T>::getPrev(){
    if(ptrList) {
        ptrList = ptrList->prev;
    }
}

template<class T>
void List<T>::getFirst(){
    while(ptrList && ptrList->prev) {
        //cout<<ptrList<<" | "<<ptrList->ptrPrev<<endl;
        ptrList = ptrList->prev;
    }
}

template<class T>
void List<T>::getLast(){
    while(ptrList && ptrList->next) {
        ptrList = ptrList->next;
    }
}

template<class TIPO>
void List<TIPO>::print(){
    Node<TIPO> *ptrNode;
    getFirst();
    ptrNode = ptrList;
    while(ptrNode) {
        ptrNode->elem.show();
        ptrNode=ptrNode->next;
    }
}

template<class TIPO>
void List<TIPO>::buscar(string nom){
    getFirst();
    while(!(ptrList->elem.getNombre()==nom)){
        ptrList=ptrList->next;
    }
}

#endif // LISTA_H_INCLUDED
