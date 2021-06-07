class ListarAsistencias():

    def __init__(self, DB):
        self.DB = DB

    def listar_asistencias(self):
        cur = self.DB.cursor()
        cur.execute('SELECT * FROM sesiones')
        sesiones = cur.fetchall()
        cur.close()
        cur = self.DB.cursor()
        cur.execute('SELECT * FROM espacios')
        espacios = cur.fetchall()
        cur.close()
        return sesiones, espacios

    def listar_estudiantes(self, sesion_id):
        cur = self.DB.cursor()
        cur.execute('SELECT * FROM sesiones')
        sesiones = cur.fetchall()
        cur.execute('SELECT * FROM espacios')
        espacios = cur.fetchall()
        cur.execute(
            f"SELECT estudiante_id FROM asistencias WHERE asistencia_id = {sesion_id}")
        estudiantes_ids = cur.fetchall()
        lista_estudiantes = []
        for estudiante_id in estudiantes_ids:
            cur.execute(
                f"SELECT * FROM estudiantes WHERE id_estudiante = {estudiante_id[0]}")
            estudiante = cur.fetchall()
            lista_estudiantes.append(estudiante[0])
        if lista_estudiantes == []:
            print('La lista no tiene estudiantes')
        cur.close()
        return sesiones, espacios, lista_estudiantes, sesion_id
