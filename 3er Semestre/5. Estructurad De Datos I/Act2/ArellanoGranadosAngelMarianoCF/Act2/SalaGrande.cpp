#include "SalaGrande.h"

SalaGrande::SalaGrande()
{

}

void SalaGrande::EliminarAsientos(){
    contAsientos=0;
}

void SalaGrande::AsignarAsiento(int pos, char tipo){
    if(contAsientos<700){
        int hor,col,fil;
        char fila;
        string name;
        stringstream sala;
        cout<<"Pelicula: "<<getPelicula()<<endl;;
        hor=getHorario();
        if(hor!=-1){
            cout<<"|----------------------------------------------|"<<endl;
            for(int i=0;i<10;i++){//filas
                cout<<"|";
                for(int j=0;j<14;j++){//columnas
                    if(asientos[i][j][hor].getOcupado()==false){
                        cout<<Letra(i)<<j+1<<"|";
                    }
                    else
                        cout<<"X |";
                }
                cout<<endl;
            }
            cout<<"|----------------------------------------------|"<<endl;
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

void SalaGrande::BuscaId(int id){
    if(getUso()){
        if(getCont()>0){
            if(contAsientos>0){
                for(int z=0;z<getCont();z++){
                    for(int x=0;x<10;x++){
                        for(int y=0;y<14;y++){
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

void SalaGrande::BuscaNombre(string name){
    if(getUso()){
        if(getCont()>0){
            if(contAsientos>0){
                for(int z=0;z<getCont();z++){
                    for(int x=0;x<10;x++){
                        for(int y=0;y<14;y++){
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
cout<<"||----------------------------------------------||"
cout<<"||A1|A2|A3|A4|A5|A6|A7|A8|A9|A10|A11|A12|A13|A14||"
cout<<"||B1|B2|B3|B4|B5|B6|B7|B8|B9|B10|B11|B12|B13|B14||"
cout<<"||C1|C2|C3|C4|C5|C6|C7|C8|C9|C10|C11|C12|C13|C14||"
cout<<"||D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14||"
cout<<"||E1|E2|E3|E4|E5|E6|E7|E8|E9|E10|E11|E12|E13|E14||"
cout<<"||F1|F2|F3|F4|F5|F6|F7|F8|F9|F10|F11|F12|F13|F14||"
cout<<"||G1|G2|G3|G4|G5|G6|G7|G8|G9|G10|G11|G12|G13|G14||"
cout<<"||H1|H2|H3|H4|H5|H6|H7|H8|H9|H10|H11|H12|H13|H14||"
cout<<"||I1|I2|I3|I4|I5|I6|I7|I8|I9|I10|I11|I12|I13|I14||"
cout<<"||J1|J2|J3|J4|J5|J6|J7|J8|J9|J10|J11|J12|J13|J14||"
cout<<"||----------------------------------------------||"
*/
