from modelos.entidades.temaAlumno import TemaAlumno
import json
import random

class RepositorioTemasAlumnos:
    __FILE_PATH = 'datos/temaAlumno.json'

    def __init__(self) -> None:
        self.__temasAlumnos = self.__cargarTodos()

    def __cargarTodos(self) -> list:
        lista_diccionarios = []
        lista_objetos = []
        try: 
            with open(RepositorioTemasAlumnos.__FILE_PATH, 'r', encoding='UTF-8') as file:
                lista_diccionarios = json.load(file)
        except FileNotFoundError:
            print('El archivo temaAlumno.json no existe. ')

        if len(lista_diccionarios)>0:
            for ta in lista_diccionarios:
                lista_objetos.append(TemaAlumno.fromDict(ta))
        else:
            from modelos.repositorios.repositorios import obtenerRepositorioAlumnos, obtenerRepositorioTemas
            repo_alumnos = obtenerRepositorioAlumnos()
            repo_temas = obtenerRepositorioTemas()
            if len(repo_alumnos.obtenerTodos())>0 and len(repo_temas.obtenerTodos())>0:
                for alumno in repo_alumnos.obtenerTodos():
                    lista_objetos.append(TemaAlumno(alumno, random.choice(repo_temas.obtenerTodos())))
                    self.__guardarCombinacion(lista_objetos)

        return lista_objetos

    def __guardarCombinacion(self, lista_objetos):
        lista_diccionarios = []
        for ta in lista_objetos:
            lista_diccionarios.append(ta.toDict())
        with open(RepositorioTemasAlumnos.__FILE_PATH, 'w', encoding='UTF-8') as file:
            json.dump(lista_diccionarios, file, indent=4)
    
    def __guardarTodos(self):
        lista = []
        for ta in self.__temasAlumnos:
            lista.append(ta.toDict())
        
        try:
            with open(self.__FILE_PATH, 'w') as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print('El archivo contenedor de la relacion Tema-Alumno no existe.')


    
    def obtenerPorAlumnoID(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError('La id debe ser un entero mayor a 0.')
        for ta in self.__temasAlumnos:
            if ta.obtenerAlumno().obtenerID() == id:
                return ta
        return None