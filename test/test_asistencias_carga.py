from apps.frontend import cargar_estudiantes_asistencia
from src.asistencias.domain import cargar
from src.asistencias.domain.cargar import CargarEstudiantesAsistencia
from src.shared.infrastructure.mysql import DB


def test_carga():
    id_sesion = 1
    cargar_estudiantes_asistencia = CargarEstudiantesAsistencia(DB)
    result = cargar_estudiantes_asistencia.cargar(id_sesion=id_sesion)
