#include "Sala.h"

Sala::Sala()
{
    for(int i=0;i<5;i++)
        this->horarios[i]=-1;
}

Sala::~Sala()
{
}

void Sala::AgregarPelicula(){
    if(!uso){
        string nombre,director;
        int duracion;
        cout<<"Nombre de la pelicula:"<<endl;
        cin>>nombre;
        cout<<"Director de la pelicula:"<<endl;
        cin>>director;
        cout<<"Duracion de la pelicula (Minutos):"<<endl;
        cin>>duracion;
        pelicula=Pelicula(nombre,director,duracion);
        uso=true;
        cout<<"Registro exitoso"<<endl<<endl;
    }
    else
        cout<<"La sala alcanzo el limite de funciones"<<endl<<endl;
}

void Sala::AgregarHorario(){
    if (uso){
        if(cont < 5){
            float horario;
            int aux,a1=0,a2=0;
            cout<<"A que hora va a iniciar la funcion? (30 min = 0.5, ejemplo 9:30 = 9.5)"<<endl;
            cin>>horario;
            aux=horario*60;//transformar a minutos
            if(aux>=540&&aux<1320){
                for(int i=0;i<cont;i++){
                    if(aux>=horarios[i]+pelicula.getDuracion()+30 || aux<=horarios[i])
                        a1++;
                    if(aux+pelicula.getDuracion()+30<=horarios[i] || aux+pelicula.getDuracion()+30>=horarios[i]+pelicula.getDuracion()+30)
                        a2++;
                }
                if(a1==cont&&a2==cont){
                    horarios[cont]=aux;
                    cont++;
                    cout<<"Registro exitoso"<<endl<<endl;
                }
                else
                    cout<<"el horario no esta disponible"<<endl;
            }
            else
                cout<<"hora fuera del horario del cine"<<endl;
        }
        else
            cout<<"limite de horarios alcazado"<<endl;
    }
    else
        cout<<"la sala no tiene una pelicula registrada"<<endl;
}

void Sala::MostrarPelicula(char tipo,int pos){
    if(uso){
        if(cont>0){
            cout<<pelicula.getNombre()<<" -> "<<tipo<<pos<<" -> ";
            for(int i=0;i<cont;i++){
                cout<<horarios[i]/60<<" - ";
            }
            cout<<endl<<endl;
        }
        else
            cout<<"La sala no tiene funciones"<<endl<<endl;
    }
    else
        cout<<"la sala no tiene una pelicula registrada"<<endl;
}

void Sala::EliminarPelicula(){
    this->uso=false;
    this->cont=0;
    for(int i=0;i<5;i++)
        this->horarios[i]=-1;
    cout<<"Se a eliminado la sala con exito"<<endl;
}

int Sala::getHorario(){
    int opc;
    cout<<"Seleciona un horario"<<endl;
    for(int i=0;i<cont;i++){
        cout<<"Horario "<<i+1<<" : "<<horarios[i]/60<<endl;
    }
    cin>>opc;
    if(opc>0&&opc<=cont)
        return opc-1;
    else{
        cout<<"Ese horaio no esta registrado"<<endl;
        return -1;}
}

float Sala::getHorarioF(int pos){
    return horarios[pos]/60;
}

string Sala::getPelicula(){
    return pelicula.getNombre();
}

char Sala::Letra(int num){
    char letra;
    switch(num){
        case 0:{
            letra='A';
            break;
        }
        case 1:{
            letra='B';
            break;
        }
        case 2:{
            letra='C';
            break;
        }
        case 3:{
            letra='D';
            break;
        }
        case 4:{
            letra='E';
            break;
        }
        case 5:{
            letra='F';
            break;
        }
        case 6:{
            letra='G';
            break;
        }
        case 7:{
            letra='H';
            break;
        }
        case 8:{
            letra='I';
            break;
        }
        case 9:{
            letra='J';
            break;
        }
    }
    return letra;
}

int Sala:: Numero(char let){
    int num;
    switch(let){
        case 'A':{
            num=0;
            break;
        }
        case 'B':{
            num=1;
            break;
        }
        case 'C':{
            num=2;
            break;
        }
        case 'D':{
            num=3;
            break;
        }
        case 'E':{
            num=4;
            break;
        }
        case 'F':{
            num=5;
            break;
        }
        case 'G':{
            num=6;
            break;
        }
        case 'H':{
            num=7;
            break;
        }
        case 'I':{
            num=8;
            break;
        }
        case 'J':{
            num=9;
            break;
        }
    }
    return num;
}

bool Sala::getUso(){
    return uso;
}

int Sala::getCont(){
    return cont;
}
