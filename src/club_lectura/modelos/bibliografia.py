from __future__ import annotations

from club_lectura.exceptions.errors import DuplicadoError
from club_lectura.utils.validadores import validar_texto_no_vacio


class Bibliografia:
    def __init__(self, nombre: str) -> None:
        self.nombre = validar_texto_no_vacio(nombre, "nombre")
        self._materiales = []

    @property
    def materiales(self) -> list:
        return self._materiales.copy()

    def agregar_material(self, material) -> None:
        if any(existing.id == material.id for existing in self._materiales):
            raise DuplicadoError(
                f"El material '{material.titulo}' ya existe en la bibliografía '{self.nombre}'."
            )
        self._materiales.append(material)

    def eliminar_material(self, material_id: int) -> None:
        self._materiales = [m for m in self._materiales if m.id != material_id]

    def ordenar_por_prioridad(self) -> list:
        return sorted(self._materiales, reverse=True)

    def __add__(self, other: "Bibliografia") -> "Bibliografia":
        if not isinstance(other, Bibliografia):
            return NotImplemented

        nueva = Bibliografia(f"{self.nombre} + {other.nombre}")
        ids_vistos = set()

        for material in self._materiales + other._materiales:
            if material.id not in ids_vistos:
                nueva._materiales.append(material)
                ids_vistos.add(material.id)

        return nueva

    def __contains__(self, material) -> bool:
        return any(m.id == material.id for m in self._materiales)

    def __len__(self) -> int:
        return len(self._materiales)

    def __iter__(self):
        return iter(self._materiales)

    def __str__(self) -> str:
        return f"Bibliografía '{self.nombre}' con {len(self)} materiales."