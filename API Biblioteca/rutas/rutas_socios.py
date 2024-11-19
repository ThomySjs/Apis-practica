from flask import Blueprint, jsonify, json, request
from modelos.repositorios.repositorios import obtenerRepositorioSocios
from modelos.entidades.socio import Socio

socios_bp = Blueprint('socios_bp', __name__)
repo_socios = obtenerRepositorioSocios()

@socios_bp.get('/socios')
def mostrarTodos():
    return jsonify([socio.toDic() for socio in repo_socios.obtenerTodos()]), 200

@socios_bp.get('/socios/<int:dni>')
def buscarDNII(dni):
    socio = repo_socios.obtenerPorDNI(dni)
    if socio != None:
        return jsonify(socio.toDic()), 200
    return jsonify({"Error" : f"No existe un socio con el dni: {dni}"}), 400

@socios_bp.post('/socios')
def agregar():
    if request.is_json:
        data = request.get_json()
        if "dni" in data and "nombre" in data and "apellido" in data and "mail" in data and "fecha_nacimiento" in data:
            socio = Socio.fromDic(data)
            if repo_socios.agregar(socio):
                return jsonify({"Mensaje" : "Datos agregados correctamente."}), 200
            else: 
                return jsonify({"Error" : f"Ya hay un socio registrado con el dni: {data["dni"]}"}), 400
        return jsonify({"Error" : "Faltan datos."}), 400
    else:
        return jsonify({"Error" : "El formato debe ser JSON."}), 400
    
@socios_bp.put('/socios/<int:dni>')
def modificar(dni):
    if request.is_json:
        data = request.get_json()
        if "dni" in data and "nombre" in data and "apellido" in data and "mail" in data and "fecha_nacimiento" in data:
            if repo_socios.modificarPorDNI(dni, data["nombre"], data["apellido"], data["mail"], data["fecha_nacimiento"]):
                return jsonify({"Mensaje" : "Datos agregados correctamente."}), 200
            else: 
                return jsonify({"Error" : f"No existe un usuario con el dni: {dni}"}), 400
        return jsonify({"Error" : "Faltan datos."}), 400
    else:
        return jsonify({"Error" : "El formato debe ser JSON."}), 400
    

@socios_bp.delete('/socios/<int:dni>')
def eliminar(dni):
    if repo_socios.eliminarPorDNI(dni):
        return jsonify({"Mensaje" : f"El socio con el dni: {dni} fue removido del sistema."}), 200
    return jsonify({"Error" : f"No existe un socio registrado con el dni: {dni}"}), 400