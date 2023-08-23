Algoritmo Num
	Leer a,b,c,d
	
	Si a>b Entonces
		x<-a
		a<-b
		b<-x
	Fin Si
	Si b>c Entonces
		x<-b
		b<-c
		c<-x
	Fin Si
	Si c>d Entonces
		x<-c
		c<-d
		d<-x
	Fin Si
	Escribir a,b,c,d
FinAlgoritmo
