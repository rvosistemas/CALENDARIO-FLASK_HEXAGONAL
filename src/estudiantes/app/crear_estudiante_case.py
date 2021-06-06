from ..domain.crear import CrearEstudiante


class CrearEstudianteCase:
    def __init__(self, DB):
        self.DB = DB

    def crear(self, estudiante):
        crearEstudiante = CrearEstudiante(self.DB)
        return crearEstudiante.crear(estudiante)
