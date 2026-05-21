import os
import sys

# Permite ejecutar el proyecto desde la raiz sin instalar el paquete.
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from club_lectura.app.menu import ejecutar_menu


if __name__ == "__main__":
    ejecutar_menu()
