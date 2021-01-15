import sqlite3

class DB():
    
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        cursor = self.con.cursor()
        cursor.execute('Create table if not exists agenda(id text PRIMARY KEY, nombre text, fecha text, tipo text, descripcion text)')
        self.con.commit()
    
    def insert(self, id, fecha, nombre, descripcion, tipo):
        cursor = self.con.cursor()
        sql = f"INSERT INTO agenda VALUES('{id}', '{nombre}', '{fecha}', '{tipo}', '{descripcion}')"
        cursor.execute(sql)
        self.con.commit()
    
    def delete(self, id):
        cursor = self.con.cursor()
        sql = f"DELETE FROM agenda WHERE id = '{id}'"
        cursor.execute(sql)
        self.con.commit()
        
    def update(self, id, fecha, nombre, descripcion, tipo):
        cursor = self.con.cursor()
        sql = 'UPDATE agenda SET fecha=?, nombre=?, descripcion=?, tipo=? WHERE id = ?;'
        datos = (fecha, nombre, descripcion, tipo, id)
        cursor.execute(sql, datos)
        self.con.commit()
    
    def select_all(self):
        cursor = self.con.cursor()
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
    
    def select(self,fecha):
        cursor = self.con.cursor()
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