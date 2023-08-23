.model
.data 
    X DB 1
    Y DB 80,100,119,135,148,156,160,159,152,142,127,109,90,70,51,33,18,8,1,0,4,12,25,41,60,80,100,119,135,148,156,160,159,152,142,127,109,90,70,51,33,18,8,1,0,4,12,25,41,60,80,100,119,135,148,156,160,159,152,142,127,109,90,70,51,33,18,8,1,0,4,12,25,41,60,80,100,119,135,148,156,160,159,152,142,127,109,90,70,51,33,18,8,1,0,4,12,25,41,60,80,100,119,135,148,156,160,159,152,142,127,109,90,70,51,33,18,8,1,0,4,12,25,41,60,80,100,119,135,148,156,160,159,152,142,127,109,90,70,51,33,18,8,1,0,4,12,25,41,60,80,100,119,135,148,156,160,159,152,142,127,109,90,70,51,33,18,8,1,0,4,12,25,41,60
    COLOR DB 0fh
;------------------------------------------
.code
    mov ax, @DATA
    mov ds, ax
    xor ax, ax
    mov si, 0
    ; establece el modo de video 
    mov ah, 0 
    mov al, 13h     ; 320 x 200 en grafico
    int 10h
    jmp pixel 
    
pixel:
    mov cl,X        ; coordenada en X
    mov dl,Y[si]    ; coordenada en Y
    mov al,COLOR    ; color
    mov ah,0Ch      ; Escribe un punto, DX = Y, CX = X,
    int 10h     
    inc si          ; Incrementa SI
    inc X           ; Incrementa variable X
    cmp X,171d      ; Comprar si X es 171
    jb pixel        ; Si es menor salta a pixel
    mov ah,04ch
    int 21h         ; Terminar programa                              
    end  

