#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;
using std::cout; using std::endl;
using std::copy; using std::string;

void binario(int *numero);
string Conversor(int numero);

int main() {
    int a=0,*ptr=NULL;
    system("cls");
    cout<<"ingrese un numero a transformar a binario"<<endl;
    cin>>a;
    ptr=&a;
    binario(ptr);
    return 0;
}

void binario(int *numero){
    int cociente=0, residuo=0;
    string bin,aux;
    if(*numero>1){
        while(*numero/2>0){
            cociente=*numero/2;
            residuo=*numero%2;
            *numero=cociente;
            bin+=Conversor(residuo);
        }
        bin+=Conversor(cociente);
        for (int i = bin.size(); i >=0 ; i--)
                 aux += bin[i];
        cout<<"Binario = "<<aux<<endl;
    }
    else if (*numero==0)
        cout<<"Binario = "<<'0'<<endl;
    else if (*numero==1)
        cout<<"Binario = "<<'1'<<endl;
}

string Conversor(int numero){
    if(numero==1)
        return "1";
    if(numero==0)
        return "0";
}
