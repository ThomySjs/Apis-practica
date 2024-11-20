from modelos.repositorios.repositorioAlumnos import RepositorioAlumnos
from modelos.repositorios.repositorioTemas import RepositorioTemas
from modelos.repositorios.repositorioTemaAlumnos import RepositorioTemasAlumnos
from modelos.repositorios.examenesConfirmados import repositorioExamenesConfirmados

repo_temas = None
repo_alumnos = None
repo_ta = None
repo_examenesConfirmados = None

def obtenerRepositorioTemas():
    global repo_temas

    if repo_temas is None:
        repo_temas = RepositorioTemas()
    return repo_temas

def obtenerRepositorioAlumnos():
    global repo_alumnos

    if repo_alumnos is None:
        repo_alumnos = RepositorioAlumnos()
    return repo_alumnos

def obtenerRepositorioTA():
    global repo_ta

    if repo_ta is None:
        repo_ta = RepositorioTemasAlumnos()
    return repo_ta

def obtenerConfirmados():
    global repo_examenesConfirmados

    if repo_examenesConfirmados is None:
        repo_examenesConfirmados = repositorioExamenesConfirmados()
    return repo_examenesConfirmados