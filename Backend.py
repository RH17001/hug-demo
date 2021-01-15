import sqlite3

def init():
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute(
        'Create table if not exists agenda(id text PRIMARY KEY, nombre text, fecha text, tipo text, descripcion text)')
    con.commit()
    return con


def insert(id, fecha, nombre, descripcion, tipo):
    con = init()
    cursor = con.cursor()
    sql = f"INSERT INTO agenda VALUES('{id}', '{nombre}', '{fecha}', '{tipo}', '{descripcion}')"
    cursor.execute(sql)
    con.commit()


def delete(id):
    con = init()
    cursor = con.cursor()
    sql = f"DELETE FROM agenda WHERE id = '{id}'"
    cursor.execute(sql)
    con.commit()


def update(id, fecha, nombre, descripcion, tipo):
    con = init()
    cursor = con.cursor()
    sql = 'UPDATE agenda SET fecha=?, nombre=?, descripcion=?, tipo=? WHERE id = ?;'
    datos = (fecha, nombre, descripcion, tipo, id)
    cursor.execute(sql, datos)
    con.commit()


def select_all():
    con = init()
    cursor = con.cursor()
    sql = f"SELECT * FROM agenda"
    cursor.execute(sql)
    lista = []
    for i in cursor.fetchall():
        lista.append({
            'id': i[0],
            'nombre': i[1],
            'fecha': i[2],
            'tipo': i[3],
            'descripcion': i[4],
        })
    return lista


def select(fecha):
    con = init()
    cursor = con.cursor()
    sql = f"SELECT * FROM agenda WHERE fecha = '{fecha}'"
    cursor.execute(sql)
    lista = []
    for i in cursor.fetchall():
        lista.append({
            'id': i[0],
            'nombre': i[1],
            'fecha': i[2],
            'tipo': i[3],
            'descripcion': i[4],
        })
    return lista