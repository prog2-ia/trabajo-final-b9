from .gestores import (
    agregar_articulo,
    agregar_libro,
    agregar_material_a_bibliografia,
    agregar_resena,
    crear_bibliografia,
    crear_sesion,
    ver_bibliografias,
    ver_materiales,
    ver_materiales_ordenados,
    ver_resenas_y_media,
    ver_sesiones,
)


def mostrar_menu():
    print("\n=== CLUB DE LECTURA Y BIBLIOGRAFÍAS ===")
    print("1. Añadir libro")
    print("2. Añadir artículo")
    print("3. Ver materiales")
    print("4. Crear bibliografía")
    print("5. Añadir material a bibliografía")
    print("6. Ver bibliografías")
    print("7. Añadir reseña")
    print("8. Ver reseñas y valoración media de un material")
    print("9. Crear sesión de lectura")
    print("10. Ver sesiones")
    print("11. Ver materiales ordenados por prioridad")
    print("0. Salir")


def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            agregar_articulo()
        elif opcion == "3":
            ver_materiales()
        elif opcion == "4":
            crear_bibliografia()
        elif opcion == "5":
            agregar_material_a_bibliografia()
        elif opcion == "6":
            ver_bibliografias()
        elif opcion == "7":
            agregar_resena()
        elif opcion == "8":
            ver_resenas_y_media()
        elif opcion == "9":
            crear_sesion()
        elif opcion == "10":
            ver_sesiones()
        elif opcion == "11":
            ver_materiales_ordenados()
        elif opcion == "0":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")