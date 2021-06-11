from ..domain.editar import EditarEspacio


class EditarEspacioCase:
    def __init__(self, DB):
        self.DB = DB

    def obtener(self, id):
        editarEspacio = EditarEspacio(self.DB)
        return editarEspacio.obtener(id)

    def editar(self, id, espacio):
        editarEspacio = EditarEspacio(self.DB)
        return editarEspacio.editar(id, espacio)
