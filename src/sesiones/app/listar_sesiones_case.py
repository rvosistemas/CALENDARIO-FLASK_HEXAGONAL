from ..domain.listar import ListarSesiones


class ListarSesionesCase:
    def __init__(self, DB):
        self.DB = DB

    def listar(self):
        listarSesiones = ListarSesiones(self.DB)
        return listarSesiones.listar_espacios()
