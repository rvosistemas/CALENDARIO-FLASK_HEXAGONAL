from ..domain.eliminar import EliminarEspacio


class EliminarEspacioCase:
    def __init__(self, DB):
        self.DB = DB

    def eliminar(self, id):
        eliminarEspacio = EliminarEspacio(self.DB)
        return eliminarEspacio.eliminar(id)
