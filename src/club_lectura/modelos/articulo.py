"""Modelo de articulo."""

from club_lectura.modelos.material import MaterialBibliografico
from club_lectura.utils.validadores import validar_texto_no_vacio


class Articulo(MaterialBibliografico):
    """Material bibliografico publicado en una revista o medio academico."""

    def __init__(self, titulo, autor, genero, nivel, paginas, revista, doi=None):
        """Crea un articulo con revista obligatoria y DOI opcional."""
        super().__init__(titulo, autor, genero, nivel, paginas)
        self.revista = revista
        self.doi = doi

    @property
    def revista(self) -> str:
        return self._revista

    @revista.setter
    def revista(self, valor: str) -> None:
        """Valida que la revista no este vacia."""
        self._revista = validar_texto_no_vacio(valor, "revista")

    @property
    def doi(self) -> str | None:
        return self._doi

    @doi.setter
    def doi(self, valor: str | None) -> None:
        """Guarda el DOI si existe; permite None cuando no se conoce."""
        if valor is None:
            self._doi = None
        else:
            self._doi = validar_texto_no_vacio(valor, "doi")

    def descripcion_corta(self) -> str:
        """Devuelve una descripcion breve, incluyendo DOI solo si existe."""
        base = f"Artículo: {self.titulo}, revista: {self.revista}"
        if self.doi:
            base += f", DOI: {self.doi}"
        return base
