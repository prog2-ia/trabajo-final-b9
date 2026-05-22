"""Modelo de bibliografia."""

from club_lectura.exceptions.errors import DuplicadoError
from club_lectura.utils.validadores import validar_texto_no_vacio


class Bibliografia:
    """Agrupa materiales de lectura evitando duplicados por id."""

    def __init__(self, nombre: str) -> None:
        """Crea una bibliografia vacia con un nombre validado."""
        self.nombre = validar_texto_no_vacio(nombre, "nombre")
        self._materiales = []

    @property
    def materiales(self) -> list:
        """Devuelve una copia de los materiales para proteger la lista interna."""
        return self._materiales.copy()

    def agregar_material(self, material) -> None:
        """Anade un material si no esta ya incluido en la bibliografia."""
        if any(existing.id == material.id for existing in self._materiales):
            raise DuplicadoError(
                f"El material '{material.titulo}' ya existe en la bibliografía '{self.nombre}'."
            )
        self._materiales.append(material)

    def eliminar_material(self, material_id: int) -> None:
        """Elimina por id todas las referencias al material indicado."""
        self._materiales = [m for m in self._materiales if m.id != material_id]

    def ordenar_por_prioridad(self) -> list:
        """Devuelve los materiales ordenados por la prioridad del modelo."""
        return sorted(self._materiales, reverse=True)

    def __add__(self, other: "Bibliografia") -> "Bibliografia":
        """Combina dos bibliografias sin duplicar materiales."""
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
        """Permite usar `material in bibliografia` comparando por id."""
        return any(m.id == material.id for m in self._materiales)

    def __len__(self) -> int:
        """Devuelve cuantos materiales contiene la bibliografia."""
        return len(self._materiales)

    def __iter__(self):
        """Permite recorrer directamente los materiales de la bibliografia."""
        return iter(self._materiales)

    def __str__(self) -> str:
        """Representacion legible para listados del menu."""
        return f"Bibliografía '{self.nombre}' con {len(self)} materiales."
