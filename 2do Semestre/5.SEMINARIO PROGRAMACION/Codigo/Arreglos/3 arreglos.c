#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void main (){
    int i,A[10],B[10],C[10],acumA=0,acumB=0,acumC=0,MA,MB,MC,mA,mB,mC;

    srand(time(NULL));

    for(i=0;i<10;i++){
        A[i]=rand()%100;
    }
    for(i=0;i<10;i++){
        B[i]=rand()%100;
    }
    for(i=0;i<10;i++){
        C[i]=A[i]+B[i];
    }

    for(i=0;i<10;i++)
        acumA=acumA+A[i];
    for(i=0;i<10;i++)
        acumB=acumB+B[i];
    for(i=0;i<10;i++)
        acumC=acumC+C[i];

    MA=mA=A[0];
    MB=mB=B[0];
    MC=mC=C[0];
    for(i=0;i<10;i++){
        if(A[i]>MA) MA=A[i];
        if(B[i]>MB) MB=B[i];
        if(C[i]>MC) MC=C[i];
        if(A[i]<mA) mA=A[i];
        if(B[i]<mB) mB=B[i];
        if(C[i]<mC) mC=C[i];
    }

    printf("\t   \t A \t B \t C\n");
    for(i=0;i<10;i++)
        printf("\t[%i]\t %i \t %i \t %i\n",i,A[i],B[i],C[i]);
    printf("\nPromedio:\t %i \t %i \t %i\n",acumA/10,acumB/10,acumC/10);
    printf("\nMaximo:\t\t %i \t %i \t %i\n",MA,MB,MC);
    printf("\nMinimo:\t\t %i \t %i \t %i\n",mA,mB,mC);
}
