#include<iostream>
#include<stdlib.h>
using namespace std;

class cola{
	private:
		int inicio,fin;
        int dato[10];
	public:
       cola();
       int lleno();
       int vacio();
       void llenar( );
       void consultar_inicio();
       void consultar_final();
       void mostrar_cola();
       void eliminar();
};

cola::cola(){
	fin=-1;//final
	inicio=0;//frente
}

 void cola::llenar(){
 	int x;
 	char y[1],*z;
    fin ++;
	 if(lleno()==0){
	 	cout<<"Ingrese dato "<<endl;
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
 		dato[fin]=x;
	 }
 }

void cola::consultar_inicio(){
	if(vacio()==0){

		cout<<"\nEL inicio es  "<<dato[0]<<endl;
		system("pause");
	}
}

void cola::consultar_final(){
	if(vacio()==0){
		cout<<"\nEl final es  "<<dato[fin]<<endl;
		system("pause");
	}
}

void cola::mostrar_cola(){
	if(vacio()==0){
	system("cls");
	printf("\n\n\t\t%c%c%c%c%c  \n",201,205,205,205,187);
	    for(int i=fin;i>=0;i--){
            if(i==inicio)
                printf("Frente->\t%c ",186,205);
            else if(i==fin)
                printf("Final->\t\t%c ",186,205);
            else
                printf("\t\t%c ",186,205);
		    cout<<dato[i]; printf(" %c\n",186);
		    if(i==0)
                printf("\t\t%c%c%c%c%c\n",200,205,205,205,188);
		    else
                printf("\t\t%c%c%c%c%c\n",204,205,205,205,185);
		}
        /*for(int i=fin;i>=0;i--){
           if(dato[i]!=-1){
            cout<<"  "<<dato[i];
            }
        }*/
	}
}

void cola::eliminar(){
	if(vacio()==0){
		for(int i=0;i<=fin;i++){
			dato[i]=dato[i+1];
		}
		dato[fin]=-1;
		fin--;
	}
}

int cola::lleno(){
	if(fin==9){
		cout<<"LA COLA ESTA LLENA"<<endl;
		system("pause");
		return 1;
	}else{
		return 0;
	}
}
int cola::vacio(){
	if(fin==-1){
		cout<<"LA COLA ESTA VACIA"<<endl;
		system("pause");
		return 1;
	} else{
		return 0;
	}
}

int main(){
   int dato;
    int opcion;
    char opc[1],*aux;
   	cola c;
do{
	system("cls");
    c.mostrar_cola();
    cout<<""<<endl;
    cout<<"Menu"<<endl;
   	cout<<"[1]Encolar(push)"<<endl;
	cout<<"[2]Mostrar inicio"<<endl;
	cout<<"[3]Mostrar fin"<<endl;
	cout<<"[4]Des-Encolar(pop)"<<endl;
	cout<<"[5]Mostrar cola"<<endl;
	cout<<"[6].Salir"<<endl;
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
   		        c.llenar();
   		        break;
   		case 2: c.consultar_inicio();
		        break;
		case 3: c.consultar_final();
		        break;
   		case 4: c.eliminar();
		          break;
		case 5: c.mostrar_cola();
		         break;
	   }
       }while(opcion!=6);
   }
