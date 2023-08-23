#include <iostream>
using namespace std;

int mayor (int *pv);
int vector []={5,7,9,20,78,15};
int main() {
    int *pv;
    pv = &vector[0];
    int m = mayor(pv);
    cout<<"El numero mayor es: "<<m<<endl;
    return 0;
}
int mayor(int *pv) {
    int may=0;
    for(int i=1; i<7; i++) {
        if(pv[i] < pv[i+1])
            may=pv[i+1];
    }
    return may;
}
