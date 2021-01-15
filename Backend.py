import sqlite3

def init():
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute(
        'Create table if not exists agenda(id text PRIMARY KEY, name text, date text, type text, description text)')
    con.commit()
    return con

def insert(id, date, name, description, type):
    con = init()
    cursor = con.cursor()
    sql = f"INSERT INTO agenda VALUES('{id}', '{name}', '{date}', '{type}', '{description}')"
    cursor.execute(sql)
    con.commit()

def delete(id):
    con = init()
    cursor = con.cursor()
    sql = f"DELETE FROM agenda WHERE id = '{id}'"
    cursor.execute(sql)
    con.commit()


def update(id, date, name, description, type):
    con = init()
    cursor = con.cursor()
    sql = 'UPDATE agenda SET date=?, name=?, description=?, type=? WHERE id = ?;'
    datos = (date, name, description, type, id)
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
            'name': i[1],
            'date': i[2],
            'type': i[3],
            'description': i[4],
        })
    return lista

def select(date):
    con = init()
    cursor = con.cursor()
    sql = f"SELECT * FROM agenda WHERE date = '{date}'"
    cursor.execute(sql)
    lista = []
    for i in cursor.fetchall():
        lista.append({
            'id': i[0],
            'name': i[1],
            'date': i[2],
            'type': i[3],
            'description': i[4],
        })
    return lista