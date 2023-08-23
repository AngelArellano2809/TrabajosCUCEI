.model .stack
.data
un db 0
de db 0
ce db 0
num1 db 0
num2 db 0
msg1 db 10,13,17,'Ingrese el numero 1:','$' 
msg2 db 10,13,17,'Ingrese el numero 2:','$'
res db 10,13,17,'Resultado:','$'     

.code 
;obtencion de datos
mov ax,data
mov ds,ax  ;Se inicia en segmento de datos
mov ah,09h
lea dx,msg1;Muestra mensaje 1    
int 21h 
mov ah,01h ;Introdusco las decenas num 1
int 21h
sub al,30h ;Se cambia de ASCII a dec
mov de,al 
mov ah,01h ;Introdusco las unidades num 1
int 21h
sub al,30h ;Se cambia de ASCII a dec
mov un,al  
mov al,de
mov bl,10
mul bl     ; al = de * 10
add al,un   ; al = de * 10 + un
mov num1,al;se obtiene el primer numero
mov ah,09h
lea dx,msg2;Muestra mensaje 2    
int 21h 
mov ah,01h ;Introdusco las decenas num 2
int 21h
sub al,30h ;Se cambia de ASCII a dec
mov de,al 
mov ah,01h ;Introdusco las unidades num 2
int 21h
sub al,30h ;Se cambia de ASCII a dec
mov un,al  
mov al,de
mov bl,10
mul bl     ; al = de * 10
add al,un  ; al = de * 10 + un
mov num2,al;se obtiene el segundo numero
                                        
;Sumador  
xor ax,ax  ;lipiamos registros
xor bx,bx  
mov al,num1
mov bl,num2
add al,bl  ;Se suman los numeros

;impresion en 3 caracteres
aam 
mov un,al  ;respaldo unidades
mov al,ah
aam
mov de,al  ;respaldo decenas
mov ce,ah  ;respaldo centenas
mov ah,09h
lea dx,msg1;Muestra mensaje 1    
int 21h
mov ah,02h
mov dl,ce
add dl,30h ;cambio de dec a ascii
int 21h
mov dl,de
add dl,30h ;cambio de dec a ascii
int 21h
mov dl,un
add dl,30h ;cambio de dec a ascii
int 21h 

;Termina programa
mov ah,04ch
int 21h                                       
end