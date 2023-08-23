import psycopg2
#import datetime as dt

hostname = 'localhost'
database = 'MESSENGERS'
username = 'postgres'
pwd = 'usuario'
post_id = 5432

def buscarArtista(nombre:str)->int:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cur.execute('SELECT * FROM artista')
    for artista in cur.fetchall():
        if nombre == artista[1]:
            cur.close()
            conn.close()
            return artista[0]
    cur.close()
    conn.close()
    return None

#funcion que obtiene de la base de datos el nombre, area y genero del artista
def infoArtista(id_artista:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM artista')
    for artista in cur.fetchall():
        if id_artista == artista[0]:
            cadena += artista[1] + "\n" + artista[2] + "\n" + artista[3] 
    cur.close()
    conn.close()
    return cadena

#funcion que obtiene de la base de datos la ubicacion del artista
def ubicacion(id_artista:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM artista')
    for artista in cur.fetchall():
        if id_artista == artista[0]:
            cadena = artista[4]
    cur.close()
    conn.close()
    return cadena

#funcion que obtiene de la base de datos el numero de seguidores del artista
def seguidores(id_artista:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM artista')
    for artista in cur.fetchall():
        if id_artista == artista[0]:
            cadena = human_format(artista[5])
    cur.close()
    conn.close()
    return cadena

#funcion que obtiene de la base de datos URL de la imagen de encima del perfil del artista
def topImagen(id_artista:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM artista')
    for artista in cur.fetchall():
        if id_artista == artista[0]:
            cadena = artista[6]
    cur.close()
    conn.close()
    return cadena

#funcion que obtiene de la base de datos URL de la imagen de Perfil del artista
def perfilImagen(id_artista:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM artista')
    for artista in cur.fetchall():
        if id_artista == artista[0]:
            cadena = artista[7]
    cur.close()
    conn.close()
    return cadena

#funcion que busca si un usuario existe y si conincide su contraseña regresa una dupla con el id y que tipo de usuario es
def acceso(usuario:str,pw:str):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    log_dup = (0,' ')
    cur.execute('SELECT * FROM artista')
    for artista in cur.fetchall():
        if usuario == artista[10]:
            if pw == artista[11]:
                log_dup = (artista[0],'A')
                break
            log_dup = (artista[0],' ')
    cur.execute('SELECT * FROM aficionado')
    for aficionado in cur.fetchall():
        if usuario == aficionado[1]:
            if pw == aficionado[2]:
                log_dup = (aficionado[0],'F')
                break
            log_dup = (aficionado[0],' ')  
    cur.execute('SELECT * FROM negocio')
    for negocio in cur.fetchall():
        if usuario == negocio[2]:
            if pw == negocio[3]:
                log_dup = (negocio[0],'N')
                break
            log_dup = (negocio[0],' ') 
    cur.close()
    conn.close()
    return log_dup

#funcion que inserta un nuevo registro en la tabla aficionado
def regFan(nombre,passw,pref):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    script = 'INSERT INTO aficionado(id_aficionado, nombre, "contraseña", preferencia, seguidos)VALUES (default, %s, %s, %s, default)'
    values = (nombre,passw,pref)
    cur.execute(script,values)
    conn.commit()
    cur.close()
    conn.close()
    return True

#funcion que inserta un nuevo registro en la tabla artista
def regArt(nombre,area,genero,estado,usuario,passw):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    script = 'INSERT INTO artista(id_artista, nombre, area, genero, ubicacion, seguidores, imagen_top, imagen_profile, peso_general, peso_semanal, usuario, "contreseña", seguidos) VALUES (default, %s, %s, %s, %s, default, default, default, default, default, %s, %s, default)'
    values = (nombre,area,genero,estado,usuario,passw)
    cur.execute(script,values)
    conn.commit()
    cur.close()
    conn.close()
    return True

#funcion que inserta un nuevo registro en la tabla negocio
def regNeg(nombre,usuario,passw,contacto,pref,direcion):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    script = 'INSERT INTO negocio(id_negocio, nombre_negocio, nombre_encargado, "contraseña", contacto, preferencia, direccion, seguidos) VALUES (default, %s, %s, %s, %s, %s, %s, default)'
    values = (nombre,usuario,passw,contacto,pref,direcion)
    cur.execute(script,values)
    conn.commit()
    cur.close()
    conn.close()
    return True

#funcion que regresa la informacion de una publicacion segun un indice
def infoPublicacion(id_artista:int):
    x = 0
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    info = [['','','',''],['','','',''],['','','',''],['','','',''],['','','','']]
    cur.execute('SELECT * FROM publicacion')
    for publicacion in cur.fetchall():
        if id_artista == publicacion[0]:
            info[x][0] = publicacion[1]
            info[x][1] = publicacion[2]
            info[x][2] = publicacion[3]
            info[x][3] = publicacion[4]
            x += 1
        
    cur.close()
    conn.close()
    return info

#funcion que retorna el id de un resgistro
def getId(nombre):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = 0
    cur.execute('SELECT * FROM artista')
    for artista in cur.fetchall():
        if nombre == artista[10]:
            cadena = artista[0]
            break
    cur.execute('SELECT * FROM aficionado')
    for aficionado in cur.fetchall():
        if nombre == aficionado[1]:
            cadena = aficionado[0]
            break
    cur.execute('SELECT * FROM negocio')
    for negocio in cur.fetchall():
        if nombre == negocio[2]:
            cadena = negocio[0]
            break
    cur.close()
    conn.close()
    return cadena

def addPeso(id_artista:int):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    script = 'UPDATE artista SET peso_general = peso_general + 1 WHERE (id_artista = %s)'
    values = ([id_artista])
    cur.execute(script,values)
    script = 'UPDATE artista SET peso_semanal = peso_semanal + 1 WHERE (id_artista = %s)'
    values = ([id_artista])
    cur.execute(script,values)
    conn.commit()
    cur.close()
    conn.close()

#funcion que regresa la informacion de los 5 artistas con mas perso segun la preferencia del usuario
def recomedacionGneral(pref):
    x = 0
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    info = [['',''],['',''],['',''],['',''],['',''],['',''],['','']]
    script = 'SELECT nombre as nom,id_artista as id_art FROM artista WHERE (area = %s) ORDER BY peso_general DESC LIMIT 7'
    values = ([pref])
    cur.execute(script,values)
    for reg in cur.fetchall():
        info[x][0] = reg[0]
        info[x][1] = reg[1]
        x += 1
        
    cur.close()
    conn.close()
    return info

#funcion que retorna el id de un resgistro
def getPref(id,tipo):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = 0
    if tipo=='A':
        cur.execute('SELECT * FROM artista')
        for artista in cur.fetchall():
            if id == artista[0]:
                cadena = artista[2]
                break
    elif tipo=='F':
        cur.execute('SELECT * FROM aficionado')
        for aficionado in cur.fetchall():
            if id == aficionado[0]:
                cadena = aficionado[3]
                break
    elif tipo=='N':
        cur.execute('SELECT * FROM negocio')
        for negocio in cur.fetchall():
            if id == negocio[0]:
                cadena = negocio[5]
                break
    cur.close()
    conn.close()
    return cadena
    

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])


"""def eliMuseo(id:int):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    value = (id,)
    script1 = 'DELETE FROM encargados_museo WHERE id_museo =  %s'
    cur.execute(script1,value)
    script2 = 'DELETE FROM colecciones_temporales WHERE id_museo =  %s'
    cur.execute(script2,value)
    script3 = 'DELETE FROM colecciones_permanentes WHERE id_museo =  %s'
    cur.execute(script3,value)
    script4 = 'DELETE FROM accesibilidad WHERE id_museo =  %s'
    cur.execute(script4,value)
    script5 = 'DELETE FROM actividades WHERE id_museo =  %s'
    cur.execute(script5,value)
    script6 = 'DELETE FROM museo WHERE id_museo =  %s'
    cur.execute(script6,value)
    conn.commit()
    cur.close()
    conn.close()

def eliminarColTem(nombre:str):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    script = 'DELETE FROM colecciones_temporales WHERE nombre = %s'
    values = (nombre,)
    cur.execute(script,values)
    conn.commit()
    cur.close()
    conn.close()

def modificar_datos_museo(id:int,nombre:str,horario:str,ubicacio:str,contacto:str):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    if nombre != '':
        script = 'UPDATE museo SET nombre = %s WHERE id_museo = %s'
        values = (nombre,id)
        cur.execute(script,values)
    if horario != '':
        script = 'UPDATE museo SET horario = %s WHERE id_museo = %s'
        values = (horario,id)
        cur.execute(script,values)
    if ubicacio != '':
        script = 'UPDATE museo SET ubicacion = %s WHERE id_museo = %s'
        values = (ubicacio,id)
        cur.execute(script,values)
    if contacto != '':
        script = 'UPDATE museo SET contacto = %s WHERE id_museo = %s'
        values = (contacto,id)
        cur.execute(script,values)
    conn.commit()
    cur.close()
    conn.close()

def login(un:str, pw:str)->list:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    tipo = []
    cur = conn.cursor()
    cur.execute('SELECT * FROM administrador_bd')
    for admin in cur.fetchall():
        if un == admin[2] and pw == admin[3]:
            tipo.append('ADMIN')
            cur.close()
            conn.close()
            return tipo
    cur.execute('SELECT * FROM encargados_museo')
    for encar in cur.fetchall():
        if un == encar[3] and pw == encar[4]:
            tipo.append('ENCAR')
            tipo.append(encar[0])
            cur.close()
            conn.close()
            return tipo
    cur.close()
    conn.close()
    return None

def accesivilidad(id:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM accesibilidad')
    for acc in cur.fetchall():
        if id == acc[0]:
            if acc[1] == True:
                cadena = "No hay accesivilidad disponibles"
            else:
                cadena = "Auditiva: " + str(int(acc[2])) + "\n" + \
                        "Motriz: " + str(int(acc[3])) + "\n" + \
                        "Cognitiva: " + str(int(acc[4])) + "\n" \
                        "Visual: " + str(int(acc[5])) + "\n" \
                        "Otra: " + acc[7] + "\n" 
    cur.close()
    conn.close()
    return cadena

def descripcion(id:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM museo')
    for mus in cur.fetchall():
        if id == mus[0]:
            cadena = "Nombre: " + mus[1] + "\n" + \
                "Ubicacion: " + mus[3] + "\n" + \
                "Contacto: " + mus [4] +"\n"
    cur.close()
    conn.close()
    return cadena
    
def colPer(id:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM colecciones_permanentes')
    for col in cur.fetchall():
        if id == col[0]:
            cadena += col[1] + " : " + col[2] + "\n\t" + col[3] + "\n"
    cur.close()
    conn.close()
    return cadena

def colTem(id:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM colecciones_temporales')
    for col in cur.fetchall():
        if id == col[0]:
            cadena += col[1] + " : " + col[2] + "\n" + str(col[3]) + " a " + str(col[4]) + "\n\t" + col[5] + "\n"
    cur.close()
    conn.close()
    return cadena

def musRelevantes()->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM museo')
    for mus in cur.fetchall():
        cadena += "ID: " + str(mus[0]) + "\n" + \
                "Nombre: " + mus[1] + "\n" + \
                "Ubicacion: " + mus[3] + "\n" + \
                "Contacto: " + mus [4] +"\n\n"
    cur.close()
    conn.close()
    return cadena
    """