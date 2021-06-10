import sys


class CrearSesion():

    def __init__(self, DB):
        self.DB = DB

    def crear(self, sesion):
        cur = self.DB.cursor()
        try:
            fecha_sesion = sesion['fecha_sesion']
            hora_inicio_sesion = sesion['hora_inicio_sesion']
            hora_fin_sesion = sesion['hora_fin_sesion']
            espacio_id = sesion['espacio_id']

            cur.execute(
                'INSERT INTO sesiones (fecha_sesion, hora_inicio_sesion, hora_fin_sesion, espacio_id) VALUES (%s, %s, %s, %s)',
                (fecha_sesion, hora_inicio_sesion, hora_fin_sesion, espacio_id))
            self.DB.commit()
            print('sesion agregada satisfactoriamente')
            return 'creada', 201
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
