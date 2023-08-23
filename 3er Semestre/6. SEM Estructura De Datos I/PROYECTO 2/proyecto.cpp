#include <iostream>
#include <windows.h>
#include <ctime>
#include <conio.h>

 using namespace std;

 void ShowConsoleCursor(bool showFlag){
    HANDLE out = GetStdHandle(STD_OUTPUT_HANDLE);

    CONSOLE_CURSOR_INFO     cursorInfo;

    GetConsoleCursorInfo(out, &cursorInfo);
    cursorInfo.bVisible = showFlag; // set the cursor visibility
    SetConsoleCursorInfo(out, &cursorInfo);
}

 void gotoxy(int x,int y){
      HANDLE hcon;
      hcon = GetStdHandle(STD_OUTPUT_HANDLE);
      COORD dwPos;
      dwPos.X = x;
      dwPos.Y= y;
      SetConsoleCursorPosition(hcon,dwPos);
 }

 struct Cliente{
     int id;
     string nombre;
     int maletas;
 };

 class cola{
	private:
		int inicio,fin;
        Cliente p1[10];
	public:
       cola();
       int lleno();
       void llenar(string nombre);
       void mostrar_cola();
       void eliminar();
       int getMaletas(int pos);
};

cola::cola(){
	fin=-1;//final
	inicio=0;//frente
}

int cola::getMaletas(int pos){
    return this->p1[pos].maletas;
}

int cola::lleno(){
	if(fin==9){
		cout<<"LA COLA ESTA LLENA"<<endl;
		system("pause");
		return 1;
	}else{
		return 0;
	}
}

void cola::llenar(string name){
    fin ++;
    if(!lleno()){
 		p1[fin].id=1+rand()%100;
 		p1[fin].nombre=name;
 		p1[fin].maletas=1+rand()%10;
	 }
 }

 void cola::eliminar(){
		for(int i=0;i<=fin;i++){
			p1[i]=p1[i+1];
		}
		p1[fin].id= 0;
		p1[fin].nombre="";
		p1[fin].maletas= 0;
		fin--;
}

void cola::mostrar_cola(){
    for(int i=fin;i>=0;i--){
        cout<<"Cliente No. "<<i+1<<endl;
        cout<<"ID: "<<p1[i].id<<endl;
        cout<<"Nombre: "<<p1[i].nombre<<endl;
        cout<<"# Maletas: "<<p1[i].maletas<<endl<<endl;
    }
}

 struct Pasajero{
     int Asiento;
     string nombre;
     int destino;
 };

 class pila{
	private:
	    Pasajero p2[10];
	    int tope;
	public:
		pila();
		void push(string name);
		void pop();
		void mostrar_pila();
 };

 pila::pila(){
	 tope=-1;
}

void pila::push(string name){
    tope ++;
    p2[tope].Asiento=1+rand()%100;
    p2[tope].nombre=name;
    p2[tope].destino=1+rand()%5;
}

void pila::mostrar_pila(){
    system("cls");
    cout<<"Pasajeros del avion:"<<endl<<endl;
    for(int i=tope;i>=0;i--){
        cout<<"Cliente No. "<<i+1<<endl;
        cout<<"Asiento: "<<p2[i].Asiento<<endl;
        cout<<"Nombre: "<<p2[i].nombre<<endl;
        switch(p2[i].destino){
        case 1:{
            cout<<"Destino: Londres"<<endl<<endl;
            break;
        }
        case 2:{
            cout<<"Destino: Barcelona"<<endl<<endl;
            break;
        }
        case 3:{
            cout<<"Destino: Los Angeles"<<endl<<endl;
            break;
        }
        case 4:{
            cout<<"Destino: Seul"<<endl<<endl;
            break;
        }
        case 5:{
            cout<<"Destino: Tokio"<<endl<<endl;
            break;
        }
        }
    }
    system("pause");
  }

 void aeropuerto(int cont,cola cola1){
     system("cls");
     int ban=0,aux=0;
     cout<<"**COMPRA DE BOLETOS**"<<endl;;
     cola1.mostrar_cola();
     gotoxy(100,7);  cout<< "|||||||||||||";
     gotoxy(100,8);  cout<< "||Recepcion||";
     gotoxy(100,9);  cout<< "|||||||||||||";
     gotoxy(100,10); cout<< "|    o     ||";
     gotoxy(100,11); cout<< "|   /|\\    ||";
     gotoxy(100,12); cout<< "|||||||||||||";
     do{
	 for(int j=95;j>=95-((cont-1)*5);j-=5){
        for(int i=30;i<j;i++){
            gotoxy(i,9);cout<< "  "<<aux+1;
            gotoxy(i,10);cout<< "  o";
            gotoxy(i,11); cout<< " /|\\";
            if(i<j){
                if(ban==0){
                        gotoxy(i,12); cout<< "  | ";
                    ban=1;
                }else{
                    gotoxy(i,12); cout<< " / \\";
                    ban=0;
                }
            }
            if(i==j-1){
                gotoxy(i,12); cout<< " / \\";
            }

             Sleep(100);
        }
        aux++;
	 }
     }while(aux<cont);
     for(int l=95;l>=95-((cont-1)*5);l-=5){
        int aux2=0;
         gotoxy(l,9);  cout<< "     ";
         gotoxy(l,10); cout<< "     ";
         gotoxy(l,11); cout<< "     ";
         gotoxy(l,12); cout<< "     ";
         cout<<"\n"<<endl;
         Sleep(100*cola1.getMaletas(aux2++));
     }
 }

 void pila::pop(){
		p2[tope].Asiento= 0;
		p2[tope].nombre="";
		p2[tope].destino= 0;
		tope --;
}

 void avion(){
     system("cls");
     for(int i=0;i<110;i++){
        gotoxy(i,9);cout<< "     ____";
        gotoxy(i,10);cout<<"     \\  `.";
        gotoxy(i,11);cout<<"      \\   `.";
        gotoxy(i,12);cout<<"       \ \   `.";
        gotoxy(i,13);cout<<"        \\01838`.";
        gotoxy(i,14);cout<<"        :. . . . `._______________________.-~|~~-._";
        gotoxy(i,15);cout<<"        \                                 ---'-----`-._";
        gotoxy(i,16);cout<<"        \                                 ---'-----`-.__\\";
        gotoxy(i,17);cout<<"         /�������/             _...---------..         ~-.\\___";
        gotoxy(i,18);cout<<"        //     .`_________  .-`           \ .-~           /";
        gotoxy(i,19);cout<<"       //    .'       ||__.~             .-~_____________/";
        gotoxy(i,20);cout<<"      //___.`           .~            .-~";
        gotoxy(i,21);cout<<"                      .~           .-~";
        gotoxy(i,22);cout<<"                    .~         _.-~";
        gotoxy(i,23);cout<<"                    `-_____.-~'";
        Sleep(100);
     }
 }

 void taxi(int cont){
     int aux=1,x;
     while(cont){
         system("cls");
         x=aux++;
         cout<<"**PARADA DE TAXI**"<<endl;;
         for(int i=95;i>=95-((cont-1)*5);i-=5){
            gotoxy(i,9);  cout<< "  "<<x++;
            gotoxy(i,10); cout<< "  o";
            gotoxy(i,11); cout<< " /|\\";
            gotoxy(i,12); cout<< " / \\";
        }
         for(int i=30;i<90;i++){
            gotoxy(i,14);cout<<"     ________";
            gotoxy(i,15);cout<<"    / / | |  \\";
            gotoxy(i,16);cout<<" __/ /__| |___\\____";
            gotoxy(i,17);cout<<"|  _  =TAXI= _    |)";
            gotoxy(i,18);cout<<"|_/ \\______/ \\_____|";
            gotoxy(i,19);cout<<"  \\_/      \\_/";
            Sleep(100);
        }
         gotoxy(95,9); cout<< "     ";
         gotoxy(95,10);cout<< "     ";
         gotoxy(95,11);cout<< "     ";
         gotoxy(95,12);cout<< "     ";
         Sleep(700);
        cont--;
     }
 }
int main(int argc, char** argv) {
	 int cont=0,opc;
	 string name;
	 cola cola1;
	 pila pila1;
	 cola cola2;
	 ShowConsoleCursor(false);
    do{
        system("cls");
        cout<<"Ingrese el nombre de cliente "<<cont+1<<endl;
        cin>>name;
        cola1.llenar(name);
        pila1.push(name);
        cola2.llenar(name);
        cola1.mostrar_cola();
        cont++;
        cout<<"desea ingresar otro cliente?   1.-Si  0.-NO"<<endl;
        cin>>opc;
    }while(opc);
    aeropuerto(cont,cola1);
    for(int i=0;i<cont;i++)
        cola1.eliminar();
    pila1.mostrar_pila();
    avion();
    for(int i=0;i<cont;i++)
        pila1.pop();
    for(int i=0;i<cont;i++)
        cola2.eliminar();
    taxi(cont);

}
