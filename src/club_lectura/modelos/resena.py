"""Modelo de resena."""

from __future__ import annotations

from club_lectura.exceptions.errors import ValoracionInvalidaError
from club_lectura.utils.validadores import validar_texto_no_vacio


class Resena:
    """Opinion valorada de una persona sobre un material."""

    def __init__(self, material, autor_resena: str, valoracion: int, comentario: str) -> None:
        """Crea la resena y la registra automaticamente en el material."""
        self._material = material
        self.autor_resena = autor_resena
        self.valoracion = valoracion
        self.comentario = comentario

        self._material.agregar_resena(self)

    @property
    def material(self):
        """Material al que pertenece la resena."""
        return self._material

    @property
    def autor_resena(self) -> str:
        return self._autor_resena

    @autor_resena.setter
    def autor_resena(self, valor: str) -> None:
        """Valida que el autor de la resena no este vacio."""
        self._autor_resena = validar_texto_no_vacio(valor, "autor_resena")

    @property
    def valoracion(self) -> int:
        return self._valoracion

    @valoracion.setter
    def valoracion(self, valor: int) -> None:
        """Valida que la valoracion sea un entero entre 1 y 5."""
        if not isinstance(valor, int) or not 1 <= valor <= 5:
            raise ValoracionInvalidaError("La valoración debe estar entre 1 y 5.")
        self._valoracion = valor

    @property
    def comentario(self) -> str:
        return self._comentario

    @comentario.setter
    def comentario(self, valor: str) -> None:
        """Valida que el comentario no este vacio."""
        self._comentario = validar_texto_no_vacio(valor, "comentario")

    def __gt__(self, other: "Resena") -> bool:
        """Permite comparar resenas por valoracion."""
        if not isinstance(other, Resena):
            return NotImplemented
        return self.valoracion > other.valoracion

    def __lt__(self, other: "Resena") -> bool:
        """Permite ordenar resenas de menor a mayor valoracion."""
        if not isinstance(other, Resena):
            return NotImplemented
        return self.valoracion < other.valoracion

    def __str__(self) -> str:
        """Representacion legible de la resena para consola."""
        return (
            f"Reseña de {self.autor_resena} sobre '{self.material.titulo}': "
            f"{self.valoracion}/5 - {self.comentario}"
        )
