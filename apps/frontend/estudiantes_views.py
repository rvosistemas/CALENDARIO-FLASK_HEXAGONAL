from flask import request, flash

from src.shared.infrastructure.mysql import DB

from src.estudiantes.app.listar_estudiantes_case import ListarEstudiantesCase
from src.estudiantes.app.crear_estudiante_case import CrearEstudianteCase
from src.estudiantes.app.editar_estudiante_case import EditarEstudianteCase
from src.estudiantes.app.eliminar_estudiante_case import EliminarEstudianteCase


class EstudiantesViews:

    def listar_estudiantes_view(self):
        listar_estudiantes_case = ListarEstudiantesCase(DB)
        estudiantes = listar_estudiantes_case.listar()
        return estudiantes

    def crear_estudiante_view(self):
        crear_estudiante_case = CrearEstudianteCase(DB)
        if request.method == 'POST':
            estudiante = {
                'identificacion_estudiante': request.form['identificacion_estudiante'],
                'nombres_estudiante': request.form['nombres_estudiante'],
                'apellidos_estudiante': request.form['apellidos_estudiante'],
                'telefono_estudiante': request.form['telefono_estudiante'],
                'email_estudiante': request.form['email_estudiante'],
                'semestre_estudiante': request.form['semestre_estudiante'],
            }
        result = crear_estudiante_case.crear(estudiante)
        if result == ('creado', 201):
            flash('estudiante agregado satisfactoriamente')
        else:
            flash('Error o la identificacion y/o el correo del estudiante ya existen')
        return result

    def obtener_estudiante_view(self, id):
        obtener_estudiante_case = EditarEstudianteCase(DB)
        estudiante = obtener_estudiante_case.obtener(id)
        return estudiante

    def editar_estudiante_view(self, id):
        editar_estudiante_case = EditarEstudianteCase(DB)
        if request.method == 'POST':
            estudiante = {
                'identificacion_estudiante': request.form['identificacion_estudiante'],
                'nombres_estudiante': request.form['nombres_estudiante'],
                'apellidos_estudiante': request.form['apellidos_estudiante'],
                'telefono_estudiante': request.form['telefono_estudiante'],
                'email_estudiante': request.form['email_estudiante'],
                'semestre_estudiante': request.form['semestre_estudiante'],
            }
        result = editar_estudiante_case.editar(id, estudiante)
        if result == ('editado', 200):
            flash('estudiante editado satisfactoriamente')
        else:
            flash('Error o la identificacion y/o el correo del estudiante ya existen')
        return result

    def eliminar_estudiante_view(self, id):
        eliminar_estudiante_case = EliminarEstudianteCase(DB)
        result = eliminar_estudiante_case.eliminar(id)
        if result == ('eliminado', 200):
            flash('estudiante eliminado satisfactoriamente')
        else:
            flash('Error al eliminar estudiante')
            return result
