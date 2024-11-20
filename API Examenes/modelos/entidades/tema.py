import json

class Tema:
    @classmethod
    def fromDict(cls, data: dict) -> 'Tema':
        if not isinstance(data, dict):
            raise TypeError('El dato ingresado debe ser de tipo diccionario.')
        return cls(data["numero"], data["nombre"], data["enunciado"])

    def __init__(self, numero: int, nombre: str, enunciado: str) -> None:
        if not isinstance(numero, int) or numero < 1:
            raise TypeError('El numero del tema debe ser de tipo entero.')
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError('El nombre debe ser un string no vacio.')
        if not isinstance(enunciado, str) or enunciado.isspace() or enunciado == "":
            raise TypeError('El enunciado debe ser un string no vacio.')
        self.__numero = numero
        self.__nombre = nombre
        self.__enunciado = enunciado

    def obtenerNumero(self) -> int:
        return self.__numero
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEnunciado(self) -> str:
        return self.__enunciado
    
    def establecerNumero(self, numero: int):
        if not isinstance(numero, int) or numero < 1:
            raise TypeError('El numero del tema debe ser de tipo entero.')
        self.__numero = numero

    def establecerNombre(self, nombre: str):
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError('El nombre debe ser un string no vacio.')
        self.__nombre = nombre
    
    def establecerEnunciado(self, enunciado: str):
        if not isinstance(enunciado, str) or enunciado.isspace() or enunciado == "":
            raise TypeError('El enunciado debe ser un string no vacio.')
        self.__enunciado = enunciado

    def esIgual(self, otro: 'Tema'):
        if not isinstance(otro, Tema):
            raise TypeError('El dato debe ser de tipo Tema.')
        return self.__numero == otro.obtenerNumero() and self.__nombre == otro.obtenerNombre() and self.__enunciado == otro.obtenerEnunciado()
    
    def toDict(self) -> dict:
        return {
            "numero" : self.__numero,
            "nombre" : self.__nombre,
            "enunciado" : self.__enunciado
        }