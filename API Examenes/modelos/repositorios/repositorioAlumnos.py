from modelos.entidades.alumno import Alumno
import json

class RepositorioAlumnos:
    __FILE_PATH = 'datos/alumnos.json'

    def __init__(self) -> None:
        self.__alumnos = self.__cargarTodos()

    def __cargarTodos(self) -> list:
        lista = []
        try:
            with open(self.__FILE_PATH, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                for alumno in data:
                    lista.append(Alumno.fromDict(alumno))
        except FileNotFoundError:
            print('El archivo contenedor de alumnos no existe.')
        return lista
    
    def __guardarTodos(self):
        lista = []
        for alumno in self.__alumnos:
            lista.append(alumno.toDict())
        
        try:
            with open(self.__FILE_PATH, 'w', encoding='UTF-8') as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print('El archivo contenedor de alumnos no existe.')

    def obtenerTodos(self):
        return self.__alumnos
    
    def obtenerLegajo(self, legajo: int) -> Alumno:
        if not isinstance(legajo, int) or legajo < 0:
            raise TypeError('El legajo debe ser un entero mayor a 0.')
        for a in self.__alumnos:
            if a.obtenerLegajo() == legajo:
                return a
        return None
        

    def existeLegajo(self, legajo: int) -> bool:
        if not isinstance(legajo, int) or legajo < 1:
            raise TypeError('El dato ingresado debe ser un entero mayor a 0.')
        for a in self.__alumnos:
            if a.obtenerLegajo() == legajo:
                return True
        return False

    def agregar(self, alumno: Alumno) -> bool:
        if not isinstance(alumno, Alumno):
            raise TypeError('El dato ingresado debe ser de la clase Alumno.')
        if self.existeLegajo(alumno.obtenerLegajo()):
            return False
        
        self.__alumnos.append(alumno)
        self.__guardarTodos()
        return True
    
    def eliminarPorID(self, id: int):
        if not isinstance(id, int) or id < 1:
            raise TypeError('El id debe ser de tipo entero mayor a 0.')
        
        for a in self.__alumnos:
            if a.obtenerID() == id:
                self.__alumnos.remove(a)
                self.__guardarTodos()
                return True
        return False
    
    def modificarPorID(self, id: int, legajo: int, apellido: str, nombre: str):
        if not isinstance(id, int) or id < 1:
            raise TypeError('El id debe ser de tipo entero mayor a 0.')
        if not isinstance(legajo, int) or legajo < 1:
            raise TypeError('El legajo debe ser un entero mayor a 0.')
        if not isinstance(apellido, str) or apellido.isspace() or apellido == "":
            raise TypeError('El apellido debe ser un string no vacio.')
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError('El nombre debe ser un string no vacio.')
        for a in self.__alumnos:
            if a.obtenerID() == id:
                a.establecerLegajo(legajo)
                a.establecerApellido(apellido)
                a.establecerNombre(nombre)
                self.__guardarTodos()
                return True
        return False
        
            