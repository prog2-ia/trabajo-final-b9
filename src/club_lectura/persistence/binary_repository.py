import pickle
from pathlib import Path


class BinaryRepository:
    def __init__(self, ruta_fichero: str = "data/club_lectura.bin") -> None:
        self.ruta_fichero = Path(ruta_fichero)

    def guardar(self, materiales: list, bibliografias: list, sesiones: list) -> None:
        self.ruta_fichero.parent.mkdir(parents=True, exist_ok=True)

        datos = {
            "materiales": materiales,
            "bibliografias": bibliografias,
            "sesiones": sesiones,
        }

        with open(self.ruta_fichero, "wb") as fichero:
            pickle.dump(datos, fichero)

    def cargar(self) -> tuple[list, list, list]:
        if not self.ruta_fichero.exists():
            return [], [], []

        with open(self.ruta_fichero, "rb") as fichero:
            datos = pickle.load(fichero)

        return (
            datos.get("materiales", []),
            datos.get("bibliografias", []),
            datos.get("sesiones", []),
        )