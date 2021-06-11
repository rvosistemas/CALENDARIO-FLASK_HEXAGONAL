from ..domain.eliminar import EliminarListaAsistencia


class EliminarAsistenciaCase:
    def __init__(self, DB):
        self.DB = DB

    def eliminar(self, sesion_id):
        eliminarListaAsistencia = EliminarListaAsistencia(self.DB)
        return eliminarListaAsistencia.eliminar(sesion_id)
