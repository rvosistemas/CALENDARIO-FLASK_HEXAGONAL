from ..domain.listar import ListarEstudiantes


class ListarEstudiantesCase:
    def __init__(self, DB):
        self.DB = DB

    def listar(self):
        listarEstudiantes = ListarEstudiantes(self.DB)
        return listarEstudiantes.listar_estudiantes()
