"""Modelo de libro."""

from club_lectura.modelos.material import MaterialBibliografico
from club_lectura.utils.validadores import validar_texto_no_vacio


class Libro(MaterialBibliografico):
    """Material bibliografico de tipo libro, identificado tambien por ISBN."""

    def __init__(self, titulo, autor, genero, nivel, paginas, isbn):
        """Crea un libro con los datos comunes y su ISBN."""
        super().__init__(titulo, autor, genero, nivel, paginas)
        self.isbn = isbn

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, valor: str) -> None:
        """Valida que el ISBN no este vacio."""
        self._isbn = validar_texto_no_vacio(valor, "isbn")

    def descripcion_corta(self) -> str:
        """Devuelve una descripcion resumida para mensajes de confirmacion."""
        return f"Libro: {self.titulo}, ISBN: {self.isbn}"
