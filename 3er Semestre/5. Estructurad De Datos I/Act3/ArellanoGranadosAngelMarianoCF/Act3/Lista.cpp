#include "Lista.h"

Lista::Lista()
{
    this->cont=0;
}

void Lista::inserta(){
    string nombre,autor,editorial,isbn,categoria,categoriaSec;
    int ejemDisp;
    float precio;

    cout<<"Ingresa el nombre del libro: "<<endl;
    cin>>nombre;
    cout<<"Ingresa el autor del libro: "<<endl;
    cin>>autor;
    cout<<"Ingresa la editorial del libro: "<<endl;
    cin>>editorial;
    cout<<"Ingresa el ISBN del libro: "<<endl;
    cin>>isbn;
    cout<<"Ingresa la categoria del libro: "<<endl;
    cin>>categoria;
    cout<<"Ingresa la categoria Secundaria del libro: "<<endl;
    cin>>categoriaSec;
    cout<<"Ingresa la Cantidad existente de libros: "<<endl;
    cin>>ejemDisp;
    cout<<"Ingresa el Precio del libro: "<<endl;
    cin>>precio;

    libros[cont].setNombre(nombre);
    libros[cont].setAutor(autor);
    libros[cont].setEditorial(editorial);
    libros[cont].setIsbn(isbn);
    for(int i=0;i<cont;i++){
        if(isbn==libros[i].getIsbn()){
            cout<<"El ISBN ya esta en uso"<<endl;
            return;
        }
    }
    libros[cont].setCategoria(categoria);
    libros[cont].setCategoriaSec(categoriaSec);
    libros[cont].setEjemDisp(ejemDisp);
    libros[cont].setEjemVend(0);
    libros[cont].setPrecio(precio);
    cont++;
}

int Lista::buscar(){
    int opc;
    string cad;
    cout<<"1) ISBN"<<endl<<"2) Nombre"<<endl;
    cin>>opc;
    cout<<"Cual es el dato a buscar?"<<endl;
    cin>>cad;
    if(opc==1){
        for(int i=0;i<cont;i++){
            if(libros[i].getIsbn()==cad){
                return i;
            }
        }
        return -1;
    }
    else if(opc==2){
        for(int j=0;j<cont;j++){
            if(libros[j].getNombre()==cad){
                mostrar(j);
            }
        }
        return -1;
    }
}

void Lista::mostrar(int pos){
    if(pos!=-1){
        cout<<endl;
        cout<<"NOMBRE: "<<libros[pos].getNombre()<<endl;
        cout<<"AUTOR: "<<libros[pos].getAutor()<<endl;
        cout<<"EDITORIAL: "<<libros[pos].getEditorial()<<endl;
        cout<<"ISBN: "<<libros[pos].getIsbn()<<endl;
        cout<<"CATEGORIA: "<<libros[pos].getCategoria()<<endl;
        cout<<"CATEGORIA SECUNDARIA: "<<libros[pos].getCategoriaSec()<<endl;
        cout<<"EJEMPLARES DISPONIBLES: "<<libros[pos].getEjemDisp()<<endl;
        cout<<"EJEMPLARES VENDIDOS: "<<libros[pos].getEjemVend()<<endl;
        cout<<"PRECIO: "<<libros[pos].getPrecio()<<endl;
        cout<<endl;
    }
}

void Lista::modificar(){
    string cad,str;
    int opc,num;
    float flo;
    cout<<"Introduce en IBSN del libro a modificar:"<<endl;
    cin>>cad;
    for(int i=0;i<cont;i++){
        if(libros[i].getIsbn()==cad){
            cout<<"Que caracteristica se editara"<<"1) Nombre"<<endl<<"2) Autor"<<endl<<"3) Edirorial"<<endl<<"4) ISBN"<<endl<<"5) Categoria"<<endl<<"6) Categoria Secundaria"
                <<endl<<"7) Ejemplares Disponibles"<<endl<<"8) Ejemplares Vendidos"<<endl<<"9) Precio"<<endl;
            cin>>opc;
            cout<<"ingresa el nuevo dato"<<endl;
            if(opc>=1&&opc<=6){cin>>str;}
            else if(opc==7||opc==8){cin>>num;}
            else if(opc==9){cin>>flo;}
            switch(opc){
                case 1:{
                    libros[i].setNombre(str);
                }break;
                case 2:{
                    libros[i].setAutor(str);
                }break;
                case 3:{
                    libros[i].setEditorial(str);
                }break;
                case 4:{
                    libros[i].setIsbn(str);
                }break;
                case 5:{
                    libros[i].setCategoria(str);
                }break;
                case 6:{
                    libros[i].setCategoriaSec(str);
                }break;
                case 7:{
                    libros[i].setEjemDisp(num);
                }break;
                case 8:{
                    libros[i].setEjemVend(num);
                }break;
                case 9:{
                    libros[i].setPrecio(flo);
                }break;
            }
        }
    }
}

void Lista::eliminar(int pos){
    if(pos!=-1){
        for(int i=pos;i<cont;i++){
            libros[i]=libros[i+1];
        }
        cont--;
    }
}

void Lista::ventas(int){
}

int Lista::getCont(){
    return cont;
}

void Lista::inserta10(string n,string a,string e,string isbn,string c,string cs,int ed,float p){
    libros[cont].setNombre(n);
    libros[cont].setAutor(a);
    libros[cont].setEditorial(e);
    libros[cont].setIsbn(isbn);
    for(int i=0;i<cont;i++){
        if(isbn==libros[i].getIsbn()){
            cout<<"El ISBN ya esta en uso"<<endl;
            return;
        }
    }
    libros[cont].setCategoria(c);
    libros[cont].setCategoriaSec(cs);
    libros[cont].setEjemDisp(ed);
    libros[cont].setEjemVend(0);
    libros[cont].setPrecio(p);
    cont++;
}
