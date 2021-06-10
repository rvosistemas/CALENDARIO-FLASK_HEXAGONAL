class CargarEstudiantesAsistencia():

    def __init__(self, DB):
        self.DB = DB

    def cargar(self, id_sesion):
        cur = self.DB.cursor()
        cur.execute('SELECT * FROM sesiones')
        sesiones = cur.fetchall()
        cur.execute('SELECT * FROM espacios')
        espacios = cur.fetchall()
        cur.execute(
            f"SELECT sesion_id FROM asistencias AS a INNER JOIN sesiones AS s ON a.sesion_id = s.id_sesion WHERE s.id_sesion = {id_sesion}")
        sesion_realizada = cur.fetchall()

        if sesion_realizada:
            print('La sesion que desea cargar ya existe')
            cur.close()
            result = {
                'sesiones': sesiones,
                'espacios': espacios,
            }
            return result
        else:
            cur.execute(
                f"SELECT nombre_espacio FROM espacios AS e INNER JOIN sesiones AS s ON e.id_espacio = s.espacio_id WHERE s.id_sesion = {id_sesion}")
            nombre_espacio = cur.fetchall()
            cur.execute(
                f"SELECT semestre_espacio FROM espacios AS e INNER JOIN sesiones AS s ON e.id_espacio = s.espacio_id WHERE s.id_sesion = {id_sesion}")
            semestre_espacio = cur.fetchall()[0]
            cur.execute(
                f"SELECT * FROM estudiantes WHERE semestre_estudiante = {semestre_espacio[0]}")
            estudiantes = cur.fetchall()
            cur.close()
            if estudiantes == ():
                print('No hay estudiantes en el semestre del espacio academico')
            result = {
                'sesiones': sesiones,
                'espacios': espacios,
                'estudiantes': estudiantes,
                'id_sesion': id_sesion,
                'nombre_espacio': nombre_espacio,
            }
            return result
