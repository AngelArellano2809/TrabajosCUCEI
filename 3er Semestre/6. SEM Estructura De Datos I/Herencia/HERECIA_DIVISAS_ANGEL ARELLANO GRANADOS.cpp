//ARELLANO GRANADOS ANGEL MARIANO
#include<iostream>
#include<cstdlib>

using namespace std;

bool Validacion(char aux[30]);

//Padre
class Moneda{
private:
    double valor;
public:
    void setValor(double valor);
    double getValor();
};

void Moneda::setValor(double valor){
    this->valor=valor;
}

double Moneda::getValor(){
    return this->valor;
}

//Hijo Peso
class Peso: public Moneda{
private:
    double T_dolar;
    double T_euro;
    double T_yen;
    double T_yuan;
public:
    void CalculaTDolar();
    double getT_dolar();
    void CalculaTEuro();
    double getT_euro();
    void CalculaTYen();
    double getT_yen();
    void CalculaTYuan();
    double getT_yuan();
};

void Peso::CalculaTDolar(){
    this->T_dolar=this->getValor()*0.049;
}

double Peso::getT_dolar(){
    return this->T_dolar;
}

void Peso::CalculaTEuro(){
    this->T_euro=this->getValor()*0.044;
}

double Peso::getT_euro(){
    return this->T_euro;
}

void Peso::CalculaTYen(){
    this->T_yen=this->getValor()*5.63;
}

double Peso::getT_yen(){
    return this->T_yen;
}

void Peso::CalculaTYuan(){
    this->T_yuan=this->getValor()*0.31;
}

double Peso::getT_yuan(){
    return this->T_yuan;
}

//Hijo Dolar
class Dolar: public Moneda{
private:
    double T_peso;
public:
    void CalculaTPeso();
    double getT_peso();
};

void Dolar::CalculaTPeso(){
    this->T_peso=this->getValor()*20.43;
}

double Dolar::getT_peso(){
    return this->T_peso;
}

//Hijo Euro
class Euro: public Moneda{
private:
    double T_peso;
public:
    void CalculaTPeso();
    double getT_peso();
};

void Euro::CalculaTPeso(){
    this->T_peso=this->getValor()*22.92;
}

double Euro::getT_peso(){
    return this->T_peso;
}

//Hijo Yen
class Yen: public Moneda{
private:
    double T_peso;
public:
    void CalculaTPeso();
    double getT_peso();
};

void Yen::CalculaTPeso(){
    this->T_peso=this->getValor()*0.18;
}

double Yen::getT_peso(){
    return this->T_peso;
}

//Hijo Yuan
class Yuan: public Moneda{
private:
    double T_peso;
public:
    void CalculaTPeso();
    double getT_peso();
};

void Yuan::CalculaTPeso(){
    this->T_peso=this->getValor()*3.23;
}

double Yuan::getT_peso(){
    return this->T_peso;
}

int main(){
    int opc=0;
    double mon;
    char aux[30];
    Peso p;
    Dolar d;
    Euro e;
    Yen ye;
    Yuan yu;
    do{
        system("cls");
        cout<<"1) Peso-Dolar"<<endl;
        cout<<"2) Dolar-Peso"<<endl;
        cout<<"3) Peso-Euro"<<endl;
        cout<<"4) Euro-Peso"<<endl;
        cout<<"5) Peso-Yen"<<endl;
        cout<<"6) Yen-Peso"<<endl;
        cout<<"7) Peso-Yuan"<<endl;
        cout<<"8) Yuan-Peso"<<endl;
        cout<<"9) Salir"<<endl;
        cout<<"Seleccione una opcion:"<<endl;
        cin>>opc;
        if(opc==9)
            break;
        cout<<"Que cantidad quiere convertir"<<endl;
        cin>>aux;
        if(Validacion(aux))
            mon=atof(aux);
        else{
            cout<<"No es un numero!"<<endl;
            break;
        }
        switch(opc){
            case 1:{
                p.setValor(mon);
                p.CalculaTDolar();
                cout<<p.getValor()<<" Pesos son "<<p.getT_dolar()<<" Dolares "<<endl;
                system("pause>>cls");
            }break;
            case 2:{
                d.setValor(mon);
                d.CalculaTPeso();
                cout<<d.getValor()<<" Dolares son "<<d.getT_peso()<<" Pesos "<<endl;
                system("pause>>cls");
            }break;
            case 3:{
                p.setValor(mon);
                p.CalculaTEuro();
                cout<<p.getValor()<<" Pesos son "<<p.getT_euro()<<" Euros "<<endl;
                system("pause>>cls");
            }break;
            case 4:{
                e.setValor(mon);
                e.CalculaTPeso();
                cout<<e.getValor()<<" Euros son "<<e.getT_peso()<<" Pesos "<<endl;
                system("pause>>cls");
            }break;
            case 5:{
                p.setValor(mon);
                p.CalculaTYen();
                cout<<p.getValor()<<" Pesos son "<<p.getT_yen()<<" Yenes "<<endl;
                system("pause>>cls");
            }break;
            case 6:{
                ye.setValor(mon);
                ye.CalculaTPeso();
                cout<<ye.getValor()<<" Yenes son "<<ye.getT_peso()<<" Pesos "<<endl;
                system("pause>>cls");
            }break;
            case 7:{
                p.setValor(mon);
                p.CalculaTYuan();
                cout<<p.getValor()<<" Pesos son "<<p.getT_yuan()<<" Yuanes "<<endl;
                system("pause>>cls");
            }break;
            case 8:{
                yu.setValor(mon);
                yu.CalculaTPeso();
                cout<<yu.getValor()<<" Yuanes son "<<yu.getT_peso()<<" Pesos "<<endl;
                system("pause>>cls");
            }break;
        }
    }while(opc!=9);
}

bool Validacion( char aux[30]){
    for(int i=0 ;i<sizeof(aux); i++ ){
        if(!((47<aux[i]<58)||(aux[i]==46)))
            return false;
    }
    return true;
}
