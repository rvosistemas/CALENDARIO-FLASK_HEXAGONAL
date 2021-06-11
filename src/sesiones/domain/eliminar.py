import sys


class EliminarSesion():

    def __init__(self, DB):
        self.DB = DB

    def eliminar(self, id):
        cur = self.DB.cursor()
        try:
            cur.execute(f"DELETE FROM sesiones WHERE id_sesion = {id}")
            self.DB.commit()
            print('sesion eliminada satisfactoriamente')
            return 'eliminada', 200
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500