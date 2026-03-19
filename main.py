from datetime import datetime
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from club_lectura.enums import Genero, Nivel
from club_lectura.exceptions import DuplicadoError, ValoracionInvalidaError
from club_lectura.models import Articulo, Bibliografia, Libro, Resena, SesionLectura


def main():
    print("=== CLUB DE LECTURA Y BIBLIOGRAFÍAS ===\n")

    libro1 = Libro(
        titulo="1984",
        autor="George Orwell",
        genero=Genero.CIENCIA_FICCION,
        nivel=Nivel.INTERMEDIO,
        paginas=328,
        isbn="978-0451524935",
    )

    libro2 = Libro(
        titulo="Sapiens",
        autor="Yuval Noah Harari",
        genero=Genero.HISTORIA,
        nivel=Nivel.AVANZADO,
        paginas=496,
        isbn="978-8499924214",
    )

    articulo1 = Articulo(
        titulo="La lectura en la era digital",
        autor="Ana Pérez",
        genero=Genero.ENSAYO,
        nivel=Nivel.BASICO,
        paginas=18,
        revista="Revista de Humanidades",
        doi="10.1234/lectura.2026.001",
    )

    print("Materiales creados:")
    print(libro1.descripcion_corta())
    print(libro2.descripcion_corta())
    print(articulo1.descripcion_corta())
    print()

    bib_novela = Bibliografia("Bibliografía narrativa")
    bib_novela.agregar_material(libro1)

    bib_academica = Bibliografia("Bibliografía académica")
    bib_academica.agregar_material(libro2)
    bib_academica.agregar_material(articulo1)

    bibliografia_total = bib_novela + bib_academica

    print(bib_novela)
    print(bib_academica)
    print(bibliografia_total)
    print()

    print("Contenido de la bibliografía combinada:")
    for material in bibliografia_total:
        print("-", material)
    print()

    r1 = Resena(libro1, "Óscar", 5, "Una lectura inquietante y muy vigente.")
    r2 = Resena(libro2, "Blanca", 4, "Muy interesante, aunque denso por momentos.")
    r3 = Resena(articulo1, "Carlos", 3, "Correcto, pero algo breve.")

    print("Reseñas registradas:")
    print(r1)
    print(r2)
    print(r3)
    print()

    print("Comparación de reseñas:")
    print(f"¿La reseña de '1984' es mejor que la de 'Sapiens'? {r1 > r2}")
    print()

    print("Valoraciones medias:")
    print(f"{libro1.titulo}: {libro1.valoracion_media()}")
    print(f"{libro2.titulo}: {libro2.valoracion_media()}")
    print(f"{articulo1.titulo}: {articulo1.valoracion_media()}")
    print()

    sesion = SesionLectura(
        fecha=datetime(2026, 3, 20, 18, 30),
        material=libro1,
        moderador="Blanca",
    )
    sesion.agregar_asistente("Óscar")
    sesion.agregar_asistente("Carlos")
    sesion.agregar_asistente("Óscar")

    print("Sesión creada:")
    print(sesion)
    print()

    print("Materiales ordenados por prioridad:")
    for material in bibliografia_total.ordenar_por_prioridad():
        print(f"- {material.titulo} | media={material.valoracion_media()} | nivel={material.nivel.value}")
    print()

    print("Probando excepciones:")
    try:
        bib_novela.agregar_material(libro1)
    except DuplicadoError as e:
        print("Duplicado capturado:", e)

    try:
        Resena(libro1, "Lucía", 7, "Esto debería fallar.")
    except ValoracionInvalidaError as e:
        print("Valoración inválida capturada:", e)


if __name__ == "__main__":
    main()