#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string.h>

void dec_bin(int dec);
void bin_dec(char*bin);
void dec_hex(int dec);
void hex_dec(char*hex);
void bin_hex(char*bin);
void hex_bin(char*hex);

int main(){
    int opc,decimal;

    do{
    char hexa[4]={0},binario[16]={0},subbin[4]={0};
    printf("\nELIJA UNA OPCION:\n \
           1.- Decimal a Binario\n \
           2.- Binario a Decimal\n \
           3.- Decimal a Hexadecimal\n \
           4.- Hexadecimal a Decimal\n \
           5.- Binario a Hexadecimal\n \
           6.- Hexadecimal a Binario\n \
           7.- Salir\n");
    scanf("%i",&opc);
    switch(opc){
        case 1:
            printf("Que numero decimal decea convertir:\n");
            scanf("%i",&decimal);
            dec_bin(decimal);
            break;
        case 2:
            printf("Que numero binario decea convertir:\n");
            fflush(stdin);
            gets(binario);
            bin_dec(binario);
            break;
        case 3:
            printf("Que numero decimal decea convertir:\n");
            scanf("%i",&decimal);
            dec_hex(decimal);
            break;
        case 4:
            printf("Que numero hexadecimal decea convertir:\n");
            fflush(stdin);
            gets(hexa);
            hex_dec(hexa);
            break;
        case 5:
            printf("Que numero binario decea convertir:\n");
            fflush(stdin);
            gets(binario);
            bin_hex(binario);
            break;
        case 6:
            printf("Que numero hexadecimal decea convertir:\n");
            fflush(stdin);
            gets(hexa);
            hex_bin(hexa);
            break;
        case 7:
            printf("Gracias");
            break;
    }}while(opc!=7);
}

dec_bin(int dec){
    char bin[16];
    int i;
    for(i=0;i<16;i++){
        bin[i]=dec%2;
        dec/=2;
    }
    printf("El numero en binario seria:\n");
    for(i=15;i>=0;i--){
        printf("%i",bin[i]);
    }
}

bin_dec(char*bin){
    int acum=0,i;
    for(i=0;i<16;i++){
        if (bin[i]=='0') bin[i]=0;
        if (bin[i]=='1') bin[i]=1;
        acum+=bin[i]*pow(2,i);
        }
    printf("El numero en decimal seria:\n%i",acum);
}

dec_hex(int dec){
    char hex[4];
    int i;
    for(i=0;i<4;i++){
        if((dec%16)==1) hex[i]='1';
        if((dec%16)==2) hex[i]='2';
        if((dec%16)==3) hex[i]='3';
        if((dec%16)==4) hex[i]='4';
        if((dec%16)==5) hex[i]='5';
        if((dec%16)==6) hex[i]='6';
        if((dec%16)==7) hex[i]='7';
        if((dec%16)==8) hex[i]='8';
        if((dec%16)==9) hex[i]='9';
        if((dec%16)==10) hex[i]='A';
        if((dec%16)==11) hex[i]='B';
        if((dec%16)==12) hex[i]='C';
        if((dec%16)==13) hex[i]='D';
        if((dec%16)==14) hex[i]='E';
        if((dec%16)==15) hex[i]='F';
        dec/=16;
    }
    printf("El numero en hexadecimal seria:\n");
    for(i=3;i>=0;i--){
        printf("%c",hex[i]);
    }
}

hex_dec(char*hex){
    int acum=0,i;
    hex=strrev(hex);
    for(i=0;i<4;i++){
        if(hex[i]=='0') hex[i]=0;
        if(hex[i]=='1') hex[i]=1;
        if(hex[i]=='2') hex[i]=2;
        if(hex[i]=='3') hex[i]=3;
        if(hex[i]=='4') hex[i]=4;
        if(hex[i]=='5') hex[i]=5;
        if(hex[i]=='6') hex[i]=6;
        if(hex[i]=='7') hex[i]=7;
        if(hex[i]=='8') hex[i]=8;
        if(hex[i]=='9') hex[i]=9;
        if(hex[i]=='A') hex[i]=10;
        if(hex[i]=='B') hex[i]=11;
        if(hex[i]=='C') hex[i]=12;
        if(hex[i]=='D') hex[i]=13;
        if(hex[i]=='E') hex[i]=14;
        if(hex[i]=='F') hex[i]=15;
        acum+=hex[i]*pow(16,i);
    }
    printf("El numero en decimal seria:\n%i",acum);
}

bin_hex(char*bin){
    int i;
    for(i=0;i<16;i=i+4){
        //printf("%i",i);
        if (bin[i]=='0'&&bin[i+1]=='0'&&bin[i+2]=='0'&&bin[i+3]=='0') printf("0");
        if (bin[i]=='0'&&bin[i+1]=='0'&&bin[i+2]=='0'&&bin[i+3]=='1') printf("1");
        if (bin[i]=='0'&&bin[i+1]=='0'&&bin[i+2]=='1'&&bin[i+3]=='0') printf("2");
        if (bin[i]=='0'&&bin[i+1]=='0'&&bin[i+2]=='1'&&bin[i+3]=='1') printf("3");
        if (bin[i]=='0'&&bin[i+1]=='1'&&bin[i+2]=='0'&&bin[i+3]=='0') printf("4");
        if (bin[i]=='0'&&bin[i+1]=='1'&&bin[i+2]=='0'&&bin[i+3]=='1') printf("5");
        if (bin[i]=='0'&&bin[i+1]=='1'&&bin[i+2]=='1'&&bin[i+3]=='0') printf("6");
        if (bin[i]=='0'&&bin[i+1]=='1'&&bin[i+2]=='1'&&bin[i+3]=='1') printf("7");
        if (bin[i]=='1'&&bin[i+1]=='0'&&bin[i+2]=='0'&&bin[i+3]=='0') printf("8");
        if (bin[i]=='1'&&bin[i+1]=='0'&&bin[i+2]=='0'&&bin[i+3]=='1') printf("9");
        if (bin[i]=='1'&&bin[i+1]=='0'&&bin[i+2]=='1'&&bin[i+3]=='0') printf("A");
        if (bin[i]=='1'&&bin[i+1]=='0'&&bin[i+2]=='1'&&bin[i+3]=='1') printf("B");
        if (bin[i]=='1'&&bin[i+1]=='1'&&bin[i+2]=='0'&&bin[i+3]=='0') printf("C");
        if (bin[i]=='1'&&bin[i+1]=='1'&&bin[i+2]=='0'&&bin[i+3]=='1') printf("D");
        if (bin[i]=='1'&&bin[i+1]=='1'&&bin[i+2]=='1'&&bin[i+3]=='0') printf("E");
        if (bin[i]=='1'&&bin[i+1]=='1'&&bin[i+2]=='1'&&bin[i+3]=='1') printf("F");
        }
    }

hex_bin(char*hex){
    int i;
    for(i=0;i<4;i++){
        if(hex[i]=='0') printf(" 0000 ");
        if(hex[i]=='1') printf(" 0001 ");
        if(hex[i]=='2') printf(" 0010 ");
        if(hex[i]=='3') printf(" 0011 ");
        if(hex[i]=='4') printf(" 0100 ");
        if(hex[i]=='5') printf(" 0101 ");
        if(hex[i]=='6') printf(" 0110 ");
        if(hex[i]=='7') printf(" 0111 ");
        if(hex[i]=='8') printf(" 1000 ");
        if(hex[i]=='9') printf(" 1001 ");
        if(hex[i]=='A') printf(" 1010 ");
        if(hex[i]=='B') printf(" 1011 ");
        if(hex[i]=='C') printf(" 1100 ");
        if(hex[i]=='D') printf(" 1101 ");
        if(hex[i]=='E') printf(" 1110 ");
        if(hex[i]=='F') printf(" 1111 ");
    }
}
