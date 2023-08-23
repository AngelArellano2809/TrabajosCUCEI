#include <iostream>
using namespace std;

int val (char y){
    int x=0;
    if(y>='0'&&y<='9'){
        x=atoi(&y);
        return x;
    }
    else{
        return -1;
    }
}

class CircularList{
    private:
    class Node {
        public:
            int number;
            Node *next;
            Node *back;
    };

    Node *ptrHead;
    public:
        CircularList();
        ~CircularList();
        void insert_First(int);
        void insert_Last(int);
        bool empty();
        void print();
        int travel();
        void remove(int );
        void search (int pos);
        void edit (int pos,int num);
};

CircularList::CircularList(){
    ptrHead = NULL;
}

CircularList::~CircularList() {
    if (ptrHead != NULL) {
        Node *temp = ptrHead->next;
        Node *temp_ptrHead;
        while (temp != ptrHead){
            temp_ptrHead = temp;
            temp = temp->next;
            delete temp_ptrHead;
        }
        delete ptrHead;
    }
}

void CircularList::insert_First(int number) {
    Node *new_node = new Node();
    new_node->number = number;
    if (ptrHead == NULL){
        new_node->next = new_node;
        new_node->back = new_node;
        ptrHead = new_node;
    }
    else{
        Node *last_node = ptrHead->back;
        new_node->next = ptrHead;
        new_node->back = last_node;
        ptrHead->back = new_node;
        last_node->next = new_node;
        ptrHead = new_node;
    }
}

void CircularList::insert_Last(int number) {
    Node *new_node = new Node();
    new_node->number = number;
    if (ptrHead == NULL){
        new_node->next = new_node;
        new_node->back = new_node;
        ptrHead = new_node;
    }
    else{
        Node *last_node = ptrHead->back;
        new_node->next = ptrHead;
        new_node->back = last_node;
        ptrHead->back = new_node;
        last_node->next = new_node;
    }
}

bool CircularList::empty() {
if (ptrHead == NULL)
    return true;
else
    return false;
}

void CircularList::print() {
if (!empty()) {
    Node *temp = ptrHead;
    do {
        cout<<temp->number <<"-";
        temp = temp->next;
    } while (temp != ptrHead);
    cout << "\n";
    }
}

int CircularList::travel() {
    int count = 0;
    if (!empty()){
        Node *temp = ptrHead;
        do {
            count++;
            temp = temp->next;
        } while (temp != ptrHead);
    }
    return count;
}

void CircularList::remove(int position){
    if (position <= travel()){
        if (position == 1){
            if (travel() == 1){
                delete ptrHead;
                ptrHead = NULL;
            }
            else{
                Node *temp_ptrHead = ptrHead;
                Node *last_node = ptrHead->back;
                ptrHead = ptrHead->next;
                last_node->next = ptrHead;
                ptrHead->back = last_node;
                delete temp_ptrHead;
            }
        }
        else {
            Node *temp = ptrHead;
            for (int f = 1; f <= position- 1; f++)
            temp = temp->next;

            Node *temp_ptrHead = temp;
            Node *back = temp->back;
            temp = temp->next;
            back->next = temp;
            temp->back = back;
            delete temp_ptrHead;
        }
    }
}

void CircularList::search (int pos){
    if (!empty()){
        Node *temp = ptrHead;
        for(int i=0;i<pos-1;i++){
            temp = temp->next;
        }
        cout<<"el valor en la posicion "<<pos<<" es: "<<temp->number<<endl;
    }
}

void CircularList::edit (int pos,int num){
    int aux=1;
    if (!empty()){
        Node *temp = ptrHead;
        do {
            temp = temp->next;
            aux++;
        } while (aux!=pos);
        temp->number=num;
    }
}


int main(int argc, char** argv) {
    CircularList *obj = new CircularList();
    char opc,numero,posicion;
    int num,pos;
    do{
        cout<<"1.-Insert first\n";
        cout<<"2.-Inser Last\n";
        cout<<"3.-Search Position\n";
        cout<<"4.-Edit\n";
        cout<<"5.-Delete\n";
        cout<<"6.-Listar/Print\n";
        cout<<"7.-Salir..\n";
        cout<<"Seleccione un opcion\n";
        do{
            cin.sync();
            cin>>opc;
            if(opc<46 || opc>'9'){
                cout<<"Ingresa puros numeros"<<endl;
            }
        }while(opc<46|| opc>'9');
        switch (opc){
            case '1':{
                cout<<"ingresa un numero:"<<endl;
                cin>>numero;
                if(val(numero)!=-1)
                    num=val(numero);
                else{
                    cout<<"no es un numero"<<endl;
                    break;}
                obj->insert_First(num);
                obj->print();
                break;
            }
            case '2':{
                cout<<"ingresa un numero:"<<endl;
                cin>>numero;
                if(val(numero)!=-1)
                    num=val(numero);
                else{
                    cout<<"no es un numero"<<endl;
                    break;}
                obj->insert_Last(num);
                obj->print();
                break;
            }
            case '3':{
                cout<<"ingresa una posicion:"<<endl;
                cin>>numero;
                if(val(numero)!=-1)
                    num=val(numero);
                else{
                    cout<<"no es un numero"<<endl;
                    break;}
                obj->search (num);
                obj->print();
                break;
            }
            case '4':{
                cout<<"ingresa una posicion a editar:"<<endl;
                cin>>posicion;
                if(val(posicion)!=-1)
                    pos=val(posicion);
                else{
                    cout<<"no es un numero"<<endl;
                    break;}
                cout<<"ingresa el nuevo numero:"<<endl;
                cin>>numero;
                if(val(numero)!=-1)
                    num=val(numero);
                else{
                    cout<<"no es un numero"<<endl;
                    break;}
                obj->edit(pos,num);
                obj->print();
                break;
            }
            case '5':{
                cout<<"ingresa una posicion a eliminar:"<<endl;
                cin>>numero;
                if(val(numero)!=-1)
                    num=val(numero);
                else{
                    cout<<"no es un numero"<<endl;
                    break;}
                obj->remove(num);
                obj->print();
                break;
            }
            case '6':{
                obj->print();
                break;
            }
            case '7':{
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
