#include<iostream>
#include<cstdlib>
using namespace std;

double *ptr1=NULL, *ptr2=NULL;

double *suma(double *n1,double *n2){
    double *res=(double *)malloc (sizeof(double));
    *res =*n1+*n2;
    return res;
}

double numero1=0,numero2=0;

int main(){
    system("cls");
    cout<<"ingrese numero 1 "<<endl;
    cin>>numero1;
    cout<<"ingrese numero 2 "<<endl;
    cin>>numero2;
    ptr1=&numero1;
    ptr2=&numero2;
    cout<<"resultado = "<<*suma(ptr1,ptr2)<<endl;
    system("pause>>cls");
    return 0;
}
