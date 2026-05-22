"""Modelo base para los materiales bibliograficos."""

from abc import ABC, abstractmethod
from statistics import mean

from club_lectura.enums.genero import Genero
from club_lectura.enums.nivel import Nivel
from club_lectura.exceptions.errors import MetadatoInvalidoError
from club_lectura.utils.validadores import validar_entero_positivo, validar_texto_no_vacio


class MaterialBibliografico(ABC):
    """Clase base para cualquier lectura gestionada por el club."""

    _contador_ids = 1

    def __init__(self, titulo: str, autor: str, genero: Genero, nivel: Nivel, paginas: int) -> None:
        """Inicializa los metadatos comunes y asigna un id autoincremental."""
        self._id = MaterialBibliografico._contador_ids
        MaterialBibliografico._contador_ids += 1

        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.nivel = nivel
        self.paginas = paginas
        self._resenas = []

    @property
    def id(self) -> int:
        """Identificador unico del material."""
        return self._id

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        self._titulo = validar_texto_no_vacio(valor, "titulo")

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, valor: str) -> None:
        self._autor = validar_texto_no_vacio(valor, "autor")

    @property
    def genero(self) -> Genero:
        return self._genero

    @genero.setter
    def genero(self, valor: Genero) -> None:
        if not isinstance(valor, Genero):
            raise MetadatoInvalidoError("El género debe ser una instancia de Genero.")
        self._genero = valor

    @property
    def nivel(self) -> Nivel:
        return self._nivel

    @nivel.setter
    def nivel(self, valor: Nivel) -> None:
        if not isinstance(valor, Nivel):
            raise MetadatoInvalidoError("El nivel debe ser una instancia de Nivel.")
        self._nivel = valor

    @property
    def paginas(self) -> int:
        return self._paginas

    @paginas.setter
    def paginas(self, valor: int) -> None:
        self._paginas = validar_entero_positivo(valor, "paginas")

    @property
    def resenas(self) -> list:
        """Devuelve una copia de las resenas para proteger la lista interna."""
        return self._resenas.copy()

    def agregar_resena(self, resena) -> None:
        """Asocia una nueva resena al material."""
        self._resenas.append(resena)

    def valoracion_media(self) -> float:
        """Calcula la media de valoraciones o 0.0 si no hay resenas."""
        if not self._resenas:
            return 0.0
        return round(mean(resena.valoracion for resena in self._resenas), 2)

    def prioridad(self) -> tuple:
        """Ordena por media alta, nivel mas facil y menor numero de paginas."""
        orden_nivel = {
            Nivel.BASICO: 1,
            Nivel.INTERMEDIO: 2,
            Nivel.AVANZADO: 3,
        }
        return (self.valoracion_media(), -orden_nivel[self.nivel], -self.paginas)

    @abstractmethod
    def descripcion_corta(self) -> str:
        """Devuelve una descripcion breve propia de cada subtipo."""
        pass

    def __lt__(self, other: "MaterialBibliografico") -> bool:
        """Permite ordenar materiales usando la prioridad calculada."""
        if not isinstance(other, MaterialBibliografico):
            return NotImplemented
        return self.prioridad() < other.prioridad()

    def __eq__(self, other: object) -> bool:
        """Dos materiales se consideran iguales si tienen el mismo id."""
        if not isinstance(other, MaterialBibliografico):
            return False
        return self.id == other.id

    def __str__(self) -> str:
        """Representacion legible para listados del menu."""
        return f"{self.titulo} - {self.autor} ({self.genero.value}, {self.nivel.value})"
