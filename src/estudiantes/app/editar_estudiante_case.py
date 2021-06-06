from ..domain.editar import EditarEstudiante


class EditarEstudiantesCase:
    def __init__(self, DB):
        self.DB = DB

    def obtener(self, id):
        editarEstudiante = EditarEstudiante(self.DB)
        return editarEstudiante.obtener(id)

    def editar(self, id, estudiante):
        editarEstudiante = EditarEstudiante(self.DB)
        return editarEstudiante.editar(id, estudiante)
