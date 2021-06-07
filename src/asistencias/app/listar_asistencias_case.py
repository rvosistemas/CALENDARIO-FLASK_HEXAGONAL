from ..domain.listar import ListarAsistencias


class ListarAsistenciasCase:
    def __init__(self, DB):
        self.DB = DB

    def listar_asistencias(self):
        listarAsistencias = ListarAsistencias(self.DB)
        return listarAsistencias.listar_asistencias()

    def listar_estudiantes(self, sesion_id):
        listarSesiones = ListarAsistencias(self.DB)
        return listarSesiones.listar_estudiantes(sesion_id)