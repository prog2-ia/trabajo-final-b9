class ClubLecturaError(Exception):
    """Excepción base del proyecto."""


class DuplicadoError(ClubLecturaError):
    """Se lanza al intentar añadir un elemento ya existente."""


class MetadatoInvalidoError(ClubLecturaError):
    """Se lanza cuando un metadato no cumple las reglas de validación."""


class ValoracionInvalidaError(ClubLecturaError):
    """Se lanza cuando la valoración de una reseña no es válida."""


class ElementoNoEncontradoError(ClubLecturaError):
    """Se lanza cuando no se encuentra un material, bibliografía o sesión."""


class PersistenciaError(ClubLecturaError):
    """Se lanza cuando hay un problema al guardar o cargar datos."""