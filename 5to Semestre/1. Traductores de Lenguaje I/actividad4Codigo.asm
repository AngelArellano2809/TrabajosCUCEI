.model
.data 
directorio db "c:\prueba1", 0 ;ascii del nombre del directorio nuevo 
directori1 db "c:\", 0         ;ascii del nombre deldirectorio original    
archivo    db "c:\prueba1\prueba.txt", 0 ;ascii del nombre del archivo
handle     dw ?
cadena     db "Traductores de lenguaje I",0   ;cadena a escribir
;------------------------------------------
.code
mov ax, @DATA
mov ds, ax
xor ax, ax 
;Creacion de direcctorio
mov dx, offset directorio ;offset lugar de memoria donde esta la variable
mov ah, 39h               ;crea directorio 
int 21h
;Entrar al directorio
mov dx, offset directorio ;offset lugar de memoria donde esta la variable
mov ah, 3Bh               ;cambio de directorio 
int 21h  
;Crear un archivo dentro
mov cx, 00h            ;modo de creacion normal
mov dx, offset archivo ;offset lugar de memoria donde esta la variable
mov ah, 3Ch            ;Crea archivo
int 21h
mov handle, ax         ;guaramos el handle 
;Escribir en el archivo
mov bx, handle         ;colocamos el handle
mov cx, 25             ;numero de bytes a escribir
mov dx, offset cadena  ;offset lugar de memoria donde esta la variable
mov ah, 40h            ;escribir en archivo
int 21h 
;Cerrar archivo
mov ah, 3Eh            ;cerrar archivo
mov bx, handle         ;colocamos el handle
int 21h  
;Borrar archivo 
mov dx, offset archivo ;offset lugar de memoria donde esta la variable
mov ah, 41h            ;Borra archivo
int 21h
;Salir del directorio
mov dx, offset directori1 ;offset lugar de memoria donde esta la variable
mov ah, 3Bh               ;cambio de directorio 
int 21h 
;Borrar directorio
mov dx, offset directorio ;offset lugar de memoria donde esta la variable
mov ah, 3AH               ;borra directorio 
int 21h
;Termina programa
mov ah,04ch
int 21h                                       
end