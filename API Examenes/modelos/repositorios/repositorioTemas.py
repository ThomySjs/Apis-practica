from modelos.entidades.tema import Tema
import json

class RepositorioTemas:
    __FILE_PATH = 'datos/temas.json'

    def __init__(self) -> None:
        self.__temas = self.__cargarTodos()

    def __cargarTodos(self) -> list:
        lista = []
        try:
            with open(self.__FILE_PATH, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                for tema in data:
                    lista.append(Tema.fromDict(tema))
        except FileNotFoundError:
            print('El archivo contenedor de los temas no existe.')
        return lista
    
    def __guardarTodos(self):
        lista = []
        for tema in self.__temas:
            lista.append(tema.toDict())
        
        try:
            with open(self.__FILE_PATH, 'w', encoding='UTF-8') as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print('El archivo contenedor de los temas no existe.')

    def obtenerTodos(self):
        return self.__temas

    def existeNumero(self, numero: int) -> bool:
        if not isinstance(numero, int) or numero < 1:
            raise TypeError('El dato ingresado debe ser un entero mayor a 0.')
        for t in self.__temas:
            if t.obtenerNumero() == numero:
                return True
        return False

    def agregar(self, tema: Tema) -> bool:
        if not isinstance(tema, Tema):
            raise TypeError('El dato ingresado debe ser de la clase Tema.')
        if self.existeNumero(tema.obtenerNumero()):
            return False
        
        self.__temas.append(tema)
        self.__guardarTodos()
        return True
    
    def eliminarPorNumero(self, numero: int):
        if not isinstance(numero, int) or numero < 1:
            raise TypeError('El numero debe ser de tipo entero mayor a 0.')
        
        for t in self.__temas:
            if t.obtenerNumero() == numero:
                self.__temas.remove(t)
                self.__guardarTodos()
                return True
        return False
    
    def modificarPorNumero(self, numero: int, nombre: str, enunciado: str):
        if not isinstance(numero, int) or numero < 1:
            raise TypeError('El numero del tema debe ser de tipo entero.')
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError('El nombre debe ser un string no vacio.')
        if not isinstance(enunciado, str) or enunciado.isspace() or enunciado == "":
            raise TypeError('El enunciado debe ser un string no vacio.')
        for t in self.__temas:
            if t.obtenerNumero() == numero:
                t.establecerNumero(numero)
                t.establecerNombre(nombre)
                t.establecerEnunciado(enunciado)
                self.__guardarTodos()
                return True
        return False