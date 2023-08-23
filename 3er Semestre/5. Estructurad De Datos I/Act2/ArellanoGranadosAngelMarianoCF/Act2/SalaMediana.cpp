#include "SalaMediana.h"

SalaMediana::SalaMediana()
{

}

void SalaMediana::EliminarAsientos(){
    contAsientos=0;
}

void SalaMediana::AsignarAsiento(int pos,char tipo){
    if (contAsientos<280){
        int hor,col,fil;
        char fila;
        string name;
        stringstream sala;
        cout<<"Pelicula: "<<getPelicula()<<endl;;
        hor=getHorario();
        if(hor!=-1){
            cout<<"|-----------------------|"<<endl;
            for(int i=0;i<7;i++){//filas
                cout<<"|";
                for(int j=0;j<8;j++){//columnas
                    if(asientos[i][j][hor].getOcupado()==false){
                        cout<<Letra(i)<<j+1<<"|";
                    }
                    else
                        cout<<"X |";
                }
                cout<<endl;
            }
            cout<<"|-----------------------|"<<endl;
            cout<<"Seleccione un acciento disponible"<<endl;
            cout<<"Seleccione la fila (Letra):   ";
            cin>>fila;
            cout<<"Seleccione la columna (Numero):   ";
            cin>>col;
            cout<<"A que nombre quedaria el asiento:   ";
            cin>>name;
            fil=Numero(fila);
            sala<<tipo<<pos+1;
            asientos[fil][col-1][hor]=Asiento(sala.str(),getHorarioF(hor),name,fila,col);
            cout<<endl<<asientos[fil][col-1][hor].Detalles()<<endl;
            contAsientos++;
            cout<<"Registro exitoso"<<endl<<endl;
        }
    }
}

void SalaMediana::BuscaId(int id){
    if(getUso()){
        if(getCont()>0){
            if(contAsientos>0){
                for(int z=0;z<getCont();z++){
                    for(int x=0;x<7;x++){
                        for(int y=0;y<8;y++){
                            if(asientos[x][y][z].getId()==id){
                                cout<<asientos[x][y][z].Detalles()<<endl;
                            }
                        }
                    }
                }
            }
        }
    }
}

void SalaMediana::BuscaNombre(string name){
    if(getUso()){
        if(getCont()>0){
            if(contAsientos>0){
                for(int z=0;z<getCont();z++){
                    for(int x=0;x<7;x++){
                        for(int y=0;y<8;y++){
                            if(asientos[x][y][z].getNombre()==name){
                                cout<<asientos[x][y][z].Detalles()<<endl;
                            }
                        }
                    }
                }
            }
        }
    }
}

/*
cout<<"|-----------------------|"
cout<<"||A1|A2|A3|A4|A5|A6|A7|A8||"
cout<<"||B1|B2|B3|B4|B5|B6|B7|B8||"
cout<<"||C1|C2|C3|C4|C5|C6|C7|C8||"
cout<<"||D1|D2|D3|D4|D5|D6|D7|D8||"
cout<<"||E1|E2|E3|E4|E5|E6|E7|E8||"
cout<<"||F1|F2|F3|F4|F5|F6|F7|F8||"
cout<<"||G1|G2|G3|G4|G5|G6|G7|G8||"
cout<<"||-----------------------||"
*/
