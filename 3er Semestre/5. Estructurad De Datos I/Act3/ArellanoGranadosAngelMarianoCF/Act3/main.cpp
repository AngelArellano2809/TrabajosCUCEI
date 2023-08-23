#include <iostream>
using namespace std;

#include "Menu.h"
#include "Lista.h"
#include "Libro.h"

int main(){
    int opc;
    Menu m;
    Lista lista;
    do{
        opc=m.menuPrincipal();
        switch(opc){
            case 1:{//
                lista.inserta();
            }break;
            case 2:{//
                lista.mostrar(lista.buscar());
            }break;
            case 3:{//
                lista.modificar();
            }break;
            case 4:{
                lista.ventas(lista.buscar());
            }break;
            case 5:{//
                for(int i=0;i<lista.getCont();i++){
                    lista.mostrar(i);
                }
            }break;
            case 6:{
                lista.eliminar(lista.buscar());
            }break;
            case 7:{
                lista.inserta10("1984","GeorgeOrwell","Editorial","1A2B","Distopico","Clasico",21,284);
                lista.inserta10("Demian","HermannHesse","Editorial","4G5R","PsicoAnalisis","Clasico",5,86.5);
                lista.inserta10("MazeRunner","JamesDashner","Editorial","8AF2","CienciaFiccion","Suspenso",36,255);
                lista.inserta10("SliverEyes","ScottCawthon","Editorial","7W9B","Terror","Suspenso",12,199);
                lista.inserta10("Metamorfosis","FranzKafka","Editorial","O2T3","Fantasia","Clasico",18,68.5);
                lista.inserta10("PoemarioPoe","Poe","Editorial","L0O4","Recopilacion","Terror",42,85.9);
                lista.inserta10("EnLlamas","SuzanneCollins","Editorial","R8UF","CienciaFiccion","Distopico",54,250);
                lista.inserta10("Wonder","RaquelPalacio","Editorial","SAA7","Emotivo","Drama",46,189);
                lista.inserta10("ArseneLupin","MauriceLeblanc","Editorial","AE98","Misterio","Clasico",24,75.5);
                lista.inserta10("ElPrincipito"," Saint-Exupery","Editorial","NV6D","Infantil","Fantasia",37,109.9);
            }break;
        }
    }while(opc);
    return 0;
}
