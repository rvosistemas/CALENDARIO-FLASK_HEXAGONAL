import sys


class CrearSesion():

    def __init__(self, DB):
        self.DB = DB

    def crear(self, sesion):
        cur = self.DB.cursor()
        try:
            fecha_asistencia = sesion['fecha_asistencia']
            hora_inicio_asistencia = sesion['hora_inicio_asistencia']
            hora_fin_asistencia = sesion['hora_fin_asistencia']
            espacio_id = sesion['espacio_id']

            cur.execute(
                'INSERT INTO sesions (fecha_asistencia, hora_inicio_asistencia, hora_fin_asistencia, espacio_id) VALUES (%s, %s, %s, %s)',
                (fecha_asistencia, hora_inicio_asistencia, hora_fin_asistencia, espacio_id))
            self.DB.commit()
            print('sesion agregada satisfactoriamente')
            return 'creada', 201
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
