from re import I
from flask import Flask, jsonify, request

from src.shared.infrastructure.mysql import DB
from src.estudiantes.app.listar_estudiantes_case import ListarEstudiantesCase
from src.estudiantes.app.crear_estudiante_case import CrearEstudianteCase

app = Flask(__name__)


@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    listar_estudiantes_case = ListarEstudiantesCase(DB)
    return jsonify(listar_estudiantes_case.listar_estudiantes())


@app.route('/agregar_estudiante', methods=['POST'])
def crear_estudiante():
    crear_estudiante_case = CrearEstudianteCase(DB)
    data = request.get_json()[0]
    identificacion_estudiante = data['identificacion_estudiante']
    nombres_estudiante = data['nombres_estudiante']
    apellidos_estudiante = data['apellidos_estudiante']
    telefono_estudiante = data['telefono_estudiante']
    email_estudiante = data['email_estudiante']
    semestre_estudiante = data['semestre_estudiante']
    return crear_estudiante_case.crear_estudiante(
        identificacion_estudiante, nombres_estudiante,
        apellidos_estudiante, telefono_estudiante, email_estudiante, semestre_estudiante)


def create_app_api():
    app.run(debug=True, port=5100)
