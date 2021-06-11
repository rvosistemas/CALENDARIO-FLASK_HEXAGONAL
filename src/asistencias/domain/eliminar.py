import sys


class EliminarListaAsistencia():

    def __init__(self, DB):
        self.DB = DB

    def eliminar(self, sesion_id):
        cur = self.DB.cursor()
        try:
            cur.execute(
                f"DELETE FROM asistencias WHERE sesion_id = {sesion_id}")
            self.DB.commit()
            print('asistencia eliminada satisfactoriamente')
            return 'eliminada', 200
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
