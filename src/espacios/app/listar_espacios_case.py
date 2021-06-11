from ..domain.listar import ListarEspacios


class ListarEspaciosCase:
    def __init__(self, DB):
        self.DB = DB

    def listar(self):
        listarEspacios = ListarEspacios(self.DB)
        return listarEspacios.listar_espacios()
