from ..domain.crear import CrearEstudiante


class CrearEstudiantesCase:
    def __init__(self, DB):
        self.DB = DB

    def crear(self, identificacion_estudiante, nombres_estudiante, apellidos_estudiante, telefono_estudiante, email_estudiante, semestre_estudiante):
        crearEstudiante = CrearEstudiante(self.DB)
        return crearEstudiante.crear(identificacion_estudiante, nombres_estudiante, apellidos_estudiante, telefono_estudiante, email_estudiante, semestre_estudiante)
