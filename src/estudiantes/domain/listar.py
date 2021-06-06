class ListarEstudiantes():

    def __init__(self, DB):
        self.DB = DB

    def listar_estudiantes(self):
        cur = self.DB.cursor(dictionary=True)
        cur.execute('SELECT * FROM estudiantes')
        estudiantes = cur.fetchall()
        cur.close()
        return estudiantes

