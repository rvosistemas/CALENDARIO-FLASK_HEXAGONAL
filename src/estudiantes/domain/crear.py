import sys


class CrearEstudiante():

    def __init__(self, DB):
        self.DB = DB

    def crear(self, estudiante):
        cur = self.DB.cursor()
        try:
            identificacion_estudiante = estudiante['identificacion_estudiante']
            nombres_estudiante = estudiante['nombres_estudiante']
            apellidos_estudiante = estudiante['apellidos_estudiante']
            telefono_estudiante = estudiante['telefono_estudiante']
            email_estudiante = estudiante['email_estudiante']
            semestre_estudiante = estudiante['semestre_estudiante']

            cur.execute(
                'INSERT INTO estudiantes (identificacion_estudiante, nombres_estudiante, apellidos_estudiante, telefono_estudiante, email_estudiante, semestre_estudiante) VALUES (%s, %s, %s, %s, %s, %s)',
                (identificacion_estudiante, nombres_estudiante, apellidos_estudiante, telefono_estudiante, email_estudiante, semestre_estudiante))
            self.DB.commit()
            print('estudiante agregado satisfactoriamente')
            return 'creado', 201
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
