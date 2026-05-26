"""Rutas de trabajo de la aplicacion."""

import sys
from pathlib import Path


def obtener_ruta_datos(nombre_fichero: str) -> Path:
    """Devuelve la ruta escribible para guardar datos de la aplicacion."""
    if getattr(sys, "frozen", False):
        base = Path(sys.executable).resolve().parent
    else:
        base = Path(__file__).resolve().parents[3]

    return base / "data" / nombre_fichero
