from modelos.repositorios.repo_libros import RepositorioLibros


repoLibros= None

def obtenerRepositorioLibros():
    global repoLibros

    if repoLibros is None:
        repoLibros = RepositorioLibros()
    return repoLibros