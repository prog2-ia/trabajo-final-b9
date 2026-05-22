"""Modelo de bibliografia."""

from club_lectura.exceptions.errors import DuplicadoError
from club_lectura.utils.validadores import validar_texto_no_vacio


class Bibliografia:
    """Agrupa materiales de lectura evitando duplicados por id."""

    def __init__(self, nombre: str) -> None:
        """Crea una bibliografia vacia con un nombre validado."""
        self.nombre = validar_texto_no_vacio(nombre, "nombre")
        self._materiales = []

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

    def __len__(self) -> int:
        """Devuelve cuantos materiales contiene la bibliografia."""
        return len(self._materiales)

    def __iter__(self):
        """Permite recorrer directamente los materiales de la bibliografia."""
        return iter(self._materiales)

    def __str__(self) -> str:
        """Representacion legible para listados del menu."""
        return f"Bibliografía '{self.nombre}' con {len(self)} materiales."
