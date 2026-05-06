from datetime import datetime

from club_lectura.exceptions import (
    DuplicadoError,
    MetadatoInvalidoError,
    ValoracionInvalidaError,
)
from club_lectura.modelos import Articulo, Bibliografia, Libro, Resena, SesionLectura

from .io import (
    elegir_genero,
    elegir_nivel,
    mostrar_bibliografias,
    mostrar_materiales,
    pedir_entero,
    pedir_texto,
    seleccionar_bibliografia,
    seleccionar_material,
)

from club_lectura.persistence import JsonRepository
from club_lectura.persistence import BinaryRepository
from club_lectura.exceptions import PersistenciaError


materiales = []
bibliografias = []
sesiones = []


def agregar_libro() -> None:
    print("\n=== AÑADIR LIBRO ===")
    titulo = pedir_texto("Título: ")
    autor = pedir_texto("Autor: ")
    genero = elegir_genero()
    nivel = elegir_nivel()
    paginas = pedir_entero("Número de páginas: ")
    isbn = pedir_texto("ISBN: ")

    try:
        libro = Libro(
            titulo=titulo,
            autor=autor,
            genero=genero,
            nivel=nivel,
            paginas=paginas,
            isbn=isbn,
        )
        materiales.append(libro)
        print(f"\nLibro añadido correctamente: {libro.descripcion_corta()}")
    except MetadatoInvalidoError as e:
        print(f"\nError al crear el libro: {e}")


def agregar_articulo() -> None:
    print("\n=== AÑADIR ARTÍCULO ===")
    titulo = pedir_texto("Título: ")
    autor = pedir_texto("Autor: ")
    genero = elegir_genero()
    nivel = elegir_nivel()
    paginas = pedir_entero("Número de páginas: ")
    revista = pedir_texto("Revista: ")
    doi = pedir_texto("DOI: ")

    try:
        articulo = Articulo(
            titulo=titulo,
            autor=autor,
            genero=genero,
            nivel=nivel,
            paginas=paginas,
            revista=revista,
            doi=doi,
        )
        materiales.append(articulo)
        print(f"\nArtículo añadido correctamente: {articulo.descripcion_corta()}")
    except MetadatoInvalidoError as e:
        print(f"\nError al crear el artículo: {e}")


def ver_materiales() -> None:
    mostrar_materiales(materiales)


def crear_bibliografia() -> None:
    print("\n=== CREAR BIBLIOGRAFÍA ===")
    nombre = pedir_texto("Nombre de la bibliografía: ")

    try:
        bibliografia = Bibliografia(nombre)
        bibliografias.append(bibliografia)
        print(f"\nBibliografía creada correctamente: {bibliografia}")
    except MetadatoInvalidoError as e:
        print(f"\nError al crear la bibliografía: {e}")


def agregar_material_a_bibliografia():
    print("\n=== AÑADIR MATERIAL A BIBLIOGRAFÍA ===")
    bibliografia = seleccionar_bibliografia(bibliografias)
    if bibliografia is None:
        return

    material = seleccionar_material(materiales)
    if material is None:
        return

    try:
        bibliografia.agregar_material(material)
        print(f"\n'{material.titulo}' añadido a la bibliografía.")
    except DuplicadoError as e:
        print(f"\nNo se pudo añadir: {e}")


def ver_bibliografias():
    mostrar_bibliografias(bibliografias)

    if not bibliografias:
        return

    ver_contenido = pedir_texto(
        "\n¿Quieres ver el contenido de alguna bibliografía? (s/n): "
    ).lower()

    if ver_contenido != "s":
        return

    bibliografia = seleccionar_bibliografia(bibliografias)
    if bibliografia is None:
        return

    print("\nContenido de la bibliografía:")
    if len(bibliografia) == 0:
        print("No tiene materiales.")
        return

    for material in bibliografia:
        print(f"- {material}")


def agregar_resena():
    print("\n=== AÑADIR RESEÑA ===")
    material = seleccionar_material(materiales)
    if material is None:
        return

    autor = pedir_texto("Autor de la reseña: ")
    valoracion = pedir_entero("Valoración (1-5): ")
    comentario = pedir_texto("Comentario: ")

    try:
        resena = Resena(material, autor, valoracion, comentario)
        print(f"\nReseña añadida correctamente: {resena}")
    except ValoracionInvalidaError as e:
        print(f"\nError al añadir la reseña: {e}")
    except MetadatoInvalidoError as e:
        print(f"\nError al añadir la reseña: {e}")


def ver_resenas_y_media():
    print("\n=== VER RESEÑAS Y VALORACIÓN MEDIA ===")
    material = seleccionar_material(materiales)
    if material is None:
        return

    print(f"\nMaterial: {material}")
    print(f"Valoración media: {material.valoracion_media()}")

    if not material.resenas:
        print("No tiene reseñas todavía.")
        return

    print("\nReseñas:")
    for resena in material.resenas:
        print(f"- {resena}")


def crear_sesion():
    print("\n=== CREAR SESIÓN DE LECTURA ===")
    material = seleccionar_material(materiales)
    if material is None:
        return

    fecha_texto = pedir_texto("Fecha y hora (dd/mm/yyyy HH:MM): ")
    moderador = pedir_texto("Moderador: ")

    try:
        fecha = datetime.strptime(fecha_texto, "%d/%m/%Y %H:%M")
    except ValueError:
        print("\nFormato de fecha incorrecto. Usa dd/mm/yyyy HH:MM")
        return

    try:
        sesion = SesionLectura(
            fecha=fecha,
            material=material,
            moderador=moderador,
        )
    except MetadatoInvalidoError as e:
        print(f"\nError al crear la sesión: {e}")
        return

    while True:
        asistente = pedir_texto("Añade un asistente (Enter para terminar): ")
        if asistente == "":
            break
        sesion.agregar_asistente(asistente)

    sesiones.append(sesion)
    print("\nSesión creada correctamente:")
    print(sesion)


def ver_sesiones():
    if not sesiones:
        print("\nNo hay sesiones registradas.")
        return

    print("\nSesiones registradas:")
    for i, sesion in enumerate(sesiones, start=1):
        print(f"{i}. {sesion}")


def ver_materiales_ordenados():
    if not materiales:
        print("\nNo hay materiales registrados.")
        return

    print("\n=== MATERIALES ORDENADOS POR PRIORIDAD ===")
    for material in sorted(materiales, reverse=True):
        print(
            f"- {material.titulo} | media={material.valoracion_media()} | "
            f"nivel={material.nivel.value}"
        )

def eliminar_material():
    if not materiales:
        print("\nNo hay materiales para eliminar.")
        return

    print("\nMateriales disponibles:")
    for material in materiales:
        print(f"{material.id}. {material.titulo} - {material.autor}")

    try:
        material_id = int(input("\nIntroduce el ID del material que quieres eliminar: "))
    except ValueError:
        print("\nEl ID debe ser un número.")
        return

    material_a_eliminar = None

    for material in materiales:
        if material.id == material_id:
            material_a_eliminar = material
            break

    if material_a_eliminar is None:
        print("\nNo existe ningún material con ese ID.")
        return

    materiales.remove(material_a_eliminar)

    for bibliografia in bibliografias:
        bibliografia.eliminar_material(material_id)

    print(f"\nMaterial eliminado correctamente: {material_a_eliminar.titulo}")

def guardar_datos_json() -> None:
    repositorio = JsonRepository("data/club_lectura.json")
    repositorio.guardar(materiales, bibliografias, sesiones)

    print("\nDatos guardados correctamente en data/club_lectura.json.")


def cargar_datos_json() -> None:
    repositorio = JsonRepository("data/club_lectura.json")

    try:
        materiales_cargados, bibliografias_cargadas, sesiones_cargadas = repositorio.cargar()

        materiales.clear()
        bibliografias.clear()
        sesiones.clear()

        materiales.extend(materiales_cargados)
        bibliografias.extend(bibliografias_cargadas)
        sesiones.extend(sesiones_cargadas)

        print("\nDatos cargados correctamente desde data/club_lectura.json.")
        print(f"Materiales cargados: {len(materiales)}")
        print(f"Bibliografías cargadas: {len(bibliografias)}")
        print(f"Sesiones cargadas: {len(sesiones)}")

    except PersistenciaError as error:
        print(f"\nError de persistencia: {error}")

def guardar_datos_binario() -> None:
    repositorio = BinaryRepository("data/club_lectura.bin")
    repositorio.guardar(materiales, bibliografias, sesiones)

    print("\nDatos guardados correctamente en formato binario.")


def cargar_datos_binario() -> None:
    repositorio = BinaryRepository("data/club_lectura.bin")

    materiales_cargados, bibliografias_cargadas, sesiones_cargadas = repositorio.cargar()

    materiales.clear()
    bibliografias.clear()
    sesiones.clear()

    materiales.extend(materiales_cargados)
    bibliografias.extend(bibliografias_cargadas)
    sesiones.extend(sesiones_cargadas)

    print("\nDatos cargados correctamente desde fichero binario.")
    print(f"Materiales cargados: {len(materiales)}")
    print(f"Bibliografías cargadas: {len(bibliografias)}")
    print(f"Sesiones cargadas: {len(sesiones)}")