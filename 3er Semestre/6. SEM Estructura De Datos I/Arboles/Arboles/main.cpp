#include <iostream>
#include <stdlib.h>
#include <cstring>

using namespace std;

bool checkDigit(char buffer[100]){
    int sizeC;
    sizeC = strlen(buffer);
    for(int i=0; i<sizeC;i++){
        if(buffer[i]<48 || buffer[i]>57){
            cout<<"Ingrese Solo Numeros"<<endl;
            return false;
        }
    }
    return true;
}
bool checkName(char buffer[100]){
    int sizeC;
    bool valid = true;
    sizeC = strlen(buffer);
    for(int i=0; i<sizeC;i++){
        if (((buffer[i]) > 31 && (buffer[i]) < 47) == 0){
            if (((buffer[i]) > 64 && (buffer[i]) < 91) == 0){
                if (((buffer[i]) > 96 && (buffer[i]) < 123) == 0){//Mayusculas, Minusculas y espacio
                cout<<"Ingrese Solo Caracteres"<<endl;
                valid = false;
                }
            }
        }
    }
    return valid;

}

struct Object{
    int id;
    string nombre;
    string direccion;
    string email;
    struct Object *left, *right,*dad ;
};
typedef struct Object *Node;

Node CreateNode(int id,string nom, string dir,string ema,Node dad) {
    Node newNode = new(Object);
    newNode->id = id;
    newNode->nombre = nom;
    newNode->direccion = dir;
    newNode->email = ema;
    newNode->left = NULL;
    newNode->right = NULL;
    newNode->dad = dad;
    return newNode;
}

void add(Node &ptr, int id,string nom, string dir,string ema,Node dad) {
    if(ptr==NULL) {
        Node newNode = CreateNode(id,nom,dir,ema,dad);
        ptr = newNode;
    }
    else if(id < ptr->id){
        add(ptr->left, id,nom,dir,ema,ptr);
    }
    else{
        add(ptr->right, id,nom,dir,ema,ptr);
    }
}

void show(Node ptr, int n){
    if(ptr==NULL){
        return;
    }
    else{
        show(ptr->right, n+1);
        for(int i=0; i<n; i++)
            cout<<"   ";
        cout<< ptr->id <<endl;
        show(ptr->left, n+1);
    }
}

bool buscaId(Node ptr, int id){
    if (ptr==NULL){
        return false;
    }
    else if (ptr->id==id){
        cout<<"ID: "<<ptr->id<<endl;
        cout<<"Nombre: "<<ptr->nombre<<endl;
        cout<<"Direccion: "<<ptr->direccion<<endl;
        cout<<"Email: "<<ptr->email<<endl;
        return true;
    }
    else if(id < ptr->id){
        return buscaId(ptr->left,id);
    }
    else if(id > ptr->id){
        return buscaId(ptr->right,id);
    }
    else
        return false;
}

bool buscaNom(Node ptr,string nom){
    if (ptr==NULL){
        return false;
    }
    else if (ptr->nombre==nom){
        cout<<"ID: "<<ptr->id<<endl;
        cout<<"Nombre: "<<ptr->nombre<<endl;
        cout<<"Direccion: "<<ptr->direccion<<endl;
        cout<<"Email: "<<ptr->email<<endl;
        return true;
    }
    else if(nom < ptr->nombre){
        return buscaNom(ptr->left,nom);
    }
    else if(nom > ptr->nombre){
        return buscaNom(ptr->right,nom);
    }
    else
        return false;
}

void minimo(Node ptr){
    if (ptr==NULL){
        return;
    }
    else{
        while(ptr->left!=NULL){
            ptr=ptr->left;
        }
        cout<<"ID MENOR: "<<endl;
        cout<<"ID: "<<ptr->id<<endl;
        cout<<"Nombre: "<<ptr->nombre<<endl;
        cout<<"Direccion: "<<ptr->direccion<<endl;
        cout<<"Email: "<<ptr->email<<endl;
    }

}

void maximo(Node ptr){
    if (ptr==NULL){
        return;
    }
    else{
        while(ptr->right!=NULL){
            ptr=ptr->right;
        }
        cout<<"ID MAYOR: "<<endl;
        cout<<"ID: "<<ptr->id<<endl;
        cout<<"Nombre: "<<ptr->nombre<<endl;
        cout<<"Direccion: "<<ptr->direccion<<endl;
        cout<<"Email: "<<ptr->email<<endl;
    }
}

bool edit(Node ptr, int id){
    int opc;
    string nuevo;
    if (ptr==NULL){
        return false;
    }
    else if (ptr->id==id){
        cout<<"Que se edtitara? 1)Nombre | 2)Direccion | 3)Email"<<endl;
        cin>>opc;
        cin.ignore();
        cout<<"Introduca en nuevo dato: "<<endl;
        getline(cin,nuevo);
        switch(opc){
            case 1:{
                ptr->nombre=nuevo;
            }break;
            case 2:{
                ptr->direccion=nuevo;
            }break;
            case 3:{
                ptr->email=nuevo;
            }break;
        }
        return true;
    }
    else if(id < ptr->id){
        return edit(ptr->left,id);
    }
    else if(id > ptr->id){
        return edit(ptr->right,id);
    }
    else
        return false;
}

Node menor(Node ptr){
    if(ptr==NULL){
        return NULL;
    }
     else if(ptr->left){
        return menor(ptr->left);
     }
     else{
        return ptr;
     }
}

void remplazar(Node ptr, Node new_ptr){
    if(ptr->dad){
        if(ptr->id == ptr->dad->left->id){
    cout<<"TEST"<<endl;
            ptr->dad->left=new_ptr;
        }
        else if(ptr->id == ptr->dad->right->id){
            ptr->dad->right=new_ptr;
        }
    }
    if(new_ptr){
        new_ptr->dad=ptr->dad;
    }
}

void destruirNodo(Node ptr){
    ptr->left=NULL;
    ptr->right=NULL;
    delete ptr;
}

void eliminarNodo(Node ptr){
    if (ptr->left && ptr->right){
        Node mini=menor(ptr->right);
        ptr->id=mini->id;
        ptr->nombre=mini->nombre;
        ptr->direccion=mini->direccion;
        ptr->email=mini->email;
        eliminarNodo(mini);
    }
    else if(ptr->left){
        remplazar(ptr,ptr->left);
        destruirNodo(ptr);
    }
    else if(ptr->right){
        remplazar(ptr,ptr->right);
        destruirNodo(ptr);
    }
    else{
        remplazar(ptr,NULL);
        destruirNodo(ptr);
    }
}

bool eliminar(Node ptr, int id){
    if(ptr==NULL){
        return false;
    }
    else if (ptr->id==id){
        eliminarNodo(ptr);
        return true;
    }
    else if(id < ptr->id){
        return eliminar(ptr->left,id);
    }
    else if(id > ptr->id){
        return eliminar(ptr->right,id);
    }
    else
        return false;
}

void preOrden(Node ptr){
    if(ptr==NULL){
        return;
    }
    else{
        cout<<ptr->id<<" - ";
        preOrden(ptr->left);
        preOrden(ptr->right);
    }
}

void inOrden(Node ptr){
    if(ptr==NULL){
        return;
    }
    else{
        inOrden(ptr->left);
        cout<<ptr->id<<" - ";
        inOrden(ptr->right);
    }
}

void postOrden(Node ptr){
    if(ptr==NULL){
        return;
    }
    else{
        postOrden(ptr->left);
        postOrden(ptr->right);
        cout<<ptr->id<<" - ";
    }
}

bool antecesor(Node ptr, int id){
    if (ptr==NULL){
        return false;
    }
    else if (ptr->id==id){
        if(ptr->left){
            cout<<"EL Antecesor del Nodo con ID: "<<ptr->id<<" es: "<<ptr->left->id<<endl;
        }
        else if(ptr->right){
            cout<<"EL Antecesor del Nodo con ID: "<<ptr->id<<" es: "<<ptr->right->id<<endl;
        }
        else{
            cout<<"El Nodo no tiene hijos"<<endl;
        }
        return true;
    }
    else if(id < ptr->id){
        return antecesor(ptr->left,id);
    }
    else if(id > ptr->id){
        return antecesor(ptr->right,id);
    }
    else
        return false;
}

bool sucesor(Node ptr, int id){
    if (ptr==NULL){
        return false;
    }
    else if (ptr->id==id){
        if(ptr->dad){
            cout<<"EL Sucesor del Nodo con ID: "<<ptr->id<<" es: "<<ptr->dad->id<<endl;
        }
        else{
            cout<<"El Nodo no tiene Sucesor"<<endl;
        }
        return true;
    }
    else if(id < ptr->id){
        return sucesor(ptr->left,id);
    }
    else if(id > ptr->id){
        return sucesor(ptr->right,id);
    }
    else
        return false;
}

int main(){
    Node ptr = NULL;
    int opc,id;
    string nom,dir,ema;
    char buffer[100];
    do{
        bool valid = false;
        //Menu
        cout<<"1) Insertar Datos"<<endl;//
        cout<<"2) Buscar Nodo"<<endl;//
        cout<<"3) Mostrar Minimo ID (Nodo)"<<endl;//
        cout<<"4) Mostrar Maximo ID (Nodo)"<<endl;//
        cout<<"5) Mostrar Nodo Antecesor"<<endl;
        cout<<"6) Mostrar Nodo Sucesor"<<endl;
        cout<<"7) Editar Nodo (por ID)"<<endl;//
        cout<<"8) Eliminar Nodo(Por ID)"<<endl;//
        cout<<"9) Mostrar Datos en Orden"<<endl;//
        cout<<"10) Mostrar Datos en PreOrden"<<endl;//
        cout<<"11) Mostrar Datos en PostOrden"<<endl;///
        cout<<"0) Salir"<<endl;//
        //cin>>opc;cin.ignore();
        do{
            cin>>buffer;cin.ignore();
            if(checkDigit(buffer)==true){
                valid = true;
                opc = atoi(buffer);
            }
       }while(!valid);
        switch(opc){
            case 1:{
                //cout<<"Ingresa el ID del usuario:"<<endl;cin>>id;cin.ignore();
                valid = false;
                do{
                    cout<<"Ingresa el ID del usuario:"<<endl;
                    cin>>buffer;cin.ignore();
                    if(checkDigit(buffer)==true){
                        valid = true;
                        id = atoi(buffer);
                    }
               }while(!valid);
                //cout<<"Ingresa el Nombre del usuario:"<<endl;cin>>nom;
                valid = false;
                do{
                    cout<<"Ingresa el Nombre del usuario:"<<endl;
                    cin.getline(buffer, 100, '\n');
                    if(checkName(buffer)==true){
                        valid = true;
                        nom= buffer;
                    }
                }while(!valid);
                //cout<<"Ingresa la Direccion del usuario:"<<endl;cin>>dir;
                valid = false;
                do{
                    cout<<"Ingresa la Direccion del usuario:"<<endl;
                    cin.getline(buffer, 100, '\n');
                    if(checkName(buffer)==true){
                        valid = true;
                        dir= buffer;
                    }
                }while(!valid);
                //cout<<"Ingresa el Email del usuario:"<<endl;cin>>ema;
                valid = false;
                do{
                    cout<<"Ingresa el Email del usuario:"<<endl;
                    cin.getline(buffer, 100, '\n');
                    if(checkName(buffer)==true){
                        valid = true;
                        ema= buffer;
                    }
                }while(!valid);
                add(ptr,id,nom,dir,ema,NULL);
            }break;
            case 2:{
                cout<<"   1) Por ID"<<endl;
                cout<<"   2) Por Nombre"<<endl;
                cin>>opc;
                cin.ignore();
                switch(opc){
                    case 1:{
                        cout<<"ingresa el Id a buscar"<<endl;
                        cin>>id;
                        cin.ignore();
                        if(!buscaId(ptr,id)){
                            cout<<"No se encontraron coincidencias."<<endl;
                        }
                    }break;
                    case 2:{
                        cout<<"Ingresa el Nombre a buscar:"<<endl;
                        getline(cin,nom);
                        if(!buscaNom(ptr,nom)){
                            cout<<"No se encontraron coincidencias."<<endl;
                        }
                    }break;
                }
            }break;
            case 3:{
                minimo(ptr);
            }break;
            case 4:{
                maximo(ptr);
            }break;
            case 5:{
                cout<<"ingresa el Id a buscar"<<endl;
                cin>>id;
                cin.ignore();
                if(!antecesor(ptr,id)){
                    cout<<"No se encontraron coincidencias."<<endl;
                }
            }break;
            case 6:{
                cout<<"ingresa el Id a buscar"<<endl;
                cin>>id;
                cin.ignore();
                if(!sucesor(ptr,id)){
                    cout<<"No se encontraron coincidencias."<<endl;
                }
            }break;
            case 7:{
                cout<<"ingresa el Id a editar"<<endl;
                cin>>id;
                cin.ignore();
                if(!edit(ptr,id)){
                    cout<<"No se encontraron coincidencias."<<endl;
                }
            }break;
            case 8:{
                cout<<"ingresa el Id a eliminar"<<endl;
                cin>>id;
                cin.ignore();
                if(!eliminar(ptr,id)){
                    cout<<"No se encontraron coincidencias."<<endl;
                }else{
                    cout<<"se elimino el dato."<<endl;
                }
            }break;
            case 9:{
                inOrden(ptr);
                cout<<endl;
                show(ptr,0);
            }break;
            case 10:{
                preOrden(ptr);
                cout<<endl;
                show(ptr,0);
            }break;
            case 11:{
                postOrden(ptr);
                cout<<endl;
                show(ptr,0);
            }break;
        }
    }while(opc);
    return 0;
}
