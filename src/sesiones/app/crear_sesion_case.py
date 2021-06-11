from ..domain.crear import CrearSesion


class CrearSesionCase:
    def __init__(self, DB):
        self.DB = DB

    def crear(self, sesion):
        crearSesion = CrearSesion(self.DB)
        return crearSesion.crear(sesion)
