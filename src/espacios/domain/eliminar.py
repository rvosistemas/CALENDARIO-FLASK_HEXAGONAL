import sys


class EliminarEspacio():

    def __init__(self, DB):
        self.DB = DB

    def eliminar(self, id):
        cur = self.DB.cursor()
        try:
            cur.execute(f"DELETE FROM espacios WHERE id_espacio = {id}")
            self.DB.commit()
            print('espacio eliminado satisfactoriamente')
            return 'eliminado', 200
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500