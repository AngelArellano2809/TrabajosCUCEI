#include<iostream>
#include<cmath>
using namespace std;

bool validacion(char num[1]);

//Padre
class Figuras{
private:
    double base;
    double altura;

public:
    void setBase(double base);
    double getBase();
    void setAltura(double altura);
    double getAltura();
};

void Figuras::setBase(double base){
  this->base=base;
}

double Figuras::getBase(){
    return this->base;
}

void Figuras::setAltura(double altura){
    this->altura=altura;
}

double Figuras::getAltura(){
    return this->altura;
}

//Hijo T
class triangulo: public Figuras{
private:
    double area;
public:
    void CalculaArea();
    double getArea();
};

void triangulo::CalculaArea(){
    this->area=(this->getBase()*this->getAltura())/2;
}

double triangulo::getArea(){
    return this->area;
}

//Hijo C
class cuadrado: public Figuras{
private:
    double area;
public:
    void CalculaArea();
    double getArea();
};

void cuadrado::CalculaArea(){
    this->area=(pow(this->getBase(),2));
}

double cuadrado::getArea(){
    return this->area;
}

//Hijo R
class rectangulo: public Figuras{
private:
    double area;
public:
    void CalculaArea();
    double getArea();
};

void rectangulo::CalculaArea(){
    this->area=(this->getBase()*this->getAltura());
}

double rectangulo::getArea(){
    return this->area;
}

//Hijo p
class poligono: public Figuras{
private:
    double area;
    double n_lados;
    double angulo;
    double apotema;
public:
    void CalculaArea();
    double getArea();
};

void poligono::CalculaArea(){
    this->angulo=(360/this->getAltura())/2;
    cout<<angulo<<endl;
    this->apotema=this->getBase()/(2*tan(this->angulo*3.1416/180));
    cout<<apotema<<endl;
    this->area=(this->getAltura()*this->getBase()*this->apotema)/2;
    cout<<area<<endl;
}

double poligono::getArea(){
    return this->area;
}

int main(){
    int opc=0;
    char a[1];
    double base=0,altura=0;
    triangulo t;
    cuadrado c;
    rectangulo r;
    poligono p;
    do{
        cout<<"Ingrese la Base/Lado:"<<endl;
        cin>>a;
        if(validacion(a))
            base=atoi(a);
        else
            break;
        cout<<"Ingrese la Altura/Numero de lados"<<endl;
        cin>>a;
        if(validacion(a))
            altura=atoi(a);
        else
            break;
        cout<<"Seleccione una figura:"<<endl;
        cout<<"1) Triangulo"<<endl;
        cout<<"2) Cuadrado"<<endl;
        cout<<"3) Rectangulo"<<endl;
        cout<<"4) Poligono"<<endl;
        cout<<"5) Salir"<<endl;
        cin>>opc;
        switch(opc){
        case 1:{
            t.setBase(base);
            t.setAltura(altura);
            t.CalculaArea();
            cout<<"Area de un triangulo de "<<t.getBase()<<" de base y "<<t.getAltura()<<" de altua es  = "<<t.getArea()<<endl;
        }break;
        case 2:{
            c.setBase(base);
            c.CalculaArea();
            cout<<"Area de un cuadrado de "<<c.getBase()<<" lados es  = "<<c.getArea()<<endl;
            }break;
        case 3:{
            r.setBase(base);
            r.setAltura(altura);
            r.CalculaArea();
            cout<<"Area de un rectangulo de "<<r.getBase()<<" de base y "<<r.getAltura()<<" de altua es  = "<<r.getArea()<<endl;
            }break;
        case 4:{
            p.setBase(base);
            p.setAltura(altura);
            p.CalculaArea();
            cout<<"Area de un poligono de "<<p.getBase()<<" como lado y "<<p.getAltura()<<" lados es  = "<<p.getArea()<<endl;
        }break;
        }

    }while(opc!=5);

    return 0;
}

bool validacion(char num[1]){
    if (47<num[0]<58)
        return true;
}
