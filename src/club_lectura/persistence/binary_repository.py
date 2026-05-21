"""Persistencia binaria usando pickle."""

from __future__ import annotations

import pickle
from pathlib import Path

from club_lectura.exceptions import PersistenciaError
from club_lectura.modelos import MaterialBibliografico


class BinaryRepository:
    """Repositorio que guarda y carga objetos Python en formato binario."""

    def __init__(self, ruta_fichero: str = "data/club_lectura.bin") -> None:
        """Recibe la ruta del fichero binario de trabajo."""
        self.ruta_fichero = Path(ruta_fichero)

    def guardar(self, materiales: list, bibliografias: list, sesiones: list) -> None:
        """Serializa el estado completo usando pickle."""
        try:
            self.ruta_fichero.parent.mkdir(parents=True, exist_ok=True)

            datos = {
                "materiales": materiales,
                "bibliografias": bibliografias,
                "sesiones": sesiones,
            }

            with open(self.ruta_fichero, "wb") as fichero:
                pickle.dump(datos, fichero)

        except (OSError, pickle.PickleError, TypeError) as error:
            raise PersistenciaError(
                "No se han podido guardar los datos en el archivo binario."
            ) from error

    def cargar(self) -> tuple[list, list, list]:
        """Deserializa el estado completo desde pickle."""
        if not self.ruta_fichero.exists():
            return [], [], []

        try:
            with open(self.ruta_fichero, "rb") as fichero:
                datos = pickle.load(fichero)

            if not isinstance(datos, dict):
                raise PersistenciaError(
                    "El archivo binario no tiene el formato esperado."
                )

            materiales = datos.get("materiales", [])
            bibliografias = datos.get("bibliografias", [])
            sesiones = datos.get("sesiones", [])

            self._actualizar_contador_ids(materiales)

            return materiales, bibliografias, sesiones

        except PersistenciaError:
            raise

        except (
            OSError,
            EOFError,
            pickle.PickleError,
            AttributeError,
            TypeError,
            ValueError,
        ) as error:
            raise PersistenciaError(
                "No se han podido cargar los datos desde el archivo binario."
            ) from error

    def _actualizar_contador_ids(self, materiales: list) -> None:
        """Evita repetir ids despues de cargar objetos desde disco."""
        if not materiales:
            MaterialBibliografico._contador_ids = 1
            return

        mayor_id = max(material.id for material in materiales)
        MaterialBibliografico._contador_ids = mayor_id + 1
