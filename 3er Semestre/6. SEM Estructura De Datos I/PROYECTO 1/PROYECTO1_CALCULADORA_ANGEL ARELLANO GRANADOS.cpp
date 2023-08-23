 //ARELLANO GRANADOS ANGEL MARIANO 218123444
 #include <iostream>
 #include<cstdlib>
 #include <cstring>
 #include <string.h>
 #include <cmath>
using namespace std;

using std::pow; using std::cout;
using std::copy; using std::string; using std::bad_alloc;

double *Operaciones(char oper);
int Factorial(int*num);
string *Conversiones(int tipo);
string ConversorBin(int numero);
string ConversorHex(int numero);
string ConversorOct(int numero);
int ConversorDec(char num);
void Conversiones2(int tipo);
bool ValidacionBin(string *bin);
bool ValidacionOct(string *oct);
bool ValidacionHex(string *hex);

int main(){
    double res;
    string res2;
    int opc;
    system("cls");
    cout<<"M E N U "<<endl
        <<"1) Suma"<<endl
        <<"2) Resta"<<endl
        <<"3) Multiplicaion"<<endl
        <<"4) Division"<<endl
        <<"5) Potencia"<<endl
        <<"6) Factorial"<<endl
        <<"7) Decimal-Binario"<<endl
        <<"8) Binario-Decimal"<<endl
        <<"9) Decimal Octal"<<endl
        <<"10) Octal-Decimal"<<endl
        <<"11) Decimal-Hexadecimal"<<endl
        <<"12) Hexadecimal-Decimal"<<endl
        <<"Seleciones una opcion:"<<endl;
    cin>>opc;
    switch(opc){
        case 1:{
            res=*Operaciones('+');
            cout<<"La suma es = "<<res<<endl;
            }break;
        case 2:{
            res=*Operaciones('-');
            cout<<"La resta es = "<<res<<endl;
            }break;
        case 3:{
            res=*Operaciones('x');
            cout<<"La multiplicacion es = "<<res<<endl;
            }break;
        case 4:{
            res=*Operaciones('/');
            cout<<"La division es = "<<res<<endl;
            }break;
        case 5:{
            res=*Operaciones('P');
            cout<<"La potencia es = "<<res<<endl;
            }break;
        case 6:{
            int numero=0,*ptr;
            cout<<"Ingrese un numero:"<<endl;
            cin>>numero;
            ptr=&numero;
            cout<<"Su factorial es: "<<Factorial(ptr)<<endl;
        }break;
        case 7:{
            res2=*Conversiones(1);//"D_B"
        }break;
        case 8:{
            Conversiones2(1);//"B_D"
        }break;
        case 9:{
            res2=*Conversiones(2);//"D_O"
        }break;
        case 10:{
            Conversiones2(2);//"O_D"
        }break;
        case 11:{
            res2=*Conversiones(3);//"D_H"
        }break;
        case 12:{
            Conversiones2(3);//"H_D"
        }break;
    }
}

double *Operaciones(char oper){
    double *res=(double*)malloc (sizeof(double));
    double num1=0,*n1=NULL,num2=0,*n2=NULL;
    cout<<"Dame un numero:"<<endl;
    cin>>num1;
    n1=&num1;
    cout<<"Dame otro numero:"<<endl;
    cin>>num2;
    n2=&num2;
    switch(oper){
        case '+':{
            *res =*n1+*n2;
            return res;
        }break;
        case '-':{
            *res =*n1-*n2;
            return res;
        }break;
        case 'x':{
            *res =(*n1)*(*n2);
            return res;
        }break;
        case '/':{
            *res =(*n1)/(*n2);
            return res;
        }break;
        case 'P':{
            *res =pow(*n1,*n2);
            return res;
        }break;
    }
}

int Factorial(int*num){
    int *aux=NULL,acum=1;
    for(int i=2;i<=*num;i++){
        acum=acum*i;
    }
    aux=&acum;
    return *aux;
}

string *Conversiones(int tipo){
    int num1=0,*numero=NULL;
    int cociente=0, residuo=0;
    string bin,hexa,dec,oct,aux;
    cout<<"Dame un numero a convertir:"<<endl;
    cin>>num1;
    numero=&num1;
    switch(tipo){
        case 1:{
            if(*numero>1){
                while(*numero/2>0){
                    cociente=*numero/2;
                    residuo=*numero%2;
                    *numero=cociente;
                    bin+=ConversorBin(residuo);
                }
                bin+=ConversorBin(cociente);
                for (int i = bin.size(); i >=0 ; i--)
                    aux += bin[i];
                cout<<"Binario = "<<aux<<endl;
            }
            else if (*numero==0)
                cout<<"Binario = "<<'0'<<endl;
            else if (*numero==1)
                cout<<"Binario = "<<'1'<<endl;
        }break;
        case 2:{
            if (*numero >8){
                while(*numero/8>0){
                    cociente=*numero/8;
                    residuo=*numero%8;
                    *numero=cociente;
                    oct+=ConversorOct(residuo);
                }
                oct+=ConversorOct(cociente);
                for (int i = oct.size(); i >=0 ; i--)
                    aux += oct[i];
                cout<<"Octal = "<<aux<<endl;
            }
            else
                cout<<"Octal = "<<ConversorHex(*numero)<<endl;
        }break;
        case 3:{
            if (*numero >16){
                while(*numero/16>0){
                    cociente=*numero/16;
                    residuo=*numero%16;
                    *numero=cociente;
                    hexa+=ConversorHex(residuo);
                }
                hexa+=ConversorHex(cociente);
                for (int i = hexa.size(); i >=0 ; i--)
                    aux += hexa[i];
                cout<<"Hexadeciamal = "<<aux<<endl;
            }
            else
                cout<<"Hexadeciamal = "<<ConversorHex(*numero)<<endl;
        }break;
    }
}

void Conversiones2(int tipo){
    string num1,*numero=NULL,aux;
    int acum=0,i;
    cout<<"Dame un numero a convertir:"<<endl;
    cin>>num1;
    numero=&num1;
    switch(tipo){
        case 1:{
            if(ValidacionBin(numero)==true){
                aux=*numero;
                for(i=0;i<aux.size();i++)
                    if(aux[i]=='1'){
                        acum+=pow(2,(aux.size()-i-1));
                        cout<<acum<<endl;
                    }
                cout<<"Decimal = "<<acum<<endl;
            }
            else
                cout<<"Numero no valido"<<endl;
        }break;
        case 2:{
            if(ValidacionOct(numero)==true){
                aux=*numero;
                for(i=0;i<aux.size();i++){
                    int j = ConversorDec(aux[i]);
                    acum+=(j)*(pow(8,(aux.size()-i-1)));
                }
                cout<<"Decimal = "<<acum<<endl;
            }
            else
                cout<<"Numero no valido"<<endl;
        }break;
        case 3:{
            if(ValidacionHex(numero)==true){
                aux=*numero;
                for(i=0;i<aux.size();i++){
                    int j = ConversorDec(aux[i]);
                    acum+=(j)*(pow(16,(aux.size()-i-1)));
                }
                cout<<"Decimal = "<<acum<<endl;
            }
            else
                cout<<"Numero no valido"<<endl;
        }break;
    }
}

string ConversorBin(int numero){
    if(numero==1)
        return "1";
    if(numero==0)
        return "0";
}

string ConversorHex(int numero){
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

string ConversorOct(int numero){
    string oct;
    switch(numero){
        case 0:
            oct='0'; break;
        case 1:
            oct='1'; break;
        case 2:
            oct='2'; break;
        case 3:
            oct='3'; break;
        case 4:
            oct='4'; break;
        case 5:
            oct='5'; break;
        case 6:
            oct='6'; break;
        case 7:
            oct='7'; break;
    }
    return oct;
}

bool ValidacionBin(string *bin){
    string aux;
    int acum,i;
    aux=*bin;
    for(i=0;i<aux.size();i++)
        if(aux[i]==48 || aux[i]==49)
            acum++;
    if(acum==aux.size())
        return true;
    else
        return false;
}

bool ValidacionOct(string *oct){
    string aux;
    int acum,i;
    aux=*oct;
    for(i=0;i<aux.size();i++)
        if(aux[i]>47 && aux[i]<57)
            acum++;
    if(acum==aux.size())
        return true;
    else
        return false;
}

bool ValidacionHex(string *hex){
    string aux;
    int acum,i;
    aux=*hex;
    for(i=0;i<aux.size();i++)
        if((aux[i]>47 && aux[i]<58)||(aux[i]>64 && aux[i]<71))
            acum++;
    if(acum==aux.size())
        return true;
    else
        return false;
}

int ConversorDec(char num){
    //string aux=*num;
    switch(num){
        case '0':{
            return 0;
        }
        case '1':{
            return 1;
        }
        case '2':{
            return 2;
        }
        case '3':{
            return 3;
        }
        case '4':{
            return 4;
        }
        case '5':{
            return 5;
        }
        case '6':{
            return 6;
        }
        case '7':{
            return 7;
        }
        case '8':{
            return 8;
        }
        case '9':{
            return 9;
        }
        case 'A':{
            return 10;
        }
        case 'B':{
            return 11;
        }
        case 'C':{
            return 12;
        }
        case 'D':{
            return 13;
        }
        case 'E':{
            return 14;
        }
        case 'F':{
            return 15;
        }
    }

}
