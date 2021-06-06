class ListarEspacios():

    def __init__(self, DB):
        self.DB = DB

    def listar_espacios(self):
        cur = self.DB.cursor(dictionary=True)
        cur.execute('SELECT * FROM espacios')
        espacios = cur.fetchall()
        cur.close()
        return espacios

