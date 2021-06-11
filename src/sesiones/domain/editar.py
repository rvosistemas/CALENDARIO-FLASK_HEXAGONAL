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
            fecha_sesion = sesion['fecha_sesion']
            hora_inicio_sesion = sesion['hora_inicio_sesion']
            hora_fin_sesion = sesion['hora_fin_sesion']
            espacio_id = sesion['espacio_id']

            cur.execute("""
                    UPDATE sesiones
                    SET fecha_sesion = %s,
                        hora_inicio_sesion = %s,
                        hora_fin_sesion = %s,
                        espacio_id = %s
                    WHERE id_sesion = %s
                """, (fecha_sesion, hora_inicio_sesion, hora_fin_sesion, espacio_id, id))
            self.DB.commit()
            print('sesion editada satisfactoriamente')
            return 'editada', 200
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
