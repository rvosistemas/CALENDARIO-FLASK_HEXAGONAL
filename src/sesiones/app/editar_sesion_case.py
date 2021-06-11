from ..domain.editar import EditarSesion


class EditarSesionCase:
    def __init__(self, DB):
        self.DB = DB

    def obtener(self, id):
        editarSesion = EditarSesion(self.DB)
        return editarSesion.obtener(id)

    def editar(self, id, sesion):
        editarSesion = EditarSesion(self.DB)
        return editarSesion.editar(id, sesion)
