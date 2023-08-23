#include <iostream>
using namespace std;
int suma( int $a, int $b ){
    int $result;
    asm(
		"movl %1, %%eax;"
		"movl %2, %%ebx;"
		"addl %%ebx,%%eax;"
        "movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));
    return $result ;
}

int resta( int $a, int $b ){
    int $result;
    asm(
		"movl %1, %%eax;"
		"movl %2, %%ebx;"
		"subl %%ebx,%%eax;"
        "movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));
    return $result ;
}

int gcd( int $a, int $b ){
    int $result;
    asm(
		"movl %1, %%eax;"
		"movl %2, %%ebx;"
 "CONTD: cmpl $0, %%ebx;"
    	"je DONE;"
    	"xorl %%edx, %%edx;"
    	"idivl %%ebx;"
    	"movl %%ebx, %%eax;"
    	"movl %%edx, %%ebx;"
    	"jmp CONTD;"
  "DONE: movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));
    return $result ;
}

int sub(int x, int y){
    return x - y;
}

int mul(int $x, int $y, int $z){
    int $result;
    asm(
        "movl %1, %%eax;"
		"movl %2, %%ebx;"
		"mul %%ebx\n" /*eax * ebx*/
        "movl %3, %%ebx;"
        "mul %%ebx\n" //ebx * c
        "movl %%eax, %0;" : "=g" ( $result ) : "g" ( $x ), "g" ( $y ), "g" ( $z )
        );
    return $result;
}



int main(int argc, char** argv) {
	int a,b,c,d;
	cout<<"\nDigite el numero a: ";
	cin>>a;
	cout<<"\nDigite el numero b: ";
	cin>>b;
	cout<<"\nDigite el numero d: ";
	cin>>d;
	c=suma(a,b);
	cout<<"\nEl resultado de la suma de "<<a<<"+"<<b<<"="<<c<<"\n";
	c=resta(a,b);
	cout<<"\nEl resultado de la resta de "<<a<<"-"<<b<<"="<<c<<"\n";
	c=gcd(a,b);
	cout<<"\nEl resultado GCD("<<a<<","<<b<<")="<<c<<"\n";
	c=mul(a,b,d);
	cout<<"\nEl resultado de la multiplicacion de "<<a<<" x "<<b<<" x "<<d<<" = "<<c<<"\n";

    asm("subl %%ebx, %%eax;"
        "movl %%eax, %%ecx;"
        : "=c"  (c)
        : "a"   (a), "b" (b)
        :                   /* lista clobber vacia */
    );

    printf("a = %d\nb = %d\nc = %d\n", a, b, c);

    asm("addl %%ebx, %%eax;"
        "movl %%eax, %%ecx;"
        : "=c"  (c)
        : "a"   (a), "b" (b), "d" (d)
        :                   /* lista clobber vacia */
    );

    printf("a = %d\nb = %d\nc = %d\nd = %d", a, b, c,d);
	return 0;
}
