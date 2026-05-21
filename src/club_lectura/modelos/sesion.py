"""Modelo de sesion de lectura."""

from datetime import datetime

from club_lectura.utils.validadores import validar_texto_no_vacio


class SesionLectura:
    """Sesion programada para comentar un material concreto."""

    def __init__(self, fecha: datetime, material, moderador: str) -> None:
        """Crea la sesion con fecha, material y moderador."""
        self.fecha = fecha
        self.material = material
        self.moderador = validar_texto_no_vacio(moderador, "moderador")
        self._asistentes = []

    @property
    def asistentes(self) -> list:
        """Devuelve una copia de asistentes para proteger la lista interna."""
        return self._asistentes.copy()

    def agregar_asistente(self, nombre: str) -> None:
        """Anade un asistente si no estaba ya registrado."""
        nombre = validar_texto_no_vacio(nombre, "asistente")
        if nombre not in self._asistentes:
            self._asistentes.append(nombre)

    def resumen(self) -> str:
        """Construye el texto resumen usado al mostrar la sesion."""
        return (
            f"Sesión del {self.fecha.strftime('%d/%m/%Y %H:%M')} sobre '{self.material.titulo}'. "
            f"Moderador: {self.moderador}. Asistentes: {len(self._asistentes)}."
        )

    def __str__(self) -> str:
        """Representacion legible para listados del menu."""
        return self.resumen()
