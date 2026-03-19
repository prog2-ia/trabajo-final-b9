from datetime import datetime

from club_lectura.utils.validadores import validar_texto_no_vacio


class SesionLectura:
    def __init__(self, fecha: datetime, material, moderador: str) -> None:
        self.fecha = fecha
        self.material = material
        self.moderador = validar_texto_no_vacio(moderador, "moderador")
        self._asistentes = []

    @property
    def asistentes(self) -> list:
        return self._asistentes.copy()

    def agregar_asistente(self, nombre: str) -> None:
        nombre = validar_texto_no_vacio(nombre, "asistente")
        if nombre not in self._asistentes:
            self._asistentes.append(nombre)

    def resumen(self) -> str:
        return (
            f"Sesión del {self.fecha.strftime('%d/%m/%Y %H:%M')} sobre '{self.material.titulo}'. "
            f"Moderador: {self.moderador}. Asistentes: {len(self._asistentes)}."
        )

    def __str__(self) -> str:
        return self.resumen()