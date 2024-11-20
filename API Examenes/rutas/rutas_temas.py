from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtenerRepositorioTemas
from modelos.entidades.tema import Tema

temas_bp = Blueprint('temas_bp', __name__)
repo_temas = obtenerRepositorioTemas()

@temas_bp.get('/temas')
def obtenerTodos():
    return jsonify([tema.toDict() for tema in repo_temas.obtenerTodos()]), 200

@temas_bp.post('/temas')
def agregarTema():
    if request.is_json:
        data = request.get_json()
        if "numero" in data and "nombre" in data and "enunciado" in data:
            if repo_temas.agregar(Tema.fromDict(data)):
                return jsonify({"Mensaje": "Tema agregado correctamente."}), 200
            return jsonify({"Error" : "Ya existe un tema registrado con ese numero."}), 400
        return jsonify({"Error": "Faltan datos."}), 400
    return jsonify({"Error": "El formato debe ser JSON."}), 400

@temas_bp.delete('/temas/<int:numero>')
def eliminarTema(numero):
    if repo_temas.eliminarPorNumero(numero):
        return jsonify({"Mensaje": "Tema eliminado correctamente."}), 200
    return jsonify({"Error": "No existe un tema asignado a ese numero."}), 400