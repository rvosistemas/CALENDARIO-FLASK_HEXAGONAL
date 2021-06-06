from ..domain.eliminar import EliminarEstudiante


class EliminarEstudianteCase:
    def __init__(self, DB):
        self.DB = DB

    def eliminar(self, id):
        eliminarEstudiante = EliminarEstudiante(self.DB)
        return eliminarEstudiante.eliminar(id)
