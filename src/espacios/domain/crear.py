import sys


class CrearEspacio():

    def __init__(self, DB):
        self.DB = DB

    def crear(self, espacio):
        cur = self.DB.cursor()
        try:
            nombre_espacio = espacio['nombre_espacio']
            semestre_espacio = espacio['semestre_espacio']

            cur.execute(
                'INSERT INTO espacios (nombre_espacio, semestre_espacio) VALUES (%s, %s)',
                (nombre_espacio, semestre_espacio))
            self.DB.commit()
            print('espacio agregado satisfactoriamente')
            return 'creado', 201
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
