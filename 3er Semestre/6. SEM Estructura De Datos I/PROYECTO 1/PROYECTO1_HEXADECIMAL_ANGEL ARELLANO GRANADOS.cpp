#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;
using std::cout; using std::endl;
using std::copy; using std::string;

void Hexadecimal(int *numero);
string Conversor(int numero);

int main() {
    system("cls");
    int a=0,*ptr1=NULL;
    cout<<"ingrese numero a convertir a Hexadecimal:"<<endl;
    cin>>a;
    ptr1=&a;
    Hexadecimal(ptr1);
    return 0;
}

void Hexadecimal (int *numero){
    int cociente=0,residuo=0;
    string hexa,aux;
    if (*numero >16){
        while(*numero/16>0){
            cociente=*numero/16;
            residuo=*numero%16;
            *numero=cociente;
            hexa+=Conversor(residuo);
        }
        hexa+=Conversor(cociente);
        for (int i = hexa.size(); i >=0 ; i--)
             aux += hexa[i];
        //cout<<hexa<<endl;
        cout<<"Decimal = "<<aux<<endl;
    }
    else
        cout<<"Decimal = "<<Conversor(*numero)<<endl;
}

string Conversor(int numero){
    string hex;
    switch(numero){
        case 0:
            hex='0'; break;
        case 1:
            hex='1'; break;
        case 2:
            hex='2'; break;
        case 3:
            hex='3'; break;
        case 4:
            hex='4'; break;
        case 5:
            hex='5'; break;
        case 6:
            hex='6'; break;
        case 7:
            hex='7'; break;
        case 8:
            hex='8'; break;
        case 9:
            hex='9'; break;
        case 10:
            hex='A'; break;
        case 11:
            hex='B'; break;
        case 12:
            hex='C'; break;
        case 13:
            hex='D'; break;
        case 14:
            hex='E'; break;
        case 15:
            hex='F'; break;
    }
    return hex;
}
