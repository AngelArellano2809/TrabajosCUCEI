#include "Cine.h"

Cine::Cine()
{
    //ctor
}

void Cine::Registrar(int pos,char tipo,int opc){
    switch(tipo){
    case 'G':{
        if(opc==1){
            salaG[pos].AgregarPelicula();
            }
        else if(opc==2){
            salaG[pos].AgregarHorario();
            }
        break;
    }
    case 'M':{
        if(opc==1){
            salaM[pos].AgregarPelicula();
            }
        else if(opc==2){
            salaM[pos].AgregarHorario();
            }
        break;
    }
    }
}


void Cine::MostrarTodo(){
    cout<<"Pelicula -> Sala -> Horarios"<<endl;
    cout<<"Salas Grandes: "<<endl;
    for(int i=0;i<2;i++){
        salaG[i].MostrarPelicula('G',i+1);
    }
    cout<<"Salas Medianas:"<<endl;
    for(int i=0;i<5;i++){
        salaM[i].MostrarPelicula('M',i+1);
    }
}

void Cine::eliminar(int pos,char tipo){
    switch(tipo){
    case 'G':{
        salaG[pos-1].EliminarAsientos();
        salaG[pos-1].EliminarPelicula();
        break;
    }
    case 'M':{
        salaM[pos-1].EliminarAsientos();
        salaM[pos-1].EliminarPelicula();
        break;
    }
    }
}

void Cine::venderAsiento(int pos,char tipo){
    switch(tipo){
    case 'G':{
        salaG[pos-1].AsignarAsiento(pos-1,tipo);
        break;
    }
    case 'M':{
        salaM[pos-1].AsignarAsiento(pos-1,tipo);
        break;
    }
    }
}

void Cine::BuscarId(int id){
    for(int i=0;i<2;i++)
        salaG[i].BuscaId(id);
    for(int i=0;i<5;i++)
        salaM[i].BuscaId(id);
    }

void Cine::BuscarNombre(string name){
    for(int i=0;i<2;i++)
        salaG[i].BuscaNombre(name);
    for(int i=0;i<5;i++)
        salaM[i].BuscaNombre(name);
}
