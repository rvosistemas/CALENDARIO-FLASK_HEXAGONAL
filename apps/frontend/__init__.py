from flask import Flask, render_template, request, redirect, url_for
from .estudiantes_views import EstudiantesViews
from .espacios_views import EspaciosViews

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


def create_app_fronted():
    app.run(debug=True, port=5000)
