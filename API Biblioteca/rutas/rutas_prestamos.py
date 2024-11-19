from flask import Blueprint, json, jsonify, request
from modelos.repositorios.repositorios import obtenerRepositorioPrestamo
from modelos.repositorios.repositorios import obtenerRepositorioLibros
from modelos.repositorios.repositorios import obtenerRepositorioSocios
from modelos.entidades.prestamo import Prestamo

prestamo_bp = Blueprint('prestamo_bp', __name__)
repo_prestamos = obtenerRepositorioPrestamo()
repo_libro = obtenerRepositorioLibros()
repo_socios = obtenerRepositorioSocios()


@prestamo_bp.post('/prestamo')
def agregarPrestamo():
    if request.is_json:
        data = request.get_json()
        if repo_socios.existeDNI(data["socio_dni"]) and repo_libro.existeISBN(data["libro_isbn"]):
            Prestamo.establecerUltimoID()
            data["id"] = Prestamo.obtenerNuevoID()
            prestamo = Prestamo.fromDic(data)

            if repo_libro.tieneEjemplares(prestamo.obtenerLibroISBN()):
                if repo_prestamos.agregar(prestamo):
                    repo_libro.restarEjemplar(prestamo.obtenerLibroISBN())
                    return jsonify({"Mensaje" : "Prestamo asignado correctamente."}), 200
                return jsonify({"Error" : "El prestamo ingresado ya se encuentra registrado."}), 400
            
            return jsonify({"Error" : "Actualmente no hay mas ejemplares del libro."}), 400
        return jsonify({"Error": "El socio o el libro no se encuentran registrados en nuestra base."}), 400
    return jsonify({"Error": "Los datos deben estar en formato JSON."}), 400
    
