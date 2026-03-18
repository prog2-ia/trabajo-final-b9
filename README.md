# Club de lectura y bibliografías

Proyecto en Python orientado a objetos para gestionar un club de lectura. Permite registrar materiales de lectura, organizar sesiones, crear reseñas y construir bibliografías combinables.

## Objetivo

El proyecto ha sido diseñado para aplicar principios de Programación Orientada a Objetos en Python:

- clases y objetos,
- encapsulación,
- herencia,
- polimorfismo,
- clases abstractas,
- modularidad,
- sobrecarga de operadores,
- excepciones personalizadas.

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
club-lectura/
│
├── main.py
├── requirements.txt
├── README.md
│
└── src/
    └── club_lectura/
        ├── enums/
        ├── exceptions/
        ├── models/
        └── utils/