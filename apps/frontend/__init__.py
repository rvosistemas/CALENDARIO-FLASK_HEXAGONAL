from flask import Flask, render_template, request, redirect, url_for

from .estudiantes_views import EstudiantesViews
from .espacios_views import EspaciosViews
from .sesiones_views import SesionesViews
from .asistencias_views import AsistenciasViews

app = Flask(__name__, template_folder='../frontend/templates')

app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    return render_template('index.html')

# --------------------------------------------------------------------------------------------------
# ---------------------------------------- CRUD ESTUDIANTES ----------------------------------------
# --------------------------------------------------------------------------------------------------


@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    estudiantes_views = EstudiantesViews()
    estudiantes = estudiantes_views.listar_estudiantes_view()
    return render_template('estudiantes/estudiantes.html', estudiantes=estudiantes)


@app.route('/agregar_estudiante', methods=['POST'])
def crear_estudiante():
    if request.method == 'POST':
        estudiantes_views = EstudiantesViews()
        estudiantes_views.crear_estudiante_view()
        return redirect(url_for('listar_estudiantes'))


@app.route('/obtener_estudiante/<id>')
def obtener_estudiante(id):
    estudiantes_views = EstudiantesViews()
    estudiante = estudiantes_views.obtener_estudiante_view(id)
    return render_template('estudiantes/editar_estudiante.html', estudiante=estudiante)


@app.route('/editar_estudiante/<id>', methods=['POST'])
def editar_estudiante(id):
    if request.method == 'POST':
        estudiantes_views = EstudiantesViews()
        estudiantes_views.editar_estudiante_view(id)
        return redirect(url_for('listar_estudiantes'))


@app.route('/eliminar_estudiante/<id>')
def eliminar_estudiante(id):
    estudiantes_views = EstudiantesViews()
    estudiantes_views.eliminar_estudiante_view(id)
    return redirect(url_for('listar_estudiantes'))

# # --------------------------------------------------------------------------------------------------
# # ----------------------------------------- CRUD ESPACIOS ------------------------------------------
# # --------------------------------------------------------------------------------------------------


@app.route('/espacios', methods=['GET'])
def listar_espacios():
    espacios_views = EspaciosViews()
    espacios = espacios_views.listar_espacios_view()
    return render_template('espacios/espacios.html', espacios=espacios)


@app.route('/agregar_espacio', methods=['POST'])
def crear_espacio():
    if request.method == 'POST':
        espacios_views = EspaciosViews()
        espacios_views.crear_espacio_view()
        return redirect(url_for('listar_espacios'))


@app.route('/obtener_espacio/<id>')
def obtener_espacio(id):
    espacios_views = EspaciosViews()
    espacio = espacios_views.obtener_espacio_view(id)
    return render_template('espacios/editar_espacio.html', espacio=espacio)


@app.route('/editar_espacio/<id>', methods=['POST'])
def editar_espacio(id):
    if request.method == 'POST':
        espacios_views = EspaciosViews()
        espacios_views.editar_espacio_view(id)
        return redirect(url_for('listar_espacios'))


@app.route('/eliminar_espacio/<id>')
def eliminar_espacio(id):
    espacios_views = EspaciosViews()
    espacios_views.eliminar_espacio_view(id)
    return redirect(url_for('listar_espacios'))

# # --------------------------------------------------------------------------------------------------
# # ----------------------------------------- CRUD SESIONES ------------------------------------------
# # --------------------------------------------------------------------------------------------------


@app.route('/sesiones', methods=['GET'])
def listar_sesiones():
    sesiones_views = SesionesViews()
    sesiones, espacios = sesiones_views.listar_sesiones_view()
    return render_template('sesiones/sesiones.html', sesiones=sesiones, espacios=espacios)


@app.route('/agregar_sesion', methods=['POST'])
def crear_sesion():
    if request.method == 'POST':
        sesiones_views = SesionesViews()
        sesiones_views.crear_sesion_view()
        return redirect(url_for('listar_sesiones'))


@app.route('/obtener_sesion/<id>')
def obtener_sesion(id):
    sesiones_views = SesionesViews()
    sesion, espacios = sesiones_views.obtener_sesion_view(id)
    return render_template('sesiones/editar_sesion.html', sesion=sesion, espacios=espacios)


@app.route('/editar_sesion/<id>', methods=['POST'])
def editar_sesion(id):
    if request.method == 'POST':
        sesiones_views = SesionesViews()
        sesiones_views.editar_sesion_view(id)
        return redirect(url_for('listar_sesiones'))


@app.route('/eliminar_sesion/<id>')
def eliminar_sesion(id):
    sesiones_views = SesionesViews()
    sesiones_views.eliminar_sesion_view(id)
    return redirect(url_for('listar_sesiones'))

# # --------------------------------------------------------------------------------------------------
# # ---------------------------------------- CRUD ASISTENCIAS ----------------------------------------
# # --------------------------------------------------------------------------------------------------


@app.route('/cargar_estudiantes_asistencia/<id_sesion>')
def cargar_estudiantes_asistencia(id_sesion):
    asistencias_views = AsistenciasViews()
    result = asistencias_views.cargar_estudiantes_asistencia_view(id_sesion)
    if result.get('id_sesion', False):
        asistencias = result['asistencias']
        espacios = result['espacios']
        estudiantes = result['estudiantes']
        id_asistencia = result['id_asistencia']
        nombre_espacio = result['nombre_espacio']
        return render_template('asistencias/tomar_asistencias.html', asistencias=asistencias, espacios=espacios, estudiantes=estudiantes, id_asistencia=id_asistencia, nombre_espacio=nombre_espacio)
    else:
        asistencias = result['asistencias']
        espacios = result['espacios']
        return render_template('asistencias/tomar_asistencias.html', asistencias=asistencias, espacios=espacios)


@app.route('/eliminar_asistencia/<sesion_id>')
def eliminar_asistencia(sesion_id):
    asistencias_views = AsistenciasViews()
    asistencias_views.eliminar_asistencia_view(sesion_id)
    return redirect(url_for('listar_sesiones'))


@app.route('/listar_asistencias')
def listar_asistencias():
    asistencias_views = AsistenciasViews()
    sesiones, espacios = asistencias_views.listar_asistencias_view()
    return render_template('asistencias/listar_asistencias.html', sesiones=sesiones, espacios=espacios)


@app.route('/listar_estudiantes/<asistencia_id>')
def listar_estudiantes():
    asistencias_views = AsistenciasViews()
    sesiones, espacios, lista_estudiantes, sesion_id = asistencias_views.listar_estudiantes_view()
    return render_template('asistencias/listar_asistencias.html', sesiones=sesiones, espacios=espacios, lista_estudiantes=lista_estudiantes, sesion_id=sesion_id)


@app.route('/tomar_sesiones')
def tomar_sesiones():
    asistencias_views = AsistenciasViews()
    sesiones, espacios = asistencias_views.tomar_sesiones_view()
    return render_template('asistencias/listar_asistencias.html', sesiones=sesiones, espacios=espacios)


@app.route('/tomar_asistencia', methods=['POST'])
def tomar_asistencia():
    if request.method == 'POST':
        asistencias_views = AsistenciasViews()
        asistencias_views.tomar_asistencias_view()
    return redirect(url_for('tomar_sesiones'))


# # --------------------------------------------------------------------------------------------------
# # ------------------------------------------ APP CREATED -------------------------------------------
# # --------------------------------------------------------------------------------------------------


def create_app_fronted():
    app.run(debug=True, port=5000)
