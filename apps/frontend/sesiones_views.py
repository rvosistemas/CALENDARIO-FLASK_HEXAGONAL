from flask import request, flash

from src.shared.infrastructure.mysql import DB

from src.sesiones.app.listar_sesiones_case import ListarSesionesCase
from src.sesiones.app.crear_sesion_case import CrearSesionCase
from src.sesiones.app.editar_sesion_case import EditarSesionCase
from src.sesiones.app.eliminar_sesion_case import EliminarSesionCase


class SesionesViews:

    def listar_sesiones_view(self):
        listar_sesiones_case = ListarSesionesCase(DB)
        sesiones, espacios = listar_sesiones_case.listar()
        return sesiones, espacios

    def crear_sesion_view(self):
        crear_sesion_case = CrearSesionCase(DB)
        if request.method == 'POST':
            sesion = {
                'fecha_asistencia': request.form['fecha_asistencia'],
                'hora_inicio_asistencia': request.form['hora_inicio_asistencia'],
                'hora_fin_asistencia': request.form['hora_fin_asistencia'],
                'espacio_id': request.form['espacio_id'],
            }
        result = crear_sesion_case.crear(sesion)
        if result == ('creada', 201):
            flash('sesion agregada satisfactoriamente')
        else:
            flash('Error al agregar sesion')
        return result

    def obtener_sesion_view(self, id):
        obtener_sesion_case = EditarSesionCase(DB)
        sesion, espacios = obtener_sesion_case.obtener(id)
        return sesion, espacios

    def editar_sesion_view(self, id):
        editar_sesion_case = EditarSesionCase(DB)
        if request.method == 'POST':
            sesion = {
                'fecha_asistencia': request.form['fecha_asistencia'],
                'hora_inicio_asistencia': request.form['hora_inicio_asistencia'],
                'hora_fin_asistencia': request.form['hora_fin_asistencia'],
                'espacio_id': request.form['espacio_id'],
            }
        result = editar_sesion_case.editar(id, sesion)
        if result == ('editada', 200):
            flash('sesion editada satisfactoriamente')
        else:
            flash('Error al editar sesion')
        return result

    def eliminar_sesion_view(self, id):
        eliminar_sesion_case = EliminarSesionCase(DB)
        result = eliminar_sesion_case.eliminar(id)
        if result == ('eliminada', 200):
            flash('sesion eliminada satisfactoriamente')
        else:
            flash('Error al eliminar sesion')
            return result

