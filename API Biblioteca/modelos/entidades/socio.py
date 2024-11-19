from datetime import date

class Socio:
    @classmethod
    def fromDic(cls, data: dict) -> 'Socio':
        if not isinstance(data, dict):
            raise ValueError('El dato ingresado debe ser un Diccionario.')
        data["fecha_nacimiento"] = date.fromisoformat(data["fecha_nacimiento"])
        return cls(data["dni"], data["nombre"], data["apellido"], data["mail"], data["fecha_nacimiento"])
    
    
    def __init__(self, dni: int, nombre: str, apellido: str, mail: str, fecha_nacimiento: date) -> None:
        if not isinstance(dni, int) or dni < 1:
            raise TypeError('El dni debe ser de tipo entero mayor a 1.')
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError('El nombre debe ser de tipo string no vacio.')
        if not isinstance(apellido, str) or apellido.isspace() or apellido == "":
            raise TypeError('El apellido debe ser de tipo string no vacio.')
        if not isinstance(mail, str) or mail.isspace() or mail == "":
            raise TypeError('El mail debe ser de tipo string no vacio.')
        if not isinstance(fecha_nacimiento, date):
            raise TypeError('La fecha de nacimiento debe ser de tipo date.')
        self.__DNI = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__fecha_nacimiento = fecha_nacimiento

    def establecerNombre(self, nombre: str):
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError('El nombre debe ser de tipo string no vacio.')
        self.__nombre = nombre

    def establecerApellido(self, apellido: str):
        if not isinstance(apellido, str) or apellido.isspace() or apellido == "":
            raise TypeError('El apellido debe ser de tipo string no vacio.')
        self.__apellido = apellido
        
    def establecerMail(self, mail: str):
        if not isinstance(mail, str) or mail.isspace() or mail == "":
            raise TypeError('El mail debe ser de tipo string no vacio.')
        self.__mail = mail

    def establecerFecha(self, fecha_nacimiento: date):
        if not isinstance(fecha_nacimiento, date):
            raise TypeError('La fecha de nacimiento debe ser de tipo date.')
        self.__fecha_nacimiento = fecha_nacimiento

    def obtenerDNI(self) -> int:
        return self.__DNI
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerApellido(self) -> str:
        return self.__apellido
    
    def obtenerMail(self) -> str:
        return self.__mail
    
    def obtenerFecha(self) -> date:
        return self.__fecha_nacimiento

    def esIgual(self, otro: 'Socio') -> bool:
        if not isinstance(otro, Socio):
            raise TypeError('El dato ingresado debe ser de la clase Socio.')
        return self.__DNI == otro.obtenerDNI() and self.__nombre == otro.obtenerNombre() and self.__apellido == otro.obtenerApellido() and self.__mail == otro.obtenerMail() and self.__fecha_nacimiento == otro.obtenerFecha()
    
    def __str__(self) -> str:
        return f"DNI: {self.__DNI}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Mail: {self.__mail}, Fecha de nacimiento: {self.__fecha_nacimiento}"
    
    def toDic(self) -> dict:
        return {"dni" : self.__DNI, "nombre" : self.__nombre, "apellido" : self.__apellido, "mail" : self.__mail, "fecha_nacimiento" : self.__fecha_nacimiento.isoformat()}
        