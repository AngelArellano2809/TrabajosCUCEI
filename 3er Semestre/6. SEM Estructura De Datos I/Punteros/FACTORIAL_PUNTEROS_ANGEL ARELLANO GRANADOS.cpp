 //ARELLANO GRANADOS ANGEL MARIANO 218123444
 #include <iostream>
 #include <cstdlib>
using namespace std;

int Factorial(int*num){
    int *aux=NULL,i,acum=1;
    for(i=2;i<=*num;i++){
        acum=acum*i;
    }
    aux=&acum;
    return *aux;
}

int main(){
    int numero=0,*ptr;
    cout<<"Ingrese un numero:"<<endl;
    cin>>numero;
    ptr=&numero;
    cout<<"Su factorial es: "<<Factorial(ptr)<<endl;
    return EXIT_SUCCESS;
}
