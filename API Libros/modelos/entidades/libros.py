import json 
import datetime

class Libro:
    @classmethod
    def from_dict(cls, data: dict) -> 'Libro':
        if not isinstance(data, dict):
            raise TypeError('El tipo de dato debe ser dict')
        return cls(data["titulo"], data["autor"], data["genero"], data["anio_publicacion"], data["ISBN"])
        

    def __init__(self, titulo: str, autor: str, genero: str, anioPublicacion: int, ISBN:int) -> None:
        if not isinstance(titulo, str):
            raise TypeError('El tipo de dato debe ser str.')
        if not isinstance(autor, str):
            raise TypeError('El tipo de dato debe ser str.')
        if not isinstance(genero, str):
            raise TypeError('El tipo de dato debe ser str.')
        if not isinstance(anioPublicacion, int):
            raise TypeError('El tipo de dato debe ser int.')
        if not isinstance(ISBN, int):
            raise TypeError('El tipo de dato debe ser int.')
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anioPublicacion = anioPublicacion
        self.__ISBN = ISBN
        self.__cantidad_ejemplares  = None

    def establecerTitulo(self, titulo: str):
        if not isinstance(titulo, str) or titulo.isspace() or titulo == "":
            raise TypeError('El titulo debe ser un string no vacio.')
        self.__titulo = titulo

    def establecerAutor(self, autor: str):
        if not isinstance(autor, str) or autor.isspace() or autor == "":
            raise TypeError('El nombre del autor debe ser un string no vacio.')
        self.__autor = autor

    def establecerGenero(self, genero: str):
        if not isinstance(genero, str) or genero.isspace() or genero == "":
            raise TypeError('El nombre del autor debe ser un string no vacio.')
        self.__genero = genero

    def establecerAnio(self, anio: int):
        if not isinstance(anio, int) or anio <= 0:
            raise TypeError('El anio debe ser un entero mayor a 0.')
        self.__anioPublicacion = anio

    def obtenerTitulo(self) -> str:
        return self.__titulo
    
    def obtenerAutor(self) -> str:
        return self.__autor
    
    def obtenerGenero(self) -> str:
        return self.__genero
    
    def obtenerAnio(self) -> datetime:
        return self.__anioPublicacion
    
    def obtenerISBN(self) -> int:
        return self.__ISBN
    
    def toDic(self):
        return {"titulo" : self.__titulo, "autor" : self.__autor, "genero" : self.__genero, "anio_publicacion" : self.__anioPublicacion, "ISBN" : self.__ISBN}
    
    def __str__(self) -> str:
        return f"Titulo: {self.__titulo}, Autor: {self.__autor}, Genero: {self.__genero}, Fecha de Publicacion: {self.__anioPublicacion}, ISBN: {self.__ISBN}."


