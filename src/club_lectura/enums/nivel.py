from enum import Enum

class Nivel(Enum):
    """
    Esta clase representa el nivel de dificultad de una lectura.

    Se utiliza para clasificar los materiales según sean más fáciles o más avanzados,
    y para que solo se puedan usar niveles válidos dentro del programa.
    """

    BASICO = "Básico"
    INTERMEDIO = "Intermedio"
    AVANZADO = "Avanzado"