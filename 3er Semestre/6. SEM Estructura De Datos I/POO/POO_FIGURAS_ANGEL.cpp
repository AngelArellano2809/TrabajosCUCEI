//ARELLANO GRANADOS ANGEL MARIANO
#include<iostream>
#include<cstdlib>
#include<math.h>

using namespace std;

//triangulo.h
class triangulo{
private:
    double base;
    double altura;
    double area;
public:
    void setBase(double);
    double getBase();
    void setAltura(double);
    double getAltura();
    void CalculaArea();
    double getArea();
};

//tringulo.cpp
void triangulo::setBase(double base){
    this->base=base;
}

double triangulo::getBase(){
    return this->base;
}

void triangulo::setAltura(double altura){
    this->altura=altura;
}

double triangulo::getAltura(){
    return this->altura;
}

void triangulo::CalculaArea(){
    this->area=(this->base*this->altura)/2;
}

double triangulo::getArea(){
    return this->area;
}

//cuadrado.h
class cuadrado{
    private:
    double base;
    double area;
public:
    void setBase(double);
    double getBase();
    void CalculaArea();
    double getArea();
};

//cuadrado.cpp
void cuadrado::setBase(double base){
    this->base=base;
}

double cuadrado::getBase(){
    return this->base;
}

void cuadrado::CalculaArea(){
    this->area=(this->base*this->base);
}

double cuadrado::getArea(){
    return this->area;
}

//rectangulo.h
class rectangulo{
private:
    double base;
    double altura;
    double area;
public:
    void setBase(double);
    double getBase();
    void setAltura(double);
    double getAltura();
    void CalculaArea();
    double getArea();
};

//rectangulo.cpp
void rectangulo::setBase(double base){
    this->base=base;
}

double rectangulo::getBase(){
    return this->base;
}

void rectangulo::setAltura(double altura){
    this->altura=altura;
}

double rectangulo::getAltura(){
    return this->altura;
}

void rectangulo::CalculaArea(){
    this->area=(this->base*this->altura);
}

double rectangulo::getArea(){
    return this->area;
}

//poligono.h
class poligono{
private:
    double lado;
    double num_lados;
    double angulo;
    double apotema;
    double area;
public:
    void setLado(double);
    double getLado();
    void setNumLados(double);
    double getNumLados();
    void CalculaAngulo();
    void CalculaApotema();
    void CalculaArea();
    double getArea();
};

//poligono.cpp
void poligono::setLado(double lado){
    this->lado=lado;
}

double poligono::getLado(){
    return this->lado;
}

void poligono::setNumLados(double num_lados){
    this->num_lados=num_lados;
}

double poligono::getNumLados(){
    return this->num_lados;
}

void poligono::CalculaAngulo(){
    this->angulo=(360/this->num_lados);
}

void poligono::CalculaApotema(){
    double aux;
    this->apotema=this->lado/(2*std::tan(angulo/2));
}

void poligono::CalculaArea(){
    this->area=(this->num_lados*this->lado*this->apotema)/2;
}

double poligono::getArea(){
    return this->area;
}

//main.cpp
int main(){
    double base=0,altura=0,lado=0,num_lados=0;
    int opc=0;
    triangulo t;
    cuadrado c;
    rectangulo r;
    poligono p;
    do{
        system("cls");
        cout<<"1) Triangulo"<<endl;
        cout<<"2) Cuadrado"<<endl;
        cout<<"3) Rectangulo"<<endl;
        cout<<"4) poligono"<<endl;
        cout<<"5) salir"<<endl;
        cout<<"Selecione una opcion:"<<endl;
        cin>>opc;
        switch(opc){
            case 1:{
                cout<<"Ingrese base"<<endl;
                cin>>base;
                cout<<"Ingrese altura"<<endl;
                cin>>altura;
                t.setBase(base);
                t.setAltura(altura);
                t.CalculaArea();
                cout<<"Area de un triangulo de "<<t.getBase()<<" de base y "<<t.getAltura()<<" de altua es  = "<<t.getArea()<<endl;
                system("pause>>cls");
            }break;
            case 2:{
                cout<<"Ingrese un lado"<<endl;
                cin>>base;
                c.setBase(base);
                c.CalculaArea();
                 cout<<"Area de un cuadrado de "<<c.getBase()<<" lados es  = "<<c.getArea()<<endl;
                system("pause>>cls");
            }break;
            case 3:{
                cout<<"Ingrese base"<<endl;
                cin>>base;
                cout<<"Ingrese altura"<<endl;
                cin>>altura;
                r.setBase(base);
                r.setAltura(altura);
                r.CalculaArea();
                cout<<"Area de un rectangulo de "<<r.getBase()<<" de base y "<<r.getAltura()<<" de altua es  = "<<r.getArea()<<endl;
                system("pause>>cls");
            }break;
            case 4:{
                cout<<"Ingrese el lado"<<endl;
                cin>>lado;
                cout<<"Ingrese el numero de lados"<<endl;
                cin>>num_lados;
                p.setLado(lado);
                p.setNumLados(num_lados);
                p.CalculaAngulo();
                p.CalculaApotema();
                p.CalculaArea();
                cout<<"Area de un poligono de "<<p.getLado()<<" como lado y "<<p.getNumLados()<<" lados es  = "<<p.getArea()<<endl;
                system("pause>>cls");
            }break;
        }

    }while(opc!=5);
    return 0;
}
