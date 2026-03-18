from club_lectura.modelos.material import MaterialBibliografico
from club_lectura.utils.validadores import validar_texto_no_vacio


class Libro(MaterialBibliografico):
    def __init__(self, titulo, autor, genero, nivel, paginas, isbn):
        super().__init__(titulo, autor, genero, nivel, paginas)
        self.isbn = isbn

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, valor: str) -> None:
        self._isbn = validar_texto_no_vacio(valor, "isbn")

    def descripcion_corta(self) -> str:
        return f"Libro: {self.titulo}, ISBN: {self.isbn}"