from flask import Blueprint,jsonify, request, json
from modelos.repositorios.repositorios import obtenerRepositorioAlumnos
from modelos.entidades.alumno import Alumno

alumnos_bp = Blueprint('alumnos_bp', __name__)
repo_alumnos = obtenerRepositorioAlumnos()

@alumnos_bp.get('/alumnos/<int:legajo>')
def obtenerDatos(legajo):
    datos = repo_alumnos.obtenerLegajo(legajo)
    if datos is None:
        return jsonify({"Error": f"No existe un alumno registrado con el legajo: {legajo}."}), 400
    return jsonify(datos.toDict()), 200

@alumnos_bp.post('/alumnos')
def agregarAlumno():
    if request.is_json:
        data = request.get_json()
        data["id"] = Alumno.obtenerNuevoID()
        if "legajo" in data and "nombre" in data and "apellido" in data:
            if repo_alumnos.agregar(Alumno.fromDict(data)):
                return jsonify({"Mensaje": "Datos cargados correctamente."}), 200
            return jsonify({"Error": "Ya existe un alumno con ese legajo."}),400
        return jsonify({"Error": "Faltan datos."}), 400
    return jsonify({"Error": "El formato debe ser JSON."}), 400

@alumnos_bp.delete('/alumnos/<int:id>')
def eliminarAlumno(id):
    if repo_alumnos.eliminarPorID(id):
        return jsonify({"Mensaje": "Alumno eliminado correctamente."}), 200
    return jsonify({"Error": "No existe un alumno con esa ID."}), 400
        