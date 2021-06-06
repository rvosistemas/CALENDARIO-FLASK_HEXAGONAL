class ListarSesiones():

    def __init__(self, DB):
        self.DB = DB

    def listar_sesiones(self):
        cur = self.DB.cursor(dictionary=True)
        cur.execute('SELECT * FROM sesiones')
        sesiones = cur.fetchall()
        cur.close()
        cur = self.DB.cursor(dictionary=True)
        cur.execute('SELECT * FROM espacios')
        espacios = cur.fetchall()
        cur.close()
        return sesiones, espacios

