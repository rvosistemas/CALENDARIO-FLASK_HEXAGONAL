import sys


class EliminarEstudiante():

    def __init__(self, DB):
        self.DB = DB

    def eliminar(self, id):
        cur = self.DB.cursor()
        try:
            cur.execute(f"DELETE FROM estudiantes WHERE id_estudiante = {id}")
            self.DB.commit()
            print('estudiante eliminado satisfactoriamente')
            return 'eliminado', 200
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500