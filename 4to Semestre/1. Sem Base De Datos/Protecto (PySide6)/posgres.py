import psycopg2
import datetime as dt

hostname = 'localhost'
database = 'MUSEOS_JALISCO'
username = 'postgres'
pwd = 'usuario'
post_id = 5432

def eliMuseo(id:int):
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

def addEncar(id:int,nombre:str,contacto:str,usuario:str,contr:str):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    script = 'INSERT INTO encargados_museo(id_museo, nombre, contacto, nombre_usuario, "contaseña")VALUES (%s, %s, %s, %s, %s)'
    values = (id,nombre,contacto,usuario,contr)
    cur.execute(script,values)
    conn.commit()
    cur.close()
    conn.close()

def addMuseo(id:int,nombre:str,horario:str,ubicacio:str,contacto:str):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    script = 'INSERT INTO museo(id_museo, nombre, horario, ubicacion, contacto)VALUES (%s, %s, %s, %s, %s)'
    values = (id,nombre,horario,ubicacio,contacto)
    cur.execute(script,values)
    conn.commit()
    cur.close()
    conn.close()

def addColPer(id:int,nombre:str,desc:str,tema:str):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    script = 'INSERT INTO colecciones_permanentes(id_museo, nombre, descripcion, tema)VALUES (%s, %s, %s, %s)'
    values = (id,nombre,desc,tema)
    cur.execute(script,values)
    conn.commit()
    cur.close()
    conn.close()

def addColTem(id:int,nombre:str,desc:str,tema:str,ini:str,fin:str):
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    script = 'INSERT INTO public.colecciones_temporales(id_museo,nombre,descripcion,fecha_inicio,fecha_final,tema)VALUES (%s, %s, %s, %s, %s, %s)'
    values = (id,nombre,desc,dt.date(int(ini[0:4]),int(ini[5:7]),int(ini[8:11])),dt.date(int(fin[0:4]),int(fin[5:7]),int(fin[8:11])),tema)
    cur.execute(script,values)
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

def buscarMuseo(nombre:str)->int:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cur.execute('SELECT * FROM museo')
    for museo in cur.fetchall():
        if nombre == museo[1]:
            cur.close()
            conn.close()
            return museo[0]
    cur.close()
    conn.close()
    return None

def actividades_especiales(id_museo:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM actividades')
    for actividad in cur.fetchall():
        if id_museo == actividad[0]:
            cadena += actividad[1] + " : " + actividad[2] + "\n\t" + str(actividad[3]) + "\n"
    cur.close()
    conn.close()
    return cadena

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

def horario(id:int)->str:
    conn = psycopg2.connect(host = hostname,dbname = database,user = username,password = pwd,port = post_id)
    cur = conn.cursor()
    cadena = ""
    cur.execute('SELECT * FROM museo')
    for mus in cur.fetchall():
        if id == mus[0]:
            cadena = "Horario: " + mus[2] + "\n"
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