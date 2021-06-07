from ..domain.tomar import TomarAsistencias


class TomarAsistenciasCase:
    def __init__(self, DB):
        self.DB = DB

    def tomar_sesiones(self):
        tomarAsistencias = TomarAsistencias(self.DB)
        return tomarAsistencias.tomar_sesiones(id)

    def tomar_asistencias(self, id, asistencia):
        tomarAsistencias = TomarAsistencias(self.DB)
        return tomarAsistencias.tomar_asistencias(id, asistencia)
