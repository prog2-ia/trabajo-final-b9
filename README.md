# Club de lectura y bibliografias

Proyecto de Programacion Orientada a Objetos en Python para gestionar un club de lectura desde consola. Permite registrar libros y articulos, crear bibliografias, anadir resenas, organizar sesiones de lectura y guardar/cargar los datos en ficheros.

## Objetivo Del Proyecto

El programa esta pensado para practicar y demostrar estos conceptos:

- clases y objetos
- encapsulacion mediante propiedades
- herencia y clases abstractas
- polimorfismo entre `Libro` y `Articulo`
- sobrecarga de operadores
- enumeraciones
- excepciones personalizadas
- persistencia en JSON
- persistencia en fichero binario
- organizacion modular del codigo

## Como Ejecutarlo

Desde la raiz del proyecto:

```bash
python main.py
```

El programa abre un menu interactivo en la terminal. Al arrancar intenta cargar automaticamente los datos desde:

```text
data/club_lectura.json
```

Si el fichero no existe, el programa empieza con listas vacias. Al salir con la opcion `0`, guarda automaticamente el estado actual en ese mismo fichero JSON.

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

## Funcionamiento General

El programa mantiene tres listas principales en memoria mientras se esta ejecutando:

- `materiales`: libros y articulos registrados.
- `bibliografias`: conjuntos de materiales seleccionados.
- `sesiones`: sesiones de lectura programadas.

Cada opcion del menu modifica o consulta esas listas. Cuando se guardan los datos, el contenido de esas listas pasa a un fichero. Cuando se cargan datos, esas listas se reemplazan por lo que haya en el fichero.

## Materiales

Hay dos tipos de materiales bibliograficos:

- `Libro`: tiene titulo, autor, genero, nivel, numero de paginas e ISBN.
- `Articulo`: tiene titulo, autor, genero, nivel, numero de paginas, revista y DOI opcional.

El DOI es opcional porque no todos los articulos tienen uno. Si se deja vacio al crear un articulo, se guarda como `None`.

Los generos y niveles se eligen desde listas cerradas para evitar errores de escritura.

## Bibliografias

Una bibliografia agrupa materiales. El programa evita duplicados: si intentas anadir dos veces el mismo material a la misma bibliografia, se muestra un error controlado.

Las bibliografias tambien soportan combinacion con el operador `+` dentro del codigo, creando una nueva bibliografia sin repetir materiales.

## Resenas

Cada resena pertenece a un material y contiene:

- autor de la resena
- valoracion numerica entre 1 y 5
- comentario

Si la valoracion no esta entre 1 y 5, el programa lanza una excepcion personalizada y muestra un mensaje de error sin cerrarse.

La valoracion media de un material se calcula a partir de todas sus resenas.

## Sesiones De Lectura

Una sesion de lectura contiene:

- fecha y hora
- material que se va a comentar
- moderador
- asistentes

La fecha debe introducirse con este formato:

```text
dd/mm/yyyy HH:MM
```

Ejemplo:

```text
21/05/2026 18:30
```

Si se elimina un material, tambien se eliminan las sesiones asociadas a ese material para no dejar referencias incorrectas.

## Persistencia De Datos

El proyecto tiene dos formas de guardar datos.

### JSON

El formato principal es JSON:

```text
data/club_lectura.json
```

Se usa automaticamente:

- al iniciar el programa, para cargar datos
- al salir con `0`, para guardar datos
- con la opcion `12`, para guardar manualmente
- con la opcion `13`, para cargar manualmente

Este formato es legible y se puede abrir con un editor de texto.

### Binario

Tambien existe persistencia binaria:

```text
data/club_lectura.bin
```

Se usa con:

- opcion `15`: guardar datos en binario
- opcion `16`: cargar datos desde binario

El repositorio binario usa `pickle` y abre el fichero en modo:

- `"wb"` para escribir en binario
- `"rb"` para leer en binario

El fichero binario no esta pensado para editarse a mano. Sirve para guardar directamente los objetos de Python.

## Manejo De Excepciones

El proyecto define excepciones propias en:

```text
src/club_lectura/exceptions/errors.py
```

Excepciones principales:

- `ClubLecturaError`
- `DuplicadoError`
- `MetadatoInvalidoError`
- `ValoracionInvalidaError`
- `ElementoNoEncontradoError`
- `PersistenciaError`

Ejemplos de errores controlados:

- campo obligatorio vacio
- numero de paginas no positivo
- valoracion fuera del rango 1-5
- material duplicado en una bibliografia
- fichero JSON corrupto
- fichero binario corrupto
- errores de lectura o escritura de ficheros

La idea es que el programa muestre un mensaje claro y continue funcionando siempre que sea posible.

## Estructura Del Proyecto

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

## Explicacion De Carpetas

- `app/`: contiene el menu y las funciones que ejecutan cada opcion.
- `modelos/`: contiene las clases principales del dominio.
- `enums/`: contiene generos y niveles validos.
- `exceptions/`: contiene excepciones personalizadas.
- `persistence/`: contiene los repositorios JSON y binario.
- `utils/`: contiene validadores reutilizables.
- `data/`: contiene los ficheros donde se guardan los datos.

## Ejemplo De Ejecucion

Este ejemplo muestra un uso normal del programa.

```text
$ python main.py

Datos cargados correctamente desde data/club_lectura.json.
Materiales cargados: 0
Bibliografias cargadas: 0
Sesiones cargadas: 0

=== CLUB DE LECTURA Y BIBLIOGRAFIAS ===
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

Elige una opcion: 1

=== ANADIR LIBRO ===
Titulo: Dune
Autor: Frank Herbert

Generos disponibles:
1. Novela
2. Ensayo
3. Ciencia ficcion
4. Fantasia
5. Historia
6. Poesia
7. Divulgacion
8. Otro
Elige un genero: 3

Niveles disponibles:
1. Basico
2. Intermedio
3. Avanzado
Elige un nivel: 2

Numero de paginas: 600
ISBN: ISBN-1

Libro anadido correctamente: Libro: Dune, ISBN: ISBN-1

Elige una opcion: 4

=== CREAR BIBLIOGRAFIA ===
Nombre de la bibliografia: Ciencia ficcion

Bibliografia creada correctamente: Bibliografia 'Ciencia ficcion' con 0 materiales.

Elige una opcion: 5

=== ANADIR MATERIAL A BIBLIOGRAFIA ===
Bibliografias registradas:
1. Bibliografia 'Ciencia ficcion' con 0 materiales.
Selecciona una bibliografia: 1

Materiales registrados:
1. Dune - Frank Herbert (Ciencia ficcion, Intermedio)
Selecciona un material: 1

'Dune' anadido a la bibliografia.

Elige una opcion: 7

=== ANADIR RESENA ===
Materiales registrados:
1. Dune - Frank Herbert (Ciencia ficcion, Intermedio)
Selecciona un material: 1
Autor de la resena: Pablo
Valoracion (1-5): 5
Comentario: Muy buen libro

Resena anadida correctamente: Resena de Pablo sobre 'Dune': 5/5 - Muy buen libro

Elige una opcion: 8

=== VER RESENAS Y VALORACION MEDIA ===
Materiales registrados:
1. Dune - Frank Herbert (Ciencia ficcion, Intermedio)
Selecciona un material: 1

Material: Dune - Frank Herbert (Ciencia ficcion, Intermedio)
Valoracion media: 5.0

Resenas:
- Resena de Pablo sobre 'Dune': 5/5 - Muy buen libro

Elige una opcion: 9

=== CREAR SESION DE LECTURA ===
Materiales registrados:
1. Dune - Frank Herbert (Ciencia ficcion, Intermedio)
Selecciona un material: 1
Fecha y hora (dd/mm/yyyy HH:MM): 21/05/2026 18:30
Moderador: Blanca
Anade un asistente (Enter para terminar): Ana
Anade un asistente (Enter para terminar):

Sesion creada correctamente:
Sesion del 21/05/2026 18:30 sobre 'Dune'. Moderador: Blanca. Asistentes: 1.

Elige una opcion: 12

Datos guardados correctamente en data/club_lectura.json.

Elige una opcion: 15

Datos guardados correctamente en formato binario.

Elige una opcion: 0

Datos guardados correctamente en data/club_lectura.json.

Datos guardados. Saliendo del programa...
```

## Ejemplo De Error Controlado

Si se intenta poner una valoracion fuera de rango:

```text
Valoracion (1-5): 6

Error al anadir la resena: La valoracion debe estar entre 1 y 5.
```

Si se intenta anadir dos veces el mismo material a una bibliografia:

```text
No se pudo anadir: El material 'Dune' ya existe en la bibliografia 'Ciencia ficcion'.
```

## Dependencias

No hay dependencias externas. El proyecto solo necesita Python.

Version recomendada:

```text
Python 3.10 o superior
```

## Estado Actual

El programa funciona por consola, guarda automaticamente en JSON y ofrece guardado/carga binaria como funcionalidad adicional.

## Mejoras Futuras

- Anadir tests automatizados permanentes.
- Incorporar una base de datos.
- Crear una interfaz grafica o web.

## Autoria

Trabajo realizado por Pablo Candela y Blanca Xifra.
