import json

class Alumno:
    __ULTIMO_ID = 0
    __FILE_PATH = 'datos/alumnos.json'

    @classmethod
    def obtenerNuevoID(cls) -> int:
        cls.establecerUltimoID()
        return cls.__ULTIMO_ID + 1
    
    @classmethod
    def establecerUltimoID(cls):
        try:
            with open(cls.__FILE_PATH, 'r') as file:
                data = json.load(file)
                if len(data) > 0:
                    cls.__ULTIMO_ID = data[-1]["id"]
                else:
                    cls.__ULTIMO_ID = 0
        except FileNotFoundError:
            print('El archivo contenedor de alumnos no existe.')
            cls.__ULTIMO_ID = 0
    
    @classmethod
    def fromDict(cls, data: dict) -> 'Alumno':
        if not isinstance(data, dict):
            raise TypeError('El tipo de dato ingresado debe ser un disccionario.')
        return cls(data["legajo"], data["apellido"], data["nombre"], data["id"])
    
    def __init__(self, legajo: int, apellido: str, nombre: str, id: int = None ) -> None:
        if not isinstance(legajo, int) or legajo < 1:
            raise TypeError('El legajo debe ser un entero mayor a 0.')
        if not isinstance(apellido, str) or apellido.isspace() or apellido == "":
            raise TypeError('El apellido debe ser un string no vacio.')
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError('El nombre debe ser un string no vacio.')
        self.__id = id
        self.__legajo = legajo
        self.__apellido = apellido
        self.__nombre = nombre

    def obtenerID(self) -> int:
        return self.__id
    
    def obtenerLegajo(self) -> int:
        return self.__legajo
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerApellido(self) -> str:
        return self.__apellido
    
    def establecerLegajo(self, legajo: int): 
        if not isinstance(legajo, int) or legajo < 1:
            raise TypeError('El legajo debe ser un entero mayor a 0.')
        self.__legajo = legajo

    def establecerApellido(self, apellido: str): 
        if not isinstance(apellido, str) or apellido.isspace() or apellido == "":
            raise TypeError('El apellido debe ser un string no vacio.')
        self.__apellido = apellido

    def establecerNombre(self, nombre: str):
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError('El nombre debe ser un string no vacio.')
        self.__nombre = nombre

    def esIgual(self, otro: 'Alumno'):
        if not isinstance(otro, Alumno):
            raise TypeError('El dato ingresado debe ser de tipo Alumno.')
        return self.__legajo == otro.obtenerLegajo() and self.__id == otro.obtenerID()

    def toDict(self) -> dict:
        return {"id" : self.__id, "legajo" : self.__legajo, "nombre" : self.__nombre, "apellido" : self.__apellido}