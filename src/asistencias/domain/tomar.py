import sys


class TomarAsistencias():

    def __init__(self, DB):
        self.DB = DB

    def tomar_asistencias(self):
        cur = self.DB.cursor()
        cur.execute('SELECT * FROM sesiones')
        sesiones = cur.fetchall()
        cur.close()
        cur = self.DB.cursor()
        cur.execute('SELECT * FROM espacios')
        espacios = cur.fetchall()
        cur.close()
        return sesiones, espacios

    def tomar_asistencia(self, asistentes):
        print("#"*50, "asistencia  ->  ", asistentes)
        try:
            sesion_id = asistentes['sesion_id'][0]
            if asistentes.get("estudiante_asistencia"):
                for estudiante_id in asistentes['estudiante_id']:
                    if estudiante_id in asistentes['estudiante_asistencia']:
                        estudiante_asistencia = 1
                        cur = self.DB.cursor()
                        cur.execute('INSERT INTO asistencias (estudiante_id, sesion_id, estudiante_asistencia) VALUES (%s, %s, %s)',
                                    (estudiante_id, sesion_id, estudiante_asistencia))
                        self.DB.commit()
                        print('asistencia agregada satisfactoriamente')
                    else:
                        continue
            return 'creada', 201
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
