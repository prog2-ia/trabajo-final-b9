# Club de lectura y bibliografias

Proyecto en Python orientado a objetos para gestionar materiales de lectura, resenas, bibliografias y sesiones de un club de lectura mediante un menu de consola.

## Objetivo

El proyecto aplica conceptos de Programacion Orientada a Objetos:

- clases y objetos
- encapsulacion
- herencia
- polimorfismo
- clases abstractas
- modularidad
- sobrecarga de operadores
- excepciones personalizadas
- persistencia en ficheros JSON y binarios

## Funcionalidades

- Registrar libros y articulos.
- Ver todos los materiales guardados.
- Crear bibliografias.
- Anadir materiales a bibliografias evitando duplicados.
- Consultar bibliografias y su contenido.
- Anadir resenas con valoracion entre 1 y 5.
- Consultar resenas y valoracion media de cada material.
- Crear sesiones de lectura con fecha, moderador y asistentes.
- Ver sesiones registradas.
- Ordenar materiales por prioridad.
- Eliminar materiales.
- Guardar y cargar datos en formato JSON.
- Guardar y cargar datos en formato binario.

## Estructura

```text
trabajo-final-b9/
|-- main.py
|-- README.md
|-- requirements.txt
|-- data/
|   |-- club_lectura.json
|   `-- club_lectura.bin
`-- src/
    `-- club_lectura/
        |-- app/
        |   |-- gestores.py
        |   |-- io.py
        |   `-- menu.py
        |-- enums/
        |   |-- genero.py
        |   `-- nivel.py
        |-- exceptions/
        |   `-- errors.py
        |-- modelos/
        |   |-- articulo.py
        |   |-- bibliografia.py
        |   |-- libro.py
        |   |-- material.py
        |   |-- resena.py
        |   `-- sesion.py
        |-- persistence/
        |   |-- binary_repository.py
        |   `-- json_repository.py
        `-- utils/
            `-- validadores.py
```

## Ejecucion

El programa se ejecuta desde `main.py`:

```bash
python main.py
```

Al iniciar, se cargan automaticamente los datos desde `data/club_lectura.json` si el fichero existe. Despues aparece un menu interactivo con las operaciones disponibles.

Al salir con la opcion `0`, el programa guarda automaticamente los datos en `data/club_lectura.json`.

## Menu Principal

```text
1. Anadir libro
2. Anadir articulo
3. Ver materiales
4. Crear bibliografia
5. Anadir material a bibliografia
6. Ver bibliografias
7. Anadir resena
8. Ver resenas y valoracion media de un material
9. Crear sesion de lectura
10. Ver sesiones
11. Ver materiales ordenados por prioridad
12. Guardar datos
13. Cargar datos
14. Eliminar material
15. Guardar datos en binario
16. Cargar datos desde binario
0. Salir
```

## Persistencia

El proyecto tiene dos repositorios de persistencia:

- `JsonRepository`: guarda los datos en `data/club_lectura.json` usando JSON. Es el formato principal del programa, porque se carga al iniciar y se guarda al salir.
- `BinaryRepository`: guarda los datos en `data/club_lectura.bin` usando `pickle`. Este formato conserva directamente los objetos de Python en un fichero binario.

El repositorio binario abre los ficheros con modos binarios:

- `"wb"` para escribir.
- `"rb"` para leer.

Si el fichero JSON o binario no existe al cargar, el programa empieza con listas vacias.

## Manejo De Excepciones

El proyecto define excepciones propias en `src/club_lectura/exceptions/errors.py`:

- `ClubLecturaError`
- `DuplicadoError`
- `MetadatoInvalidoError`
- `ValoracionInvalidaError`
- `ElementoNoEncontradoError`
- `PersistenciaError`

Estas excepciones se usan para separar los errores del dominio del programa de los errores internos de Python.

Ejemplos:

- Si se intenta anadir un material duplicado a una bibliografia, se lanza `DuplicadoError`.
- Si un campo obligatorio esta vacio, se lanza `MetadatoInvalidoError`.
- Si una valoracion no esta entre 1 y 5, se lanza `ValoracionInvalidaError`.
- Si falla la lectura o escritura de datos, se lanza `PersistenciaError`.

Los repositorios de persistencia capturan errores de lectura, escritura, formato o datos corruptos y los convierten en `PersistenciaError`, para que el menu pueda mostrar un mensaje claro sin cerrar el programa de forma brusca.

## Dependencias

El proyecto no requiere dependencias externas. Solo necesita Python 3.10 o superior.

```bash
python --version
```

## Estado Actual

El programa funciona por consola y mantiene persistencia en JSON como formato principal. Tambien incluye guardado y carga en fichero binario como funcionalidad adicional.

## Mejoras Futuras

- Incorporar una base de datos para sustituir o complementar los ficheros.
- Anadir tests automatizados para modelos, validadores y repositorios.
- Crear una interfaz grafica o web para hacer el uso mas visual.

## Autoria

Trabajo realizado por Pablo Candela y Blanca Xifra.
