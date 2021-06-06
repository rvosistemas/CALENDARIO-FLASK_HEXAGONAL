from flask import Flask, render_template, request, redirect, url_for, flash
from .estudiantes_views import EstudiantesViews

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
        result = estudiantes_views.crear_estudiante_view()
        if result == ('creado', 201):
            flash('estudiante agregado satisfactoriamente')
        else:
            flash('Error o la identificacion y/o el correo del estudiante ya existen')
        return redirect(url_for('listar_estudiantes'))


@app.route('/obtener_estudiante/<id>')
def obtener_estudiante(id):
    estudiantes_views = EstudiantesViews()
    estudiante = estudiantes_views.obtener_estudiante_view(id)
    print("$"*50, "estudiante  -->  ", estudiante)
    return render_template('estudiantes/editar_estudiante.html', estudiante=estudiante)


@app.route('/editar_estudiante/<id>', methods=['POST'])
def editar_estudiante(id):
    if request.method == 'POST':
        estudiantes_views = EstudiantesViews()
        result = estudiantes_views.editar_estudiante_view(id)
        if result == ('editado', 200):
            flash('estudiante editado satisfactoriamente')
        else:
            flash('Error o la identificacion y/o el correo del estudiante ya existen')
        return redirect(url_for('listar_estudiantes'))


@app.route('/eliminar_estudiante/<id>')
def eliminar_estudiante(id):
    estudiantes_views = EstudiantesViews()
    result = estudiantes_views.eliminar_estudiante_view(id)
    if result == ('eliminado', 200):
        flash('estudiante eliminado satisfactoriamente')
    else:
        flash('Error al eliminar estudiante')
    return redirect(url_for('listar_estudiantes'))

# --------------------------------------------------------------------------------------------------
# ---------------------------------------- CRUD ASISTENCIAS ----------------------------------------
# --------------------------------------------------------------------------------------------------


def create_app_fronted():
    app.run(debug=True, port=5000)
