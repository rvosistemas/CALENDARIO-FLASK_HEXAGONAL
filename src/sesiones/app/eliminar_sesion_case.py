from ..domain.eliminar import EliminarSesion


class EliminarSesionCase:
    def __init__(self, DB):
        self.DB = DB

    def eliminar(self, id):
        eliminarSesion = EliminarSesion(self.DB)
        return eliminarSesion.eliminar(id)
