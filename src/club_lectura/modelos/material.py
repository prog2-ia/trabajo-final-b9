from __future__ import annotations

from abc import ABC, abstractmethod
from statistics import mean

from club_lectura.enums.genero import Genero
from club_lectura.enums.nivel import Nivel
from club_lectura.exceptions.errors import MetadatoInvalidoError
from club_lectura.utils.validadores import validar_entero_positivo, validar_texto_no_vacio


class MaterialBibliografico(ABC):
    _contador_ids = 1

    def __init__(self, titulo: str, autor: str, genero: Genero, nivel: Nivel, paginas: int) -> None:
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
        return self._resenas.copy()

    def agregar_resena(self, resena) -> None:
        self._resenas.append(resena)

    def valoracion_media(self) -> float:
        if not self._resenas:
            return 0.0
        return round(mean(resena.valoracion for resena in self._resenas), 2)

    def prioridad(self) -> tuple:
        """
        Cuanto mayor sea la valoración media y menor el nivel de dificultad,
        más prioritario será el título.
        """
        orden_nivel = {
            Nivel.BASICO: 1,
            Nivel.INTERMEDIO: 2,
            Nivel.AVANZADO: 3,
        }
        return (self.valoracion_media(), -orden_nivel[self.nivel], -self.paginas)

    @abstractmethod
    def descripcion_corta(self) -> str:
        pass

    def __lt__(self, other: "MaterialBibliografico") -> bool:
        if not isinstance(other, MaterialBibliografico):
            return NotImplemented
        return self.prioridad() < other.prioridad()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MaterialBibliografico):
            return False
        return self.id == other.id

    def __str__(self) -> str:
        return f"{self.titulo} - {self.autor} ({self.genero.value}, {self.nivel.value})"