"""Funciones auxiliares para leer y mostrar datos por consola."""

from club_lectura.enums import Genero, Nivel


def pedir_texto(mensaje: str) -> str:
    """Pide texto por consola y elimina espacios sobrantes."""
    return input(mensaje).strip()


def pedir_entero(mensaje: str) -> int:
    """Pide un entero hasta que el usuario introduce un valor valido."""
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Debes introducir un número entero.")


def elegir_genero():
    """Muestra los generos disponibles y devuelve el elegido."""
    generos = list(Genero)

    print("\nGéneros disponibles:")
    for i, genero in enumerate(generos, start=1):
        print(f"{i}. {genero.value}")

    while True:
        opcion = pedir_entero("Elige un género: ")
        if 1 <= opcion <= len(generos):
            return generos[opcion - 1]
        print("Opción no válida.")


def elegir_nivel():
    """Muestra los niveles disponibles y devuelve el elegido."""
    niveles = list(Nivel)

    print("\nNiveles disponibles:")
    for i, nivel in enumerate(niveles, start=1):
        print(f"{i}. {nivel.value}")

    while True:
        opcion = pedir_entero("Elige un nivel: ")
        if 1 <= opcion <= len(niveles):
            return niveles[opcion - 1]
        print("Opción no válida.")


def mostrar_materiales(materiales: list) -> None:
    """Imprime los materiales registrados o avisa si no hay ninguno."""
    if not materiales:
        print("\nNo hay materiales registrados.")
        return

    print("\nMateriales registrados:")
    for i, material in enumerate(materiales, start=1):
        print(f"{i}. {material}")


def seleccionar_material(materiales: list):
    """Permite elegir un material por posicion dentro de una lista."""
    if not materiales:
        print("\nNo hay materiales disponibles.")
        return None

    mostrar_materiales(materiales)
    opcion = pedir_entero("Selecciona un material: ")

    if 1 <= opcion <= len(materiales):
        return materiales[opcion - 1]

    print("Selección no válida.")
    return None


def mostrar_bibliografias(bibliografias: list) -> None:
    """Imprime las bibliografias registradas o avisa si no hay ninguna."""
    if not bibliografias:
        print("\nNo hay bibliografías registradas.")
        return

    print("\nBibliografías registradas:")
    for i, bibliografia in enumerate(bibliografias, start=1):
        print(f"{i}. {bibliografia}")


def seleccionar_bibliografia(bibliografias: list):
    """Permite elegir una bibliografia por posicion dentro de una lista."""
    if not bibliografias:
        print("\nNo hay bibliografías disponibles.")
        return None

    mostrar_bibliografias(bibliografias)
    opcion = pedir_entero("Selecciona una bibliografía: ")

    if 1 <= opcion <= len(bibliografias):
        return bibliografias[opcion - 1]

    print("Selección no válida.")
    return None
