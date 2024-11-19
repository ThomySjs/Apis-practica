import json
from modelos.entidades.socio import Socio
from datetime import date

class RepositorioSocios:
    FILE_PATH = 'datos/socios.json'

    def __init__(self) -> None:
        self.__socios = self.__cargarTodos()

    def __cargarTodos(self) -> list:
        lista = []
        try:
            with open(RepositorioSocios.FILE_PATH, 'r') as file:
                socios = json.load(file)
                for s in socios:
                    lista.append(Socio.fromDic(s))
        except FileNotFoundError:
            print('No se ha encontrado el archivo.')
        
        return lista
    
    def __guardarTodos(self):
        lista = [] 
        try: 
            for s in self.__socios:
                lista.append(s.toDic())

            with open(RepositorioSocios.FILE_PATH, 'w') as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print('No se ha encontrado el archivo para guardar los datos.')

    def obtenerTodos(self):
        return self.__socios

    def existe(self, socio: 'Socio') -> bool:
        if not isinstance(socio, Socio):
            raise TypeError('El tipo de dato debe pertenecer a la clase Socio.')
        for s in self.__socios:
            if s.esIgual(socio):
                return True
            
        return False
    
    def existeDNI(self, dni: int) -> bool:
        if not isinstance(dni, int) or dni < 1:
            raise TypeError('El tipo de dato debe ser un entero mayor a 1.')
        for s in self.__socios:
            if s.obtenerDNI() == dni:
                return True
        return False
    
    def obtenerPorDNI(self, dni: int) -> Socio:
        if not isinstance(dni, int) or dni < 1:
            raise TypeError('El tipo de dato debe ser un entero mayor a 1.')
        for s in self.__socios:
            if s.obtenerDNI() == dni:
                return s
        return None
    
    def agregar(self, nuevoSocio: 'Socio'):
        if not isinstance(nuevoSocio, Socio):
            raise TypeError('El dato ingresado debe pertenecer a la clase Socio.')
        if self.existe(nuevoSocio):
            return False
        
        self.__socios.append(nuevoSocio)
        self.__guardarTodos()
        return True
    
    def modificarPorDNI(self, dni: int, nombre: str, apellido: str, mail: str, fecha_nacimiento: date):
        if not isinstance(dni, int) or dni < 1:
            raise TypeError('El dni debe ser de tipo entero mayor a 1.')
        for socio in self.__socios:
            if socio.obtenerDNI() == dni:
                socio.establecerNombre(nombre)
                socio.establecerApellido(apellido)
                socio.establecerMail(mail)
                socio.establecerFecha(date.fromisoformat(fecha_nacimiento))
                self.__guardarTodos()
                return True
        return False
    
    def eliminarPorDNI(self, dni: int):
        if not isinstance(dni, int) or dni < 1:
            raise TypeError('El dni debe ser de tipo entero mayor a 1.')
        if self.existeDNI(dni):
            for s in self.__socios:
                if s.obtenerDNI() == dni:
                    self.__socios.remove(s)
                    self.__guardarTodos()
                    return True
        return False


