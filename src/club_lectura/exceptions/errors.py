"""Errores propios del dominio del club de lectura."""


class ClubLecturaError(Exception):
    """Excepcion base del proyecto."""


class DuplicadoError(ClubLecturaError):
    """Se lanza al intentar anadir un elemento ya existente."""


class MetadatoInvalidoError(ClubLecturaError):
    """Se lanza cuando un metadato no cumple las reglas de validacion."""


class ValoracionInvalidaError(ClubLecturaError):
    """Se lanza cuando la valoracion de una resena no es valida."""


class PersistenciaError(ClubLecturaError):
    """Se lanza cuando hay un problema al guardar o cargar datos."""
