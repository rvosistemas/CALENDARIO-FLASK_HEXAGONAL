from flask import request

from src.shared.infrastructure.mysql import DB

from src.estudiantes.app.listar_estudiantes_case import ListarEstudiantesCase
from src.estudiantes.app.crear_estudiante_case import CrearEstudiantesCase
from src.estudiantes.app.editar_estudiante_case import EditarEstudiantesCase
from src.estudiantes.app.eliminar_estudiante_case import EliminarEstudiantesCase

class EstudiantesViews:

    def listar_estudiantes_view(self):
        listar_estudiantes_case = ListarEstudiantesCase(DB)
        estudiantes = listar_estudiantes_case.listar()
        return estudiantes

    def crear_estudiante_view(self):
        crear_estudiante_case = CrearEstudiantesCase(DB)
        if request.method == 'POST':
            estudiante = {
                'identificacion_estudiante': request.form['identificacion_estudiante'],
                'nombres_estudiante': request.form['nombres_estudiante'],
                'apellidos_estudiante': request.form['apellidos_estudiante'],
                'telefono_estudiante': request.form['telefono_estudiante'],
                'email_estudiante': request.form['email_estudiante'],
                'semestre_estudiante': request.form['semestre_estudiante'],
            }
        return crear_estudiante_case.crear(estudiante)

    def obtener_estudiante_view(self, id):
        obtener_estudiantes_case = EditarEstudiantesCase(DB)
        estudiante = obtener_estudiantes_case.obtener(id)
        return estudiante
    
    def editar_estudiante_view(self, id):
        editar_estudiante_case = EditarEstudiantesCase(DB)
        if request.method == 'POST':
            estudiante = {
                'identificacion_estudiante': request.form['identificacion_estudiante'],
                'nombres_estudiante': request.form['nombres_estudiante'],
                'apellidos_estudiante': request.form['apellidos_estudiante'],
                'telefono_estudiante': request.form['telefono_estudiante'],
                'email_estudiante': request.form['email_estudiante'],
                'semestre_estudiante': request.form['semestre_estudiante'],
            }
        return editar_estudiante_case.editar(id, estudiante)
            
    def eliminar_estudiante_view(self, id):
        eliminar_estudiantes_case = EliminarEstudiantesCase(DB)
        return eliminar_estudiantes_case.eliminar(id)