import json

class repositorioExamenesConfirmados:
    __FILE_PATH = 'datos/examenesConfirmados.json'

    def __init__(self) -> None:
        self.__examenesConfirmados = self.__cargarTodos()

    def __cargarTodos(self):
        try:
            with open(repositorioExamenesConfirmados.__FILE_PATH, 'r', encoding='UTF-8') as file:
                lista = json.load(file)
        except FileNotFoundError:
            print('No existe el archivo examenesConfirmados.json')
        return lista
    
    def __guardarTodos(self):
        with open(repositorioExamenesConfirmados.__FILE_PATH, 'w', encoding='UTF-8') as file:
            json.dump(self.__examenesConfirmados, file, indent=4)

    def confirmar(self, dato:  dict):
        if not isinstance(dato, dict):
            raise TypeError('El dato ingresado debe ser de tipo diccionario.')
        for examen in self.__examenesConfirmados:
            if examen["alumno"]["id"] == dato["alumno"]["id"]:
                return False
        self.__examenesConfirmados.append(dato)
        self.__guardarTodos()
        return True

                