 //ARELLANO GRANADOS ANGEL MARIANO 218123444
 #include <iostream>
 #include <cstring>
 #include <string.h>
using namespace std;

struct Player{
    int id;
    char name[30];
    int score;
}p[100];

int cont=0;
void CrearJuagador(){
    int x=0;
    bool unic;
    if (cont<100){
        cout<<"ingrese el nombre del jugador: "<<endl;
        cin>>p[cont].name;
        p[cont].score=0;
         do{
            x=1+rand()%100;
            bool unic=true;
            for(int i=0;i<cont;i++){
                if (p[i].id==x){
                    unic=false;
                    break;
                }
            }
            unic=false;
        }while(unic=false);
        p[cont].id=x;
        cout<<"el jugador "<<p[cont].name<<" tiene el Id: "<<p[cont].id<<endl<<endl;
        cont++;
    }
    if (cont>=100)
        cout<<"La lista esta llena"<<endl;
}

int BuscarJugadorID(int id){
    int i,pos;
    bool aux=false;
    for(i=0;i<cont;i++){
        if (id==p[i].id){
            pos=i;
            aux=true;
        }
    }
    if (aux==true)
        return pos;
    if(aux==false){
        cout<<"ERROR"<<endl;
        return 101;
    }
}

void AccederJugador(int pos){
    int opc, sum, res,i;
    if(pos<100){
    do{
        cout<<"Jugador "<<pos+1<<" Nombre: "<<p[pos].name<<endl;
        cout<<"1) Sumar Puntos"<<endl;
        cout<<"2) Restar Puntos"<<endl;
        cout<<"3) Eliminar"<<endl;
        cout<<"4) Salir"<<endl;

        cout<<"Seleccione una opcion:"<<endl;
        cin>>opc;
        switch(opc){
            case 1:{
                cout<<"Puntaje actual: "<<p[pos].score<<endl;
                cout<<"Cuantos puntos desea sumar?"<<endl;
                cin>>sum;
                p[pos].score+=sum;
                }break;
            case 2:{
                cout<<"Puntaje actual: "<<p[pos].score<<endl;
                cout<<"Cuantos puntos desea restar?"<<endl;
                cin>>res;
                if(res<=p[pos].score)
                    p[pos].score-=res;
                else
                    cout<<"ERROR"<<endl;
                }break;
            case 3:{
                for(i=pos;i<cont;i++){
                    p[i]=p[i+1];
                }
                cont--;
                opc=4;
                }break;
            case 4:{
                break;
                }break;
            default:{
                cout<<"Esa opcion no existe!"<<endl;
                }break;
        }
    }while(opc!=4);
    }
}

int BuscarJugadorNombre(char name[30]){
    int i,pos,opc;
    bool aux=false;
    for(i=0;i<cont;i++){
        if ((strcmp (name,p[i].name)) == 0){
            cout<<"Jugador "<<i+1<<"\t"<<p[i].name<<endl;
            cout<<"ID: "<<p[i].id<<endl;
            cout<<"Puntos: "<<p[i].score<<endl;
            cout<<"--------------------------------------------------------"<<endl;
            cout<<"continuar buscarndo?\n 1) Acceder\n 2) Continuar"<<endl;
            cin>>opc;
            if(opc==1){
                pos=i;
                aux=true;
            }
        }
    }
    if(opc==2){
        cout<<"No hay mas coincidencias!"<<endl;
        return 101;
    }
    if (aux==true)
        return pos;
    if(aux==false){
        cout<<"ERROR"<<endl;
        return 101;
    }
}

void MejorPuntaje(){
    int i,aux=0;
    aux=p[0].score;
    for (i=1;i<cont;i++){
        if(p[i].score>aux)
            aux=p[i].score;
    }
    cout<<"El Jugador / Jugadores como mejor puntaje es: "<<endl;
    for(i=0;i<cont;i++){
        if(aux==p[i].score){
            cout<<"Jugador "<<i+1<<"\t"<<p[i].name<<endl;
            cout<<"ID: "<<p[i].id<<endl;
            cout<<"Puntos: "<<p[i].score<<endl;
            cout<<"--------------------------------------------------------"<<endl;
        }

    }
}

void MostrarJugadores(){
    for(int i=0;i<cont;i++){
        cout<<"Jugador "<<i+1<<"\tNombre: "<<p[i].name<<endl;
        cout<<"ID: "<<p[i].id<<endl;
        cout<<"Puntos: "<<p[i].score<<endl;
        cout<<"--------------------------------------------------------"<<endl;
    }
}

int main(){
    char name[30];
    int opc=0,opc2=0,id;
    do{
        //menu
        cout<<"1) Crear jugador"<<endl;
        cout<<"2) Acceder a un jugador"<<endl;
        cout<<"3) Jugador con mayor puntaje"<<endl;
        cout<<"4) Mostrar todos los jugadores"<<endl;
        cout<<"5) Salir"<<endl;

        cout<<"Seleccione una opcion:"<<endl;
        cin>>opc;
        switch(opc){
            case 1:{
                CrearJuagador();
                }break;
            case 2:{
                cout<<"1) Buscar por ID"<<endl;
                cout<<"2) Buscar por Nombre"<<endl;
                cin>>opc2;
                switch(opc2){
                    case 1:{
                        cout<<"Ingresa un ID:"<<endl;
                        cin>>id;
                        AccederJugador(BuscarJugadorID(id));
                        }break;
                    case 2:{
                        cout<<"Ingresa un Nombre:"<<endl;
                        cin>>name;
                        AccederJugador(BuscarJugadorNombre(name));
                        }break;
                    default:{
                        cout<<"Esa opcion no existe!"<<endl;
                        }break;
                }
                }break;
            case 3:{
                MejorPuntaje();
                }break;
            case 4:{
                MostrarJugadores();
                }break;
            case 5:{
                cout<<"Gracias por usar."<<endl;
                exit(EXIT_SUCCESS);
                }break;
            default:{
                cout<<"Esa opcion no existe!"<<endl;
                }break;
        }
    }while(opc!=5);
    return 0;
}
