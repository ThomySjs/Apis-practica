from modelos.entidades.prestamo import Prestamo
import json
from datetime import date

class RepositorioPrestamos:
    FILE_PATH = 'datos/prestamos.json'

    def __init__(self) -> None:
        self.__prestamos = self.__cargarTodos()

    def __cargarTodos(self):
        lista= []
        try:
            with open(self.FILE_PATH, 'r') as file:
                data = json.load(file)
                for prestamo in data:
                    lista.append(Prestamo.fromDic(prestamo))
        except FileNotFoundError:
            print('No se encontro el archivo de los prestamos.')
        
        return lista
    
    def __guardarTodos(self):
        lista = []
        try:
            for prestamo in self.__prestamos:
                lista.append(prestamo.toDic())

            with open(RepositorioPrestamos.FILE_PATH, 'w') as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print('No se encontro el archivo de los prestamos.')

    def obtenerTodos(self) -> list:
        return self.__prestamos
    
    def estaDevuelto(self, prestamo: 'Prestamo') -> bool:
        if not isinstance(prestamo, Prestamo):
            raise TypeError('El prestamo debe ser de la clase Prestamo.')
        for p in self.__prestamos:
            if p.esIgual(prestamo):
                if p.obtenerDevolucion() is None:
                    return False
                else:
                    return True
        return False

    def agregar(self, nuevoPrestamo: 'Prestamo'):
        if not isinstance(nuevoPrestamo, Prestamo):
            raise TypeError('El tipo de dato debe ser de la clase Prestamo.')
        if self.existe(nuevoPrestamo.obtenerSocioDNI(), nuevoPrestamo.obtenerLibroISBN(), nuevoPrestamo.obtenerRetiro()):
            return False
        self.__prestamos.append(nuevoPrestamo)
        self.__guardarTodos()
        return True
        
        
    def existe(self, socio_dni: int, libro_isbn: int, fecha_retiro: date):
        if not isinstance(socio_dni, int) or socio_dni < 1:
            raise TypeError('El dni debe ser de tipo entero mayor a 1.')
        if not isinstance(libro_isbn, int) or libro_isbn < 1:
            raise TypeError('El ISBN debe ser de tipo entero mayor a 1.')
        if not isinstance(fecha_retiro, date):
            raise TypeError('La fecha de retiro debe ser de tipo date.')
        for p in self.__prestamos:
            if p.obtenerSocioDNI()  == socio_dni and p.obtenerLibroISBN() == libro_isbn and p.obtenerRetiro() == fecha_retiro:
                return True
        return False
    
    def obtenerPrestamo(self, socio_dni: int, libro_isbn: int, fecha_retiro: date) -> Prestamo:
        if not isinstance(socio_dni, int) or socio_dni < 1:
            raise TypeError('El dni debe ser de tipo entero mayor a 1.')
        if not isinstance(libro_isbn, int) or libro_isbn < 1:
            raise TypeError('El ISBN debe ser de tipo entero mayor a 1.')
        if not isinstance(fecha_retiro, date):
            raise TypeError('La fecha de retiro debe ser de tipo date.')
        if self.existe(socio_dni, libro_isbn, fecha_retiro):
            for p in self.__prestamos:
                if p.obtenerSocioDNI()  == socio_dni and p.obtenerLibroISBN() == libro_isbn and p.obtenerRetiro() == fecha_retiro:
                    return p
        else:
            return None
        
    def modificarPorID(self, id: int, socio_dni: int, libro_isbn: int, fecha_retiro: date, cant_dias: int, fecha_devolucion: date):
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
        for p in self.__prestamos:
            if p.obtenerID() == id:
                p.establecerSocioDNI(socio_dni)
                p.establecerLibroISBN(libro_isbn)
                p.establecerRetiro(fecha_retiro)
                p.establecerCantDias(cant_dias)
                p.establecerDevolucion(fecha_devolucion)
                self.__guardarTodos()
                return True
        return False        

    def eliminarPorID(self, id: int):    
        if not isinstance(id, int) or id < 1:
            raise TypeError('El  id debe ser un entero mayor a 1.')
        for p in self.__prestamos:
            if p.obtenerID() == id:
                self.__prestamos.remove(p)
                return True
        return False
    
    def cantidadLibrosSinDevolver(self, isbn: int) -> int:
        if not isinstance(isbn, int) or isbn < 1:
            raise TypeError('El isbn debe ser un entero mayor a 0.')
        contador = 0
        for p in self.__prestamos:
            if p.obtenerISBN() == isbn:
                if p.obtenerDevolucion() is None:
                    contador += 1
        return contador
