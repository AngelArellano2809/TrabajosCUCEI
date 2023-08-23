#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define M 3
#define N 3
#define P 3

int main(){
    int i,j,k,A[M][N],B[N][P],C[M][P];
    srand(time(NULL));
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
            A[i][j]=rand()%10;

    for(i=0;i<N;i++)
        for(j=0;j<P;j++)
            B[i][j]=rand()%10;

    for(i=0;i<M;i++){
        for(j=0;j<P;j++){
            C[i][j]=0;
            for(k=0;k<N;k++){
                C[i][j]+=A[i][k]*B[k][j];
            }
        }
    }
    printf("MATRIZ A\n");
    for(i=0;i<M;i++){
        for(j=0;j<N;j++){
            printf("%3i",A[i][j]);
        }
        printf("\n");
    }
    printf("\nMATRIZ B\n");
    for(i=0;i<N;i++){
        for(j=0;j<P;j++){
            printf("%3i",B[i][j]);
        }
        printf("\n");
    }
    printf("\nMATRIZ C (resultado)\n");
    for(i=0;i<M;i++){
        for(j=0;j<P;j++){
            printf("%4i",C[i][j]);
        }
        printf("\n");
    }
}
