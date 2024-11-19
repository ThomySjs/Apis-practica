from modelos.repositorios.repo_libros import RepositorioLibros
from modelos.repositorios.repo_socios import RepositorioSocios
from modelos.repositorios.repo_prestamos import RepositorioPrestamos


repoLibros= None
repoSocios= None
repoPrestamos = None

def obtenerRepositorioLibros():
    global repoLibros

    if repoLibros is None:
        repoLibros = RepositorioLibros()
    return repoLibros

def obtenerRepositorioSocios():
    global repoSocios

    if repoSocios is None:
        repoSocios = RepositorioSocios()
    return repoSocios

def obtenerRepositorioPrestamo():
    global repoPrestamos

    if repoPrestamos is None:
        repoPrestamos = RepositorioPrestamos()
    return repoPrestamos