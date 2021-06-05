from src.estudiantes.app.listar_estudiante_case import ListarEstudiantesCase
from src.shared.infrastructure.mysql import DB
case = ListarEstudiantesCase(DB)
print(case.run())
