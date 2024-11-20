from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtenerRepositorioTA, obtenerConfirmados


ta_bp = Blueprint('ta_bp', __name__)
repo_TA = obtenerRepositorioTA()
repo_confirmados = obtenerConfirmados()

@ta_bp.get('/examenesDisponibles/<int:id>')
def obtenerEnunciado(id):
    ta = repo_TA.obtenerPorAlumnoID(id)
    if ta is None:
        return jsonify({"Error": "El id ingresado no se encuentra registrado."})
    return jsonify(ta.toDict())

@ta_bp.post('/examenesConfirmados')
def confirmar():
    if request.is_json:
        data = request.get_json()
        if "alumno" in data and "id" in data["alumno"] and "legajo" in data["alumno"] and "nombre" in data["alumno"] and "apellido" in data["alumno"] and "tema" in data and "numero" in data["tema"] and "enunciado" in data["tema"] and "nombre" in data["tema"]:
            if repo_confirmados.confirmar(data):
                return jsonify({"Mensaje": "Examen confirmado!"}), 200
            return jsonify({"Error": f"El alumno con id: {data["alumno"]["id"]} ya confirmo su examen."}), 400
        return jsonify({"Error": "Faltan datos."}), 400
    return jsonify({"Error": "El formato debe ser JSON."}), 400
           