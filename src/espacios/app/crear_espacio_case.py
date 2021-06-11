from ..domain.crear import CrearEspacio


class CrearEspacioCase:
    def __init__(self, DB):
        self.DB = DB

    def crear(self, espacio):
        crearEspacio = CrearEspacio(self.DB)
        return crearEspacio.crear(espacio)
