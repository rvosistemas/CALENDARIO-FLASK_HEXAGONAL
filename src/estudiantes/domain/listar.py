class ListarEstudiantes():

    def __init__(self, DB):
        self.DB = DB

    def run(self):
        cur = self.DB.cursor(dictionary=True)
        cur.execute('SELECT * FROM estudiantes')
        estudiantes = cur.fetchall()
        cur.close()
        print("estudiantes   -->  ", estudiantes)
        return estudiantes

