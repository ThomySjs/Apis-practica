from flask import Blueprint, jsonify, json, request
from modelos.repositorios.repositorios import obtenerRepositorioLibros
from modelos.entidades.libros import Libro

libros_bp = Blueprint('liiros_bp', __name__)

repo_libros = obtenerRepositorioLibros()

@libros_bp.route('/libros', methods=['GET'])
def obtenerLibros():
    return jsonify([libro.toDic() for libro in repo_libros.obtenerLibros()])

@libros_bp.route('/libros/<int:isbn>', methods=['GET'])
def buscarLibroID(isbn):
    libroEncontrado = repo_libros.obtenerLibroISBN(isbn)
    return jsonify(libroEncontrado)

@libros_bp.route('/libros/agregar', methods=['POST'])
def agregarLibro():
    if request.is_json:
        data = request.get_json()
        try: 
            libro = Libro.from_dict(data)
            if repo_libros.agregarLibro(libro):
                return jsonify(libro.toDic()), 201
            else: 
                return jsonify({"Error" : f'Ya existe un libro registrado con el ISBN: {libro.obtenerISBN()}.'}), 400
        except ValueError as e:
            return jsonify({"Error" : {e}}), 400
    else:
        return jsonify({"Error" : 'Los datos deben estar en formato JSON.'}), 400


@libros_bp.route('/libros/<int:isbn>', methods=['PUT'])
def modificarLibro(isbn):
    if request.is_json:
        data = request.get_json()
        if "titulo" in data and "autor" in data and "genero" in data and "anio_publicacion" in data:
                titulo = data["titulo"]
                autor = data["autor"]
                genero = data["genero"]
                anio = data["anio_publicacion"]

                if repo_libros.modificarLibroISBN(isbn, titulo, autor, genero, anio):
                    return jsonify({"Mensaje" : "Datos modificados."}), 200
                else:
                    return jsonify({"Error" : "No se encontro el isbn"}), 400
        else:
            return jsonify({"Error" : "Faltan datos."}), 400
        
@libros_bp.route('/libros/<int:isbn>', methods=["DELETE"])
def eliminarLibro(isbn):
    if repo_libros.existeISBN(isbn):
        repo_libros.eliminarLibroISBN(isbn)
        return jsonify({"Mensaje" : "Libro eliminado correctamente."}), 200
    else:
        return jsonify({"Error" : "El isbn no se encuentra registrado."}), 400