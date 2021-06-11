from ..domain.tomar import TomarAsistencias


class TomarAsistenciasCase:
    def __init__(self, DB):
        self.DB = DB

    def tomar_asistencias(self):
        tomarAsistencias = TomarAsistencias(self.DB)
        return tomarAsistencias.tomar_asistencias()

    def tomar_asistencia(self, asistentes):
        tomarAsistencia = TomarAsistencias(self.DB)
        return tomarAsistencia.tomar_asistencia(asistentes)
