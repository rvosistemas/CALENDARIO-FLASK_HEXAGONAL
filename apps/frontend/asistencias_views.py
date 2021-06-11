from flask import request, flash

from src.shared.infrastructure.mysql import DB

from src.asistencias.app.cargar_asistencia_case import CargarEstudianteAsistenciaCase
from src.asistencias.app.eliminar_asistencia_case import EliminarAsistenciaCase
from src.asistencias.app.listar_asistencias_case import ListarAsistenciasCase
from src.asistencias.app.tomar_asistencia_case import TomarAsistenciasCase


class AsistenciasViews:

    def cargar_estudiantes_asistencia_view(self, id_sesion):
        cargar_estudiante_asistencia_case = CargarEstudianteAsistenciaCase(DB)
        result = cargar_estudiante_asistencia_case.cargar(id_sesion)
        if result.get('id_sesion', False):
            if result['estudiantes'] == ():
                flash('No hay estudiantes en el semestre del espacio academico')
            return result
        else:
            flash('La asistencia que desea cargar ya existe')
            return result

    def eliminar_asistencia_view(self, sesion_id):
        eliminar_asistencia_case = EliminarAsistenciaCase(DB)
        result = eliminar_asistencia_case.eliminar(sesion_id)
        if result == ('eliminada', 200):
            flash('asistencia eliminada satisfactoriamente')
        else:
            flash('Error al eliminar asistencia')
            return result

    def listar_asistencias_view(self):
        listar_asistencia_case = ListarAsistenciasCase(DB)
        sesion, espacios = listar_asistencia_case.listar_asistencias()
        return sesion, espacios

    def listar_estudiantes_asistencia_view(self, sesion_id):
        listar_asistencia_case = ListarAsistenciasCase(DB)
        sesiones, espacios, lista_estudiantes, sesion_id = listar_asistencia_case.listar_estudiantes_asistencia(
            sesion_id)
        if lista_estudiantes == []:
            flash('La lista no tiene estudiantes')
        return sesiones, espacios, lista_estudiantes, sesion_id

    def tomar_asistencias_view(self):
        tomar_asistencias_case = TomarAsistenciasCase(DB)
        sesiones, espacios = tomar_asistencias_case.tomar_asistencias()
        return sesiones, espacios

    def tomar_asistencia_view(self):
        tomar_asistencias_case = TomarAsistenciasCase(DB)
        try:
            asistentes = request.form.to_dict(flat=False)
            result = tomar_asistencias_case.tomar_asistencia(
                asistentes)
            if result == ('creada', 201):
                flash('asistencia agregada satisfactoriamente')
            else:
                flash('Error al agregar asistencia')
        except:
            flash('No se puede guardar sin cargar estudiantes')
        return result
