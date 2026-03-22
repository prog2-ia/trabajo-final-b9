# Club de lectura y bibliografías

Proyecto en Python orientado a objetos para gestionar un club de lectura y construir bibliografías combinables.

## Objetivo

El proyecto ha sido diseñado para aplicar principios de Programación Orientada a Objetos en Python, como:

- clases y objetos
- encapsulación
- herencia
- polimorfismo
- clases abstractas
- modularidad
- sobrecarga de operadores
- excepciones personalizadas

## Funcionalidades principales

- Registro de materiales bibliográficos.
- Distinción entre distintos tipos de lectura:
  - `Libro`
  - `Articulo`
- Gestión de reseñas con valoración numérica.
- Gestión de bibliografías sin duplicados.
- Combinación de bibliografías con el operador `+`.
- Comparación de reseñas por valoración.
- Priorización de lecturas por valoración media.
- Organización de sesiones de lectura.

## Estructura del proyecto

```text
TRABAJO-FINAL-B9/
│
├── src/
│   └── club_lectura/
│       ├── __pycache__/
│       ├── app/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   ├── gestores.py
│       │   ├── io.py
│       │   └── menu.py
│       │
│       ├── enums/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   ├── genero.py
│       │   └── nivel.py
│       │
│       ├── exceptions/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   └── errors.py
│       │
│       ├── modelos/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   ├── articulo.py
│       │   ├── bibliografia.py
│       │   ├── libro.py
│       │   ├── material.py
│       │   ├── resena.py
│       │   └── sesion.py
│       │
│       ├── utils/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   └── validadores.py
│       │
│       └── __init__.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Uso

El proyecto se ejecuta desde el archivo principal `main.py`, que despliega un menú interactivo en consola desde el que se pueden gestionar las distintas funcionalidades del sistema.

Para ejecutarlo:

```bash
python main.py
```

Una vez iniciado, aparecerá un menú de texto en la terminal con opciones para:

- añadir libros y artículos
- ver materiales
- crear bibliografías
- añadir materiales a bibliografías
- crear reseñas
- consultar valoraciones
- crear sesiones de lectura
- ordenar materiales por prioridad

## Estado actual

Actualmente, el proyecto funciona mediante interacción por consola a través de un menú textual.

## Mejoras futuras

Como ampliación futura del trabajo, se plantea:

- incorporar una base de datos para almacenar de forma persistente los materiales, bibliografías, reseñas y sesiones
- sustituir el menú de texto en consola por una interfaz más visual e intuitiva

## Autoría

Trabajo realizado por Pablo Candela y Blanca Xifra.

## Ejemplo de ejecución

A continuación se muestra un ejemplo de ejecución del programa en consola:

```bash
$ python main.py

=== CLUB DE LECTURA Y BIBLIOGRAFÍAS ===
1. Añadir libro
2. Añadir artículo
3. Ver materiales
4. Crear bibliografía
5. Añadir material a bibliografía
6. Ver bibliografías
7. Añadir reseña
8. Ver reseñas y valoración media de un material
9. Crear sesión de lectura
10. Ver sesiones
11. Ver materiales ordenados por prioridad
0. Salir

Elige una opción: 1

=== AÑADIR LIBRO ===
Título: Los pilares de la tierra
Autor: Ken Follett

Géneros disponibles:
1. Novela
2. Ensayo
3. Ciencia ficción
4. Fantasía
5. Historia
6. Poesía
7. Divulgación

Selecciona un género: 1
Número de páginas: 1040
Nivel de lectura: alto

Libro añadido correctamente.
'''

