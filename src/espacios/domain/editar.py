import sys


class EditarEspacio():

    def __init__(self, DB):
        self.DB = DB

    def obtener(self, id):
        cur = self.DB.cursor()
        cur.execute(f"SELECT * FROM espacios WHERE id_espacio = {id}")
        espacio = cur.fetchall()
        print('espacio obtenido satisfactoriamente')
        return espacio[0]

    def editar(self, id, espacio):
        cur = self.DB.cursor()
        try:
            nombres_espacio = espacio['nombres_espacio']
            semestre_espacio = espacio['semestre_espacio']
            
            cur.execute("""
                    UPDATE espacios
                    SET nombres_espacio = %s,
                        semestre_espacio = %s,
                    WHERE id_espacio = %s
                """, (nombres_espacio, semestre_espacio, id))
            self.DB.commit()
            print('espacio editado satisfactoriamente')
            return 'editado', 200
        except:
            err = sys.exc_info()[0]  # captura todos los errores
            print(f' ha ocurrido el siguente error: {err}')
            return err, 500
