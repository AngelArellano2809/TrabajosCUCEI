#include<iostream>
#include<stdlib.h>
#include<windows.h>
 using namespace std;

class Nodo{
  public:
    int value;
    Nodo* next;
};

int vacia(Nodo *&pila){
	if(pila==NULL){
		cout<<"LA PILA ESTA VACIA"<<endl;
        system("pause");
		return 0;
    }
    else
        return 1;
}

void push(Nodo *&pila, int n){
  Nodo *temp = new Nodo();
  temp->value = n;
  temp->next = pila;
  pila = temp;
};

void pop(Nodo *&pila){
    if(vacia(pila)==1){
      Nodo *temp = pila;
      pila = temp->next;
      delete(temp);
    }
};

void display(Nodo *&pila, int cont){
  Nodo *temp = pila;
  while(temp!=NULL){
    if(temp==pila){
        printf("\n\n\t\t%c%c%c%c%c\n",201,205,205,205,187);
        printf("\ttope->\t%c ",186);
      cout <<temp->value;
      if(temp->next!=nullptr){
        printf(" %c\n\t\t%c%c%c%c%c\n",186,204,205,205,205,185);
      }
      else{
        printf(" %c\n\t\t%c%c%c%c%c\n",186,200,205,205,205,188);;
      }
      temp=temp->next;
    }
    else if(temp->next==nullptr){
        printf("\t\t%c ",186);
      cout <<temp->value;
      printf(" %c\n\t\t%c%c%c%c%c\n",186,200,205,205,205,188);
      temp = temp->next;
    }
    else{
        printf("\t\t%c ",186);
        cout <<temp->value;
       printf(" %c\n\t\t%c%c%c%c%c\n",186,204,205,205,205,185);
        temp=temp->next;
    }
  }
  cout<<endl;
};

mostrarTope(Nodo *&pila){
    Nodo *temp = pila;
    system("cls");
    cout<<"El tope es:  "<<temp->value<<endl;
    system("pause>>cls");
    system("cls");
}

int menu(){
  int opc1;
  char opc[1],*aux;
  cout <<"1.- Apilar"<<endl;
  cout <<"2.- Eliminar"<<endl;
  cout <<"3.- Mostrar Tope"<<endl;
  cout <<"0.- Salir"<<endl;
  cin>>opc;
  if(isdigit(opc[0])){
    aux=&opc[0];
    opc1=atoi(aux);
    }
    else{
        return 7;
    }
  return opc1;
};

int main(){
    int x=0;
    char y[1],*z;
  Nodo *pila = NULL;
  int value, cont=0, opc=1;
  do {
    switch (menu()) {
      case 1:
      cont++;
      cout<<"ingresa numero"<<endl;
      cin>>y;
      if(isdigit(y[0])){
        z=&y[0];
        x=atoi(z);
      }
      else{
        cout<<"el dato no es un numero"<<endl;
        system("pause>>cls");
        system("CLS");
        break;
            }
      push(pila, x);
      system("CLS");
      display(pila, cont);
      break;
      case 2:
      cont--;
      pop(pila);
      system("CLS");
      display(pila, cont);
      break;
      case 3:
          mostrarTope(pila);
        break;
      case 0:
      opc=0;
      break;
      default: std::cout << "\nOpcion no disponible" << '\n';system("CLS");
    }
  } while(opc!=0);
};
