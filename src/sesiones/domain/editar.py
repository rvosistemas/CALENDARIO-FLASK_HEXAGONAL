import sys


class EditarSesion():

    def __init__(self, DB):
        self.DB = DB

    def obtener(self, id):
        cur = self.DB.cursor()
        cur.execute(f"SELECT * FROM sesiones WHERE id_sesion = {id}")
        sesion = cur.fetchall()
        cur = self.DB.cursor()
        cur.execute('SELECT * FROM espacios')
        espacios = cur.fetchall()
        cur.close()
        print('sesion obtenida satisfactoriamente')
        return sesion[0], espacios

    def editar(self, id, sesion):
        cur = self.DB.cursor()
        try:
            fecha_asistencia = sesion['fecha_asistencia']
            hora_inicio_asistencia = sesion['hora_inicio_asistencia']
            hora_fin_asistencia = sesion['hora_fin_asistencia']
            sesion_id = sesion['sesion_id']

            cur.execute("""
                    UPDATE sesions
                    SET fecha_asistencia = %s,
                        hora_inicio_asistencia = %s,
                        hora_fin_asistencia = %s,
                        sesion_id = %s,
                    WHERE id_sesion = %s
                """, (fecha_asistencia, hora_inicio_asistencia, hora_fin_asistencia, sesion_id, id))
            self.DB.commit()
            print('sesion editada satisfactoriamente')
            return 'editada', 200
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
