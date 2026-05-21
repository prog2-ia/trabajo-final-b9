"""Validadores reutilizables para datos introducidos por el usuario."""

from club_lectura.exceptions.errors import MetadatoInvalidoError


def validar_texto_no_vacio(valor: str, campo: str) -> str:
    """Devuelve el texto limpio o lanza error si esta vacio."""
    if not isinstance(valor, str) or not valor.strip():
        raise MetadatoInvalidoError(f"El campo '{campo}' no puede estar vacío.")
    return valor.strip()


def validar_entero_positivo(valor: int, campo: str) -> int:
    """Valida que el valor sea un entero positivo."""
    if not isinstance(valor, int) or valor <= 0:
        raise MetadatoInvalidoError(f"El campo '{campo}' debe ser un entero positivo.")
    return valor
