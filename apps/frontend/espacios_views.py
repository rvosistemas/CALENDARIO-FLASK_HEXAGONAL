from flask import request, flash

from src.shared.infrastructure.mysql import DB

from src.espacios.app.listar_espacios_case import ListarEspaciosCase
from src.espacios.app.crear_espacio_case import CrearEspacioCase
from src.espacios.app.editar_espacio_case import EditarEspacioCase
from src.espacios.app.eliminar_espacio_case import EliminarEspacioCase


class EspaciosViews:

    def listar_espacios_view(self):
        listar_espacios_case = ListarEspaciosCase(DB)
        espacios = listar_espacios_case.listar()
        return espacios

    def crear_espacio_view(self):
        crear_espacio_case = CrearEspacioCase(DB)
        if request.method == 'POST':
            espacio = {
                'nombre_espacio': request.form['nombre_espacio'],
                'semestre_espacio': request.form['semestre_espacio'],
            }
        result = crear_espacio_case.crear(espacio)
        if result == ('creado', 201):
            flash('espacio agregado satisfactoriamente')
        else:
            flash('Error al agregar el espacio')
        return result

    def obtener_espacio_view(self, id):
        obtener_espacio_case = EditarEspacioCase(DB)
        espacio = obtener_espacio_case.obtener(id)
        return espacio

    def editar_espacio_view(self, id):
        editar_espacio_case = EditarEspacioCase(DB)
        if request.method == 'POST':
            espacio = {
                'nombre_espacio': request.form['nombre_espacio'],
                'semestre_espacio': request.form['semestre_espacio'],
            }
        result = editar_espacio_case.editar(id, espacio)
        if result == ('editado', 200):
            flash('espacio editado satisfactoriamente')
        else:
            flash('Error al editar el espacio')
        return result

    def eliminar_espacio_view(self, id):
        eliminar_espacio_case = EliminarEspacioCase(DB)
        result = eliminar_espacio_case.eliminar(id)
        if result == ('eliminado', 200):
            flash('espacio eliminado satisfactoriamente')
        else:
            flash('Error al eliminar espacio')
            return result

