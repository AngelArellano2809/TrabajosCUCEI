.model .stack
.data 
menu1 db 09,10,13,'Calculadora resultados: 0>X>255','$'
opc0  db 10,13,'0.- Salir','$'
opc1  db 10,13,'1.- Suma','$'
opc2  db 10,13,'2.- Resta','$'
opc3  db 10,13,'3.- Multiplicacion','$'
opc4  db 10,13,'4.- Division','$' 
opc5  db 10,13,'5.- Potencia','$'
opc6  db 10,13,'6.- Grafica Seno','$'
opc7  db 10,13,'7.- Grafica Coseno','$'
menu2 db 10,13,17,'Selecciona una opcion:','$'
opc   db 0

un db 0
de db 0
ce db 0
num1 db 0
num2 db 0 
msg1 db 10,13,17,'Ingrese el numero 1:','$' 
msg2 db 10,13,17,'Ingrese el numero 2:','$'
res db 10,13,17,'Resultado:','$'

SenX DB 1
SenY DB 80,100,119,135,148,156,160,159,152,142,127,109,90,70,51,33,18,8,1,0,4,12,25,41,60    
COLOR DB 0fh

CosX DB 1
CosY DB 160,157,150,138,123,105,85,65,46,29,15,6,1,1,6,15,29,46,65,85,105,123,138,150,157
 

.code
    mov ax,data
    mov ds,ax  ;Se inicia en segmento de datos
;Menu--------------------------------------------------------
Menu:
    mov un,0
    mov de,0
    mov ce,0
    mov num1,0
    mov num2,0
    mov ax,03h
    int 10h
    mov ah,09h
    lea dx,menu1;Muestra linea de apoyo   
    int 21h
    lea dx,opc0;Muestra opcion 0    
    int 21h 
    lea dx,opc1;Muestra opcion 1    
    int 21h 
    lea dx,opc2;Muestra opcion 2    
    int 21h 
    lea dx,opc3;Muestra opcion 3    
    int 21h     
    lea dx,opc4;Muestra opcion 4    
    int 21h
    lea dx,opc5;Muestra opcion 5    
    int 21h
    lea dx,opc6;Muestra opcion 6    
    int 21h
    lea dx,opc7;Muestra opcion 7    
    int 21h
    lea dx,menu2;Muestra linea de apoyo    
    int 21h
    mov ah,01h ;Se recibe la opccion selccionada 
    int 21h
    sub al,30h ;Se cambia de ASCII a dec
    mov opc,al
    cmp opc,0d
    je Salir
    cmp opc,1d
    je Sum
    cmp opc,2d
    je Rest
    cmp opc,3d
    je Mult
    cmp opc,4d
    je Divi
    cmp opc,5d
    je Pot
    cmp opc,6d
    je Sen
    cmp opc,7d
    je Cos
    cmp opc,7d
    jg Menu    
;Suma--------------------------------------------------------- 
Sum:
    mov ax,03h
    int 10h
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
    lea dx,res;Muestra mensaje 1    
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
    mov ah,08h
    int 21h
    jmp Menu
`
;Resta-------------------------------------------------------- 
Rest:
    mov ax,03h
    int 10h
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
                                            
    ;Restador  
    xor ax,ax  ;lipiamos registros
    xor bx,bx  
    mov al,num1
    mov bl,num2
    sub al,bl  ;Se restan los numeros
    
    ;impresion en 2 caracteres
    aam 
    mov un,al  ;respaldo unidades
    mov al,ah
    aam
    mov de,al  ;respaldo decenas
    mov ah,09h
    lea dx,res;Muestra mensaje 1    
    int 21h
    mov ah,02h
    mov dl,de
    add dl,30h ;cambio de dec a ascii
    int 21h
    mov dl,un
    add dl,30h ;cambio de dec a ascii
    int 21h
    mov ah,08h
    int 21h
    jmp Menu
;Multiplicacion-----------------------------------------------
mult: 
    mov ax,03h
    int 10h
    mov ah,09h
    lea dx,msg1;Muestra mensaje 1    
    int 21h  
    mov ah,01h ;Introdusco las unidades num 1
    int 21h
    sub al,30h ;Se cambia de ASCII a dec
    mov un,al  
    mov num1,al;se obtiene el primer numero
    mov ah,09h
    lea dx,msg2;Muestra mensaje 2    
    int 21h  
    mov ah,01h ;Introdusco las unidades num 2
    int 21h
    sub al,30h ;Se cambia de ASCII a dec
    mov un,al  
    mov num2,al;se obtiene el segundo numero
                                            
    ;Multiplicador  
    xor ax,ax  ;lipiamos registros
    xor bx,bx  
    mov al,num1
    mov bl,num2
    mul bl      ;Se multiplican los numeros
    
    ;impresion en 2 caracteres
    aam 
    mov un,al  ;respaldo unidades
    mov al,ah
    aam
    mov de,al  ;respaldo decenas
    mov ah,09h
    lea dx,res;Muestra mensaje 1    
    int 21h
    mov ah,02h
    mov dl,de
    add dl,30h ;cambio de dec a ascii
    int 21h
    mov dl,un
    add dl,30h ;cambio de dec a ascii
    int 21h
    mov ah,08h
    int 21h
    jmp Menu
;Division--------------------------------------------------------- 
Divi:
    mov ax,03h
    int 10h
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
    
    ;Divisor  
    xor ax,ax  ;lipiamos registros
    xor bx,bx  
    mov al,num1
    mov bl,num2
    div bl      ;Se multiplican los numeros
    
    ;impresion en 2 caracteres
    aam 
    mov un,al  ;respaldo unidades
    mov al,ah
    aam
    mov de,al  ;respaldo decenas
    mov ah,09h
    lea dx,res;Muestra mensaje 1    
    int 21h
    mov ah,02h
    mov dl,de
    add dl,30h ;cambio de dec a ascii
    int 21h
    mov dl,un
    add dl,30h ;cambio de dec a ascii
    int 21h
    mov ah,08h
    int 21h
    jmp Menu
;Potencia--------------------------------------------------------- 
Pot:
    mov ax,03h
    int 10h
    mov ah,09h
    lea dx,msg1;Muestra mensaje 1    
    int 21h  
    mov ah,01h ;Introdusco las unidades num 1
    int 21h
    sub al,30h ;Se cambia de ASCII a dec
    mov un,al  
    mov num1,al;se obtiene el primer numero
    mov ah,09h
    lea dx,msg2;Muestra mensaje 2    
    int 21h  
    mov ah,01h ;Introdusco las unidades num 2
    int 21h
    sub al,30h ;Se cambia de ASCII a dec
    mov un,al  
    mov num2,al;se obtiene el segundo numero
                                            
    ;Potenciador  
    xor ax,ax  ;lipiamos registros
    xor bx,bx
    xor cx,cx  
    mov al,num1
    mov bl,num1
    mov cl,num2
    dec cl
bucle:
    mul bl      ;Se multiplican los numeros
    loop bucle
    
    ;impresion en 3 caracteres
    aam 
    mov un,al  ;respaldo unidades
    mov al,ah
    aam
    mov de,al  ;respaldo decenas
    mov ce,ah  ;respaldo centenas
    mov ah,09h
    lea dx,res;Muestra mensaje 1    
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
    mov ah,08h
    int 21h
    jmp Menu
;Seno--------------------------------------------------------- 
Sen:
    mov bl,7
    mov si,0
    mov SenX,1
    ; establece el modo de video 
    mov ah,0 
    mov al,13h     ; 320 x 200 en grafico
    int 10h
    jmp pixelS     
    pixelS:
        mov cl,SenX        ; coordenada en X
        mov dl,SenY[si]    ; coordenada en Y
        mov al,COLOR    ; color
        mov ah,0Ch      ; Escribe un punto, DX = Y, CX = X,
        int 10h     
        inc si          ; Incrementa SI
        inc SenX           ; Incrementa variable X
        cmp si,25d      ; Comprar si X es 171
        jb pixelS        ; Si es menor salta a pixel 
    mov si,0
    dec bl
    cmp bl,00d
    jne pixelS
    mov ah,08h
    int 21h
    jmp Menu
;Coseno--------------------------------------------------------- 
Cos:  
    mov bl,7
    mov si,0
    mov CosX,1
    ; establece el modo de video 
    mov ah,0 
    mov al,13h     ; 320 x 200 en grafico
    int 10h
    jmp pixelC     
    pixelC:
        mov cl,CosX        ; coordenada en X
        mov dl,CosY[si]    ; coordenada en Y
        mov al,COLOR    ; color
        mov ah,0Ch      ; Escribe un punto, DX = Y, CX = X,
        int 10h     
        inc si          ; Incrementa SI
        inc CosX           ; Incrementa variable X
        cmp si,25d      ; Comprar si X es 171
        jb pixelC        ; Si es menor salta a pixel 
    mov si,0
    dec bl
    cmp bl,00d
    jne pixelC
    mov ah,08h
    int 21h
    jmp Menu
;Termina programa------------------------------------------------
Salir:
    mov ah,04ch
    int 21h                                       
    end