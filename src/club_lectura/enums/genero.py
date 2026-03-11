from enum import Enum

class Genero(Enum):
    """
    Esta clase sirve para definir los géneros que puede tener un material bibliográfico.

    Se usa para que no se escriban los géneros de cualquier manera como texto libre,
    y así mantener todos los datos más ordenados y sin errores.
    """

    NOVELA = "Novela"
    ENSAYO = "Ensayo"
    CIENCIA_FICCION = "Ciencia ficción"
    FANTASIA = "Fantasía"
    HISTORIA = "Historia"
    POESIA = "Poesía"
    DIVULGACION = "Divulgación"
    OTRO = "Otro"