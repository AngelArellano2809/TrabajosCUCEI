#include <iostream>
#include <cstdlib>
using namespace std;

class Nodo{
  public:
    int value;
    Nodo* next;
};

bool cola_vacia(Nodo *frente){
	return (frente == NULL)? true : false;
};

void push(Nodo *&frente,Nodo *&fin,int num){
	Nodo *nuevo_nodo = new Nodo();
	nuevo_nodo->value = num;
	nuevo_nodo->next = NULL;

	if(cola_vacia(frente)){
		frente = nuevo_nodo;
	}
	else{
		fin->next = nuevo_nodo;
	}
	fin = nuevo_nodo;
};

void pop(Nodo *&frente,Nodo *&fin){
	Nodo *aux = frente;
	if(frente == fin){
		frente = NULL;
		fin = NULL;
	}else{
		frente = frente->next;
	}
	delete aux;
};

void display(Nodo *&frente, int cont,Nodo *&fin){
  Nodo *temp = frente;
  while(temp!=NULL){
    if(temp==frente){
        printf("\n\n\t\t%c%c%c%c%c\n",201,205,205,205,187);
        printf("Frente->\t%c ",186);
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
        printf("Final->\t\t%c ",186);
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

int menu(){
  int opc1;
  char opc[1],*aux;
  cout <<endl;
  cout <<"Menu"<<endl;
  cout <<"[1]Push"<<endl;
  cout <<"[2]Pop"<<endl;
  cout <<"[0]Salir"<<endl;
  cin>>opc;
    if(isdigit(opc[0])){
        aux=&opc[0];
        opc1=atoi(aux);
    }
    else{
        return 3;
    }
  return opc1;
};

int main(){
  Nodo *frente = NULL;
  Nodo *fin = NULL;
  int value, opc=1, cont2=0;
  char y;
  do {
    int x=0;
    system("cls");
    display(frente, cont2,fin);
    opc=menu();
    switch (opc) {
      case 1:{
         cont2++;
         cout<<"ingresa numero"<<endl;
          cin>>y;
          if(isdigit(y)){
            x=atoi(&y);
          }
          else{
            cout<<"el dato no es un numero"<<endl;
            system("pause>>cls");
            system("CLS");
            continue;
        }
         push(frente, fin,x);
         system("cls");
        break;
      }
      case 2:{
          cont2--;
          pop(frente, fin);
          system("cls");
          break;
        }
      default: {
          cout << "Opcion no disponible" <<endl;
          system("pause>>cls");
          break;
    }
    }
  } while(opc);
  return 0;
};
