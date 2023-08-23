#include <iostream>
using namespace std;

double voto1=0,voto2=0,voto3=0,porcentaje1,porcentaje2,porcentaje3;
double *ptr1,*ptr2,*ptr3,a,b,c,p1,p2,p3,resp;
int opc=0;

double setVoto(double voto) {
    return voto+1;
}

double setPorcentajes(double voto,double a,double b,double c) {
    return (voto*100)/(a+b+c);
}

int main() {
do {
    system("cls");
    cout<<"Menu"<<endl;
    cout<<"Candidato -> Atlas [1]"<<endl;
    cout<<"Candidato -> Chivas [2]"<<endl;
    cout<<"Candidato -> Toluca [3]"<<endl;
    cout<<"Seleccione opcion"<<endl;
    cin>>opc;
    cout<<endl;
    cout<<endl;

    if(opc==1){
        voto1=setVoto(voto1);
        ptr1 = &voto1;
        a=*ptr1;
    }

    if(opc==2){
        voto2=setVoto(voto2);
        ptr2 = &voto2;
        b=*ptr2;
    }

    if(opc==3){
        voto3=setVoto(voto3);
        ptr3 = &voto3;
        c=*ptr3;
    }

    porcentaje1=setPorcentajes(voto1,a,b,c);
    ptr1 = &porcentaje1;
    p1=*ptr1;

    porcentaje2=setPorcentajes(voto2,a,b,c);
    ptr2 = &porcentaje2;
    p2=*ptr2;

    porcentaje3=setPorcentajes(voto3,a,b,c);
    ptr3 = &porcentaje3;
    p3=*ptr3;

    cout<<"*********VOTOS**********"<<endl;
    cout<<" Atlas: "<<a<<endl;
    cout<<" Chivas: "<<b<<endl;
    cout<<" Toluca: "<<c<<endl;
    cout<<endl;
    cout<<endl;
    cout<<"*****PORCENTAJES********"<<endl;
    cout<<" % Atlas "<<p1<<endl;
    cout<<" % Chivas "<<p2<<endl;
    cout<<" % Toluca "<<p3<<endl;
    cout<<endl;
    cout<<endl;
    cout<<"Ingresar nuevo voto 1 [si] 2[no]"<<endl;
    cin>>resp;
}while(resp!=2);
return 0;
}
