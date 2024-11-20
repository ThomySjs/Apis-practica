from modelos.entidades.alumno import Alumno
from modelos.entidades.tema import Tema

class TemaAlumno:
    @classmethod
    def fromDict(cls, data: dict) -> 'TemaAlumno':
        if not isinstance(data, dict):
            raise TypeError('El dato ingresado debe ser  un diccionario.')
        return cls(Alumno.fromDict(data["alumno"]), Tema.fromDict(data["tema"]))
    
    def __init__(self, alumno: 'Alumno', tema: 'Tema') -> None:
        if not isinstance(alumno, Alumno):
            raise TypeError('El alumno debe ser de la clase Alumno.')
        if not isinstance(tema, Tema):
            raise TypeError('El tema debe ser de la clase Tema.')
        self.__alumno = alumno
        self.__tema = tema

    def obtenerAlumno(self) -> Alumno:
        return self.__alumno
    
    def obtenerTema(self) -> Tema:
        return self.__tema
    
    def establecerTema(self, tema: Tema):
        if not isinstance(tema, Tema):
            raise TypeError('El tema debe ser de la clase Tema.')
        self.__tema = tema

    def establecerAlumno(self, alumno: Alumno):
        if not isinstance(alumno, Alumno):
            raise TypeError('El alumno debe ser de la clase Alumno.')
        self.__alumno = alumno
    
    def esIgual(self, otro: 'TemaAlumno') -> bool:
        if not isinstance(otro, TemaAlumno): 
            raise TypeError('El dato debe ser de la clase TemaAlumno.')
        return self.__alumno.esIgual(otro.obtenerAlumno()) and self.__tema.esIgual(otro.obtenerTema())

    def toDict(self):
        return {
            "alumno" : self.__alumno.toDict(),
            "tema" : self.__tema.toDict()
        }