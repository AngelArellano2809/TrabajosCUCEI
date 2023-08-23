 //ARELLANO GRANADOS ANGEL MARIANO 218123444
 #include <iostream>
 #include <cstring>
using namespace std;
struct agenda{
	int id;
	char nombre[30];
	char direccion[30];
	char email[30];
	char telefono[10];
}a[5];
int index=0;
void RegistrarContacto(){
     	a[index].id=index+1;
		cout<<"ingrese nombre: "<<endl;
		cin>>a[index].nombre;
		cout<<"ingrese direccion: "<<endl;
		cin>>a[index].direccion;
		cout<<"ingrese email: "<<endl;
		cin>>a[index].email;
		cout<<"ingrese telefono: "<<endl;
		cin>>a[index].telefono;
        index++;
}

int BuscarContacto(int id){
	int posicion=-1,x=0;
	bool ban=false;
	while(x<5 && ban==false){
		if(id==a[x].id){
		  ban=true;
		  posicion=x;
		}
		x++;
	}
	return posicion;
}
void MostrarContacto(int pos){
		cout<<"nombre: "<<a[pos].nombre<<endl;
		cout<<"direccion: "<<a[pos].direccion<<endl;
		cout<<"email: "<<a[pos].email<<endl;
		cout<<"telefono: "<<a[pos].telefono<<endl;
}

void ModificarContacto(int pos){
        cout<<"ingrese el nuevo nombre: "<<endl;
		cin>>a[pos].nombre;
		cout<<"ingrese la nuevo direccion: "<<endl;
		cin>>a[pos].direccion;
		cout<<"ingrese el nuevo email: "<<endl;
		cin>>a[pos].email;
		cout<<"ingrese el nuevo telefono: "<<endl;
		cin>>a[pos].telefono;
}

void EliminarContacto(int pos){
        for(int i=pos;i<5;i++){
            strcpy(a[i].nombre,a[i+1].nombre);
            strcpy(a[i].direccion,a[i+1].direccion);
            strcpy(a[i].email,a[i+1].email);
            strcpy(a[i].telefono,a[i+1].telefono);
        }
}

void menu(){
	int opcMenu=0,id=0;
	cout<<"1) Registro Contacto"<<endl;
	cout<<"2) Buscar Contacto"<<endl;
    cout<<"3) Editar Contacto"<<endl;
	cout<<"4) Remover Contacto"<<endl;
	cout<<"5) Salir"<<endl;
	cout<<"Seleccione una opcion"<<endl;
	cin>>opcMenu;
	switch(opcMenu){
		case 1: RegistrarContacto();break;
		case 2:{
				cout<<"Ingrese Id a Buscar"<<endl;
	            cin>>id;
			    MostrarContacto(BuscarContacto(id));
		}break;
		case 3:{
                cout<<"Ingrese Id a Modificar"<<endl;
	            cin>>id;
	            ModificarContacto(BuscarContacto(id));
		} break;
		case 4: {
                cout<<"Ingrese Id a Eliminar"<<endl;
	            cin>>id;
	            EliminarContacto(BuscarContacto(id));
		} break;
		case 5: {
                exit(EXIT_SUCCESS);
		} break;
	}

}
int opc=0;
int main() {
	do{
		system("cls");
		menu();
		cout<<"Continuar 1 si 2 no"<<endl;
		cin>>opc;
	}while(opc!=2);
	return 0;
}
