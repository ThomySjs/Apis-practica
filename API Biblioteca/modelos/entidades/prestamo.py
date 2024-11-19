from datetime import date
import json

class Prestamo:
    ULTIMO_ID = 0
    FILE_PATH = 'datos/prestamos.json'

    @classmethod
    def obtenerNuevoID(cls) -> int:
        cls.ULTIMO_ID += 1
        return cls.ULTIMO_ID

    @classmethod
    def establecerUltimoID(cls):
        try:
            with open(Prestamo.FILE_PATH, 'r') as file:
                data = json.load(file)
                if len(data) < 1:
                    cls.ULTIMO_ID = 0
                else: 
                    cls.ULTIMO_ID = data[-1]["id"]
        except FileNotFoundError:
            print('No se encontro el archivo con los prestamos.')
            cls.ULTIMO_ID = 0
        

    @classmethod
    def fromDic(cls, data: dict) -> 'Prestamo':
        if not isinstance(data, dict):
            raise TypeError('El dato ingresado debe ser un diccionario.')
        data['fecha_retiro'] = date.fromisoformat(data['fecha_retiro'])
        data['fecha_devolucion']= date.fromisoformat(data['fecha_devolucion'])
        return cls(data["id"], data["socio_dni"], data["libro_isbn"], data["fecha_retiro"], data["cant_dias"], data["fecha_devolucion"])


    def __init__(self,id: int, socio_dni: int, libro_isbn: int, fecha_retiro: date, cant_dias: int, fecha_devolucion: date = None) -> None:
        if not isinstance(id, int) or id < 1:
            raise TypeError('El  id debe ser un entero mayor a 1.')
        if not isinstance(socio_dni, int) or socio_dni < 1:
            raise TypeError('El dni debe ser de tipo entero mayor a 1.')
        if not isinstance(libro_isbn, int) or libro_isbn < 1:
            raise TypeError('El ISBN debe ser de tipo entero mayor a 1.')
        if not isinstance(fecha_retiro, date):
            raise TypeError('La fecha de retiro debe ser de tipo date.')
        if not isinstance(cant_dias, int) or cant_dias < 1:
            raise TypeError('La cantidad de dias debe ser de tipo entero mayor a 0.')
        if not isinstance(fecha_devolucion, date):
            raise TypeError('La fecha de devolucion debe ser de tipo date.')
        self.__id = id
        self.__socio_dni = socio_dni
        self.__libro_isbn = libro_isbn
        self.__fecha_retiro = fecha_retiro
        self.__cant_dias = cant_dias
        self.__fecha_devolucion = fecha_devolucion

    def establecerSocioDNI(self, dni: int):
        if not isinstance(dni, int) or dni < 1:
            raise TypeError('El dni debe ser de tipo entero mayor a 1.')
        self.__socio_dni = dni

    def establecerLibroISBN(self, isbn: int):
        if not isinstance(isbn, int) or isbn < 1:
            raise TypeError('El ISBN debe ser de tipo entero mayor a 1.')
        self.__libro_isbn = isbn

    def establecerRetiro(self, fecha: date):
        if not isinstance(fecha, date):
            raise TypeError('La fecha de retiro debe ser de tipo date.')
        self.__fecha_retiro = fecha

    def establecerCantDias(self, dias: int):
        if not isinstance(dias, int) or dias < 1:
            raise TypeError('La cantidad de dias debe ser de tipo entero mayor a 0.')
        self.__cant_dias = dias

    def establecerDevolucion(self, fecha: date):
        if not isinstance(fecha, date):
            raise TypeError('La fecha de retiro debe ser de tipo date.')
        self.__fecha_devolucion = fecha
    
    def obtenerID(self) -> int:
        return self.__id
    
    def obtenerSocioDNI(self) -> int:
        return self.__socio_dni
    
    def obtenerLibroISBN(self) -> int:
        return self.__libro_isbn
    
    def obtenerRetiro(self) -> date:
        return self.__fecha_retiro
    
    def obtenerDevolucion(self) -> date:
        return self.__fecha_devolucion

    def obtenerCantDias(self) -> int:
        return self.__cant_dias
    
    def esIgual(self, otro: 'Prestamo') -> bool:
        if not isinstance(otro, Prestamo):
            raise TypeError('El dato ingresado debe ser de la clase Prestamo.')
        return self.__socio_dni == otro.obtenerSocioDNI() and self.__libro_isbn == otro.obtenerLibroISBN() and self.__fecha_retiro == otro.obtenerRetiro() and self.__cant_dias == otro.obtenerCantDias() and self.__fecha_devolucion == otro.obtenerDevolucion()
    
    def __str__(self) -> str:
        return f"ID: {self.__id}, DNI socio: {self.__socio_dni}, ISBN: {self.__libro_isbn}, Fecha de retiro: {self.__fecha_retiro}, Cantidad de dias: {self.__cant_dias}, Fecha de devolucion: {self.__fecha_devolucion}"
    
    def toDic(self) -> dict:
        return {"id" : self.__id, "socio_dni" : self.__socio_dni, "libro_isbn" : self.__libro_isbn, "fecha_retiro" : self.__fecha_retiro.isoformat(), "cant_dias" : self.__cant_dias, "fecha_devolucion" : self.__fecha_devolucion.isoformat()}
    