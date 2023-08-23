#include <iostream>
using namespace std;
template<class TIPO> class List;

template<class TIPO>
class Node {
    public:
        Node(TIPO v, Node<TIPO> *pnext = NULL, Node<TIPO> *pprev = NULL) :
        value(v), ptrNext(pnext), ptrPrev(pprev) {}
    private:
        TIPO value;
        Node<TIPO> *ptrNext;
        Node<TIPO> *ptrPrev;
        friend class List<TIPO>; // funcion amiga que permite sobrecargar la lista
};

template<class TIPO>
class List { // objeto lista
    public:
        List() : ptrList(NULL) {}
        ~List();
        void Add(TIPO v);
        void remove(TIPO v);
        bool Empty() { return ptrList == NULL; }
        void print();
        void ptrNext();
        void ptrPrev();
        void First();
        void Last();
        bool Current() { return ptrList != NULL; }
        TIPO CurrentValue() { return ptrList->value; }
    private:
        Node<TIPO> *ptrList; // puntero de la lista
};

template<class TIPO>
List<TIPO>::~List() // Destructor de la clase
{
    Node<TIPO> *aux;
    First();
    while(ptrList) {
        aux = ptrList;
        ptrList = ptrList->ptrNext;
        delete aux;
    }
}

template<class TIPO>
void List<TIPO>::Add(TIPO v) // Agregar al Nodo
{
    Node<TIPO> *ptrNew;
    First(); // Metodo que permite insertar al inicio de la lista
    if(Empty() || ptrList->value > v) {
        ptrNew = new Node<TIPO>(v, ptrList);
        if(!ptrList) ptrList = ptrNew;
        else ptrList->ptrPrev = ptrNew;
    }
    else {
    // se mueve hasta el último nodo que tenva un valor mayor
        while(ptrList->ptrNext && ptrList->ptrNext->value <= v) ptrNext();

        ptrNew = new Node<TIPO>(v, ptrList->ptrNext, ptrList);
        ptrList->ptrNext = ptrNew;
        if(ptrNew->ptrNext) ptrNew->ptrPrev->ptrPrev = ptrNew;
    }
}

template<class TIPO>
void List<TIPO>::remove(TIPO v){
    Node<TIPO> *ptrNode;

    ptrNode = ptrList;
    while(ptrNode && ptrNode->value < v) ptrNode = ptrNode->ptrNext;
    while(ptrNode && ptrNode->value > v) ptrNode = ptrNode->ptrPrev;

    if(!ptrNode || ptrNode->value != v) return;

    if(ptrNode->ptrPrev) // no es el primer elemento
        ptrNode->ptrPrev->ptrNext = ptrNode->ptrPrev;
    if(ptrNode->ptrNext) // no el último Node
        ptrNode->ptrNext->ptrPrev = ptrNode->ptrNext;
}

template<class TIPO>
void List<TIPO>::print(){
    Node<TIPO> *ptrNode;
    First();
    //cout<<ptrList;
    ptrNode = ptrList;
    while(ptrNode) {
        cout << ptrNode->value << "-> ";
    }
    cout << endl;
}

template<class TIPO>
void List<TIPO>::ptrNext(){
    if(ptrList) {
        ptrList = ptrList->ptrNext;
    }
}

template<class TIPO>
void List<TIPO>::ptrPrev(){
    if(ptrList) {
        ptrList = ptrList->ptrPrev;
    }
}

template<class TIPO>
void List<TIPO>::First(){
    while(ptrList && ptrList->ptrPrev) {
        cout<<ptrList<<" | "<<ptrList->ptrPrev<<endl;
        ptrList = ptrList->ptrPrev;
    }
}

template<class TIPO>
void List<TIPO>::Last(){
    while(ptrList && ptrList->ptrNext) {
        ptrList = ptrList->ptrNext;
    }
}

int main(){
    List<int> list;
    char opc;
    do{
        cout<<"1-.Agregar Numero\n";
        cout<<"2-.Buscar Numero.\n";
        cout<<"3-.Ordenar de forma ascendente\n";
        cout<<"4-.Ordenar de forma descendente\n";
        cout<<"5-.Remover el último nodo\n";
        cout<<"0-.Salir..\n";
        cout<<"Seleccione un opcion\n";
        do{
            cin.sync();
            cin>>opc;
            if(opc<46 || opc>'9'){
                cout<<"Ingresa puros numeros"<<endl;
            }
        }while(opc<46|| opc>'9');
        switch(opc){
            case '1':{
                int num;
                cout<<"Ingresa un numero:"<<endl;
                cin>>num;
                list.Add(num);
                list.print();
                break;
            }
            case '2':{

                break;
            }
            case '3':{
                list.First();
                list.print();
                break;
            }
            case '4':{
                list.Last();
                list.print();
                break;
            }
            case '5':{
                list.remove(40);
                break;
            }
            case '0':{
                return 0;
                break;
            }
        }
        cout<<endl;
        system("pause");
        system("cls");
    }while(opc!=0);
    return 0;
}
