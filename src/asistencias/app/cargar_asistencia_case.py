from ..domain.cargar import CargarEstudiantesAsistencia


class CargarEstudianteAsistenciaCase:
    def __init__(self, DB):
        self.DB = DB

    def cargar(self, id_sesion):
        cargarEstudiantesAsistencia = CargarEstudiantesAsistencia(self.DB)
        return cargarEstudiantesAsistencia.cargar(id_sesion)
