#include<iostream>
#include<stdlib.h>
#include<windows.h>
 using namespace std;



 class pila{
	private: int datos[10],tope;
	public:
		pila();
		void push();
		void pop();
		int  vacia();
		int llena();
		void mostrar_tope();
		void mostrar_pila();
		void gotoxy(int,int);


};

pila::pila(){
	 tope=-1;
}

void pila::push(){
	int x=0;
	char y[1],*z;
	if(llena()==0){
		cout<<"ingresa numero"<<endl;
		cin>>y;
		if(isdigit(y[0])){
                z=&y[0];
                x=atoi(z);
            }
            else{
                cout<<"el dato no es un numero"<<endl;
                system("pause>>cls");
                return;
            }
		tope ++;
	     datos[tope]=x;
	}
}

void pila::pop(){
	if(vacia()==0){
		datos[tope ]= 0;
		tope --;
	}
}

void pila::mostrar_tope(){
	if(vacia()==0){
		system("cls");
		cout<<"El tope es:  "<<datos[tope ]<<endl;
		system("pause");
	}
}

void pila::mostrar_pila(){
	int ayuda,i;
	if(vacia()==0){
		system("cls");
	   	printf("\n\n\t\t%c%c%c%c%c  \n",201,205,205,205,187);
	    for(i=tope;i>=0;i--){
            if(i==tope)
                printf("\ttope->\t%c ",186,205);
            else
                printf("\t\t%c ",186,205);
		    cout<<datos[i]; printf(" %c\n",186);
		    if(i==0)
                printf("\t\t%c%c%c%c%c\n",200,205,205,205,188);
		    else
                printf("\t\t%c%c%c%c%c\n",204,205,205,205,185);
		}
	}
  }

int  pila::vacia(){
	if(tope==-1){
		system("cls");
		cout<<"LA PILA ESTA VACIA"<<endl;
		system("pause");
		return 1;
	} else{
		return 0;
	}
}
int  pila::llena(){
	if(tope==9){
		system("cls");
		cout<<"LA PILA ESTA LLENA "<<endl;
		system("pause");
	     return 1;
	}
	else{
			return 0;
	}
}

void pila:: gotoxy(int x,int y){
      HANDLE hcon;
      hcon = GetStdHandle(STD_OUTPUT_HANDLE);
      COORD dwPos;
      dwPos.X = x;
      dwPos.Y= y;
      SetConsoleCursorPosition(hcon,dwPos);
 }

 int main(){
	pila p;
	char opc[1],*aux;
	int opcion,num;
		do{
            system("cls");
            p.mostrar_pila();
			cout<<"\n\n[1].ingresar numero\n[2].Eliminar tope\n[3].Mostrar tope\n[4].Mostrar pila\n[5].salir"<<endl;
            cin>>opc;
            if(isdigit(opc[0])){
                aux=&opc[0];
                opcion=atoi(aux);
            }
            else{
                cout<<"el dato no es un numero"<<endl;
                system("pause>>cls");
                continue;
            }
			switch(opcion){
				case 1:
                    p.push();
                    break;
				case 2:
                    p.pop();
                    break;
				case 3:
				    p.mostrar_tope();
                    break;
				case 4:
				    p.mostrar_pila();
                    break;
				default: cout<<"Opcion incorrecta "<<endl;
                system("pause");
                break;
            }
		}while(opcion!=5);
}
