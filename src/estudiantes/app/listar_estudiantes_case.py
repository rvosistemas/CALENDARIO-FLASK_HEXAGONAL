from ..domain.listar import ListarEstudiantes


class ListarEstudiantesCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self):
        listarEstudiantes = ListarEstudiantes(self.DB)
        return listarEstudiantes.run()
