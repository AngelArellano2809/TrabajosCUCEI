//ARELLANO GRANADOS ANGEL MARIANO
#include<iostream>
#include<cstdlib>
#include<math.h>

using namespace std;

class Celsius{
private:
    double tem;
    double transformacion1;
    double transformacion2;
public:
    void setTem(double celsius);
    void Cel_Kel();
    void Cel_Fah();
    double getKel();
    double getFah();
};

void Celsius::setTem(double celsius){
    this->tem=celsius;
}

void Celsius::Cel_Kel(){
    this->transformacion1=this->tem+ 273.15;
}

void Celsius::Cel_Fah(){
    this->transformacion2=(this->tem*1.8)+32;
}

double Celsius::getKel(){
    return this->transformacion1;
}

double Celsius::getFah(){
    return this->transformacion2;
}


class Kelvin{
private:
    double tem;
    double transformacion;
public:
    void setTem(double kelvin);
    void Kel_Cel();
    double getCel();
};

void Kelvin::setTem(double kelvin){
    this->tem=kelvin;
}

void Kelvin::Kel_Cel(){
    this->transformacion=this->tem-273.15;
}

double Kelvin::getCel(){
    return this->transformacion;
}

class Fahrenheit{
private:
    double tem;
    double transformacion;
public:
    void setTem(double fahrenheit);
    void Fah_Cel();
    double getCel();
};

void Fahrenheit::setTem(double fahrenheit){
    this->tem=fahrenheit;
}

void Fahrenheit::Fah_Cel(){
    this->transformacion=(this->tem-32)/1.8;
}

double Fahrenheit::getCel(){
    return this->transformacion;
}

int main(){
    double celsius=0,kelvin=0,fahrenheit=0;
    int opc=0;
    Celsius c;
    Kelvin k;
    Fahrenheit f;
    do{
        system("cls");
        cout<<"1) Celsius-Kelvin"<<endl;
        cout<<"2) Kelvin-Celsius"<<endl;
        cout<<"3) Celsius-Fahrenheit"<<endl;
        cout<<"4) Fahrenheit-Celsius"<<endl;
        cout<<"5) salir"<<endl;
        cout<<"Selecione una opcion:"<<endl;
        cin>>opc;
        switch(opc){
            case 1:{
                cout<<"Ingrese los grados a convertir"<<endl;
                cin>>celsius;
                c.setTem(celsius);
                c.Cel_Kel();
                cout<<"Kelvin = "<<c.getKel()<<endl;
                system("pause>>cls");
            }break;
            case 2:{
                cout<<"Ingrese los grados a convertir"<<endl;
                cin>>kelvin;
                k.setTem(kelvin);
                k.Kel_Cel();
                cout<<"Celsius = "<<k.getCel()<<endl;
                system("pause>>cls");
            }break;
             case 3:{
                cout<<"Ingrese los grados a convertir"<<endl;
                cin>>celsius;
                c.setTem(celsius);
                c.Cel_Fah();
                cout<<"Kelvin = "<<c.getFah()<<endl;
                system("pause>>cls");
            }break;
            case 4:{
                cout<<"Ingrese los grados a convertir"<<endl;
                cin>>fahrenheit;
                f.setTem(fahrenheit);
                f.Fah_Cel();
                cout<<"Celsius = "<<f.getCel()<<endl;
                system("pause>>cls");
            }break;
        }

    }while(opc!=5);
    return 0;
}
