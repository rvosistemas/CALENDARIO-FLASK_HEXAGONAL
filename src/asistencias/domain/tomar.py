import sys


class TomarAsistencias():

    def __init__(self, DB):
        self.DB = DB

    def tomar_sesiones(self):
        cur = self.DB.cursor()
        cur.execute('SELECT * FROM sesiones')
        sesiones = cur.fetchall()
        cur.close()
        cur = self.DB.cursor()
        cur.execute('SELECT * FROM espacios')
        espacios = cur.fetchall()
        cur.close()
        return sesiones, espacios

    def tomar_asistencias(self, asistencia):
        cur = self.DB.cursor()
        try:            
            estudiante_id = asistencia['estudiante_id']
            asistencia_id = asistencia['asistencia_id']
            estudiante_asistencia = asistencia['estudiante_asistencia']

            cur.execute('INSERT INTO asistencias_estudiantes (estudiante_id, asistencia_id, estudiante_asistencia) VALUES (%s, %s, %s)',
                        (estudiante_id, asistencia_id, estudiante_asistencia))
            self.DB.commit()
            print('asistencia agregada satisfactoriamente')
            return 'creada', 201
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
