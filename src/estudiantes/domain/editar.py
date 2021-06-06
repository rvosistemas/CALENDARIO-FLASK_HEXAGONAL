import sys


class EditarEstudiante():

    def __init__(self, DB):
        self.DB = DB

    def obtener(self, id):
        cur = self.DB.cursor()
        cur.execute(f"SELECT * FROM estudiantes WHERE id_estudiante = {id}")
        estudiante = cur.fetchall()
        print('estudiante obtenido satisfactoriamente')
        return estudiante[0]

    def editar(self, id, estudiante):
        cur = self.DB.cursor()
        try:
            identificacion_estudiante = estudiante['identificacion_estudiante']
            nombres_estudiante = estudiante['nombres_estudiante']
            apellidos_estudiante = estudiante['apellidos_estudiante']
            telefono_estudiante = estudiante['telefono_estudiante']
            email_estudiante = estudiante['email_estudiante']
            semestre_estudiante = estudiante['semestre_estudiante']
            
            cur.execute("""
                    UPDATE estudiantes
                    SET identificacion_estudiante = %s,
                        nombres_estudiante = %s,
                        apellidos_estudiante = %s,
                        telefono_estudiante = %s,
                        email_estudiante = %s,
                        semestre_estudiante = %s
                    WHERE id_estudiante = %s
                """, (identificacion_estudiante, nombres_estudiante, apellidos_estudiante, telefono_estudiante, email_estudiante, semestre_estudiante, id))
            self.DB.commit()
            print('estudiante agregado satisfactoriamente')
            return 'editado', 200
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
