import json
from modelos.entidades.libros import Libro


class RepositorioLibros:
    FILE_PATH = 'datos\libros.json'

    def __init__(self):
        self.__libros = self.__cargarLibros()

    def __cargarLibros(self):
        lista = []

        try:
            with open(RepositorioLibros.FILE_PATH, 'r') as file:
                libros = json.load(file)
                for l in libros:
                    lista.append(Libro.from_dict(l))
        except FileNotFoundError:
            print('No se ha encontrado el archivo.')

        return lista

    def __guardarLibros(self):
        try:
            lista = []
            for l in self.__libros:
                lista.append(l.toDic())

            with open(RepositorioLibros.FILE_PATH, 'w') as file:
                json.dump(lista, file,  indent=4)
        except FileNotFoundError:
            print('El archivo con los datos de los libros no existe.')

    def tieneEjemplares(self, isbn:int):
        if not isinstance(isbn, int) or isbn < 0:
            raise TypeError('El tipo de dato debe ser int.')
        for libro in self.__libros:
            if libro.obtenerISBN() == isbn:
                if libro.obtenerEjemplares() > 0:
                    return True
        return False

    def restarEjemplar(self, isbn: int):
        if not isinstance(isbn, int) or isbn < 0:
            raise TypeError('El tipo de dato debe ser int.')
        for libro in self.__libros:
            if libro.obtenerISBN() == isbn:
                    libro.restarEjemplares()
                    self.__guardarLibros()
                    return True
        return False

    
    def sumarEjemplar(self, isbn: int):
        if not isinstance(isbn, int) or isbn < 0:
            raise TypeError('El tipo de dato debe ser int.')
        for libro in self.__libros:
            if libro.obtenerISBN() == isbn:
                    libro.sumarEjemplares()
                    self.__guardarLibros()
                    return True
        return False

    def obtenerLibros(self) -> list:
        return self.__libros
    
    def obtenerLibroISBN(self, ISBN: int) -> Libro:
        if not isinstance(ISBN, int) or ISBN <= 0:
            raise TypeError('El ISBN tiene que ser un entero mayor a 0.')
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                return libro.toDic()
        return None
    
    def existeISBN(self, ISBN: int) -> bool:
        if not isinstance(ISBN, int) or ISBN <= 0:
            raise TypeError('El ISBN tiene que ser un entero mayor a 0.')
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                return True
        return False
    
    def agregarLibro(self, libro: 'Libro'):
        if not isinstance(libro, Libro):
            raise TypeError('El libro tiene que ser de tipo libro.')
        if self.existeISBN(libro.obtenerISBN()):
            print('El libro ya se encuentra cargado.')
            return False
        else:
            self.__libros.append(libro)
            self.__guardarLibros()
            return True

    def modificarLibroISBN(self, ISBN: int, titulo: str, autor: str, genero: str, anio_publicacion: int) :
        if not isinstance(ISBN, int) or ISBN <= 0:
            raise TypeError('El ISBN tiene que ser un entero mayor a 0.')
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                libro.establecerTitulo(titulo)
                libro.establecerAutor(autor)
                libro.establecerGenero(genero)
                libro.establecerAnio(anio_publicacion)
                self.__guardarLibros()
                return  True
        return False
    
    def eliminarLibroISBN(self, ISBN: int):
        if not isinstance(ISBN, int) or ISBN <= 0:
            raise TypeError('El ISBN tiene que ser un entero mayor a 0.')
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                self.__libros.remove(libro)
                self.__guardarLibros()
                return True
        return False
        
        

        
