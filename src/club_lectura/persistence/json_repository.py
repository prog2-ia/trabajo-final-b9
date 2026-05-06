import json
from datetime import datetime
from pathlib import Path

from club_lectura.enums import Genero, Nivel
from club_lectura.modelos import Articulo, Bibliografia, Libro, MaterialBibliografico, Resena, SesionLectura
from club_lectura.exceptions import PersistenciaError


class JsonRepository:
    def __init__(self, ruta_fichero: str = "data/club_lectura.json") -> None:
        self.ruta_fichero = Path(ruta_fichero)

    def guardar(self, materiales: list, bibliografias: list, sesiones: list) -> None:
        self.ruta_fichero.parent.mkdir(parents=True, exist_ok=True)

        datos = {
            "materiales": [self._material_a_dict(material) for material in materiales],
            "bibliografias": [self._bibliografia_a_dict(bibliografia) for bibliografia in bibliografias],
            "sesiones": [self._sesion_a_dict(sesion) for sesion in sesiones],
        }

        with open(self.ruta_fichero, "w", encoding="utf-8") as fichero:
            json.dump(datos, fichero, indent=4, ensure_ascii=False)

    def cargar(self) -> tuple[list, list, list]:
        if not self.ruta_fichero.exists():
            return [], [], []

        try:
            with open(self.ruta_fichero, "r", encoding="utf-8") as fichero:
                datos = json.load(fichero)

            if not isinstance(datos, dict):
                raise PersistenciaError(
                    "El archivo JSON no tiene el formato esperado. "
                    "Debe contener un diccionario principal."
                )

            materiales = []
            materiales_por_id = {}

            for item in datos.get("materiales", []):
                material = self._dict_a_material(item)
                materiales.append(material)
                materiales_por_id[material.id] = material

            bibliografias = []
            for item in datos.get("bibliografias", []):
                bibliografia = self._dict_a_bibliografia(item, materiales_por_id)
                bibliografias.append(bibliografia)

            sesiones = []
            for item in datos.get("sesiones", []):
                sesion = self._dict_a_sesion(item, materiales_por_id)
                if sesion is not None:
                    sesiones.append(sesion)

            self._actualizar_contador_ids(materiales)

            return materiales, bibliografias, sesiones

        except json.JSONDecodeError as error:
            raise PersistenciaError(
                "No se han podido cargar los datos porque el archivo JSON está dañado o mal escrito."
            ) from error

        except KeyError as error:
            raise PersistenciaError(
                f"No se han podido cargar los datos porque falta el campo obligatorio: {error}."
            ) from error

        except TypeError as error:
            raise PersistenciaError(
                "No se han podido cargar los datos porque el JSON contiene datos con un tipo incorrecto."
            ) from error

        except ValueError as error:
            raise PersistenciaError(
                f"No se han podido cargar los datos porque hay un valor inválido: {error}."
            ) from error

        except OSError as error:
            raise PersistenciaError(
                "No se ha podido leer el archivo de datos."
            ) from error

    def _material_a_dict(self, material) -> dict:
        datos = {
            "id": material.id,
            "titulo": material.titulo,
            "autor": material.autor,
            "genero": material.genero.name,
            "nivel": material.nivel.name,
            "paginas": material.paginas,
            "resenas": [self._resena_a_dict(resena) for resena in material.resenas],
        }

        if isinstance(material, Libro):
            datos["tipo"] = "libro"
            datos["isbn"] = material.isbn

        elif isinstance(material, Articulo):
            datos["tipo"] = "articulo"
            datos["revista"] = material.revista
            datos["doi"] = material.doi

        else:
            datos["tipo"] = "desconocido"

        return datos

    def _dict_a_material(self, datos: dict):
        tipo = datos.get("tipo")

        if tipo == "libro":
            material = Libro(
                titulo=datos["titulo"],
                autor=datos["autor"],
                genero=Genero[datos["genero"]],
                nivel=Nivel[datos["nivel"]],
                paginas=datos["paginas"],
                isbn=datos["isbn"],
            )

        elif tipo == "articulo":
            material = Articulo(
                titulo=datos["titulo"],
                autor=datos["autor"],
                genero=Genero[datos["genero"]],
                nivel=Nivel[datos["nivel"]],
                paginas=datos["paginas"],
                revista=datos["revista"],
                doi=datos.get("doi"),
            )

        else:
            raise ValueError(f"Tipo de material no reconocido: {tipo}")

        material._id = datos["id"]

        for datos_resena in datos.get("resenas", []):
            Resena(
                material=material,
                autor_resena=datos_resena["autor_resena"],
                valoracion=datos_resena["valoracion"],
                comentario=datos_resena["comentario"],
            )

        return material

    def _resena_a_dict(self, resena) -> dict:
        return {
            "autor_resena": resena.autor_resena,
            "valoracion": resena.valoracion,
            "comentario": resena.comentario,
        }

    def _bibliografia_a_dict(self, bibliografia) -> dict:
        return {
            "nombre": bibliografia.nombre,
            "materiales_ids": [material.id for material in bibliografia],
        }

    def _dict_a_bibliografia(self, datos: dict, materiales_por_id: dict) -> Bibliografia:
        bibliografia = Bibliografia(datos["nombre"])

        for material_id in datos.get("materiales_ids", []):
            material = materiales_por_id.get(material_id)
            if material is not None:
                bibliografia.agregar_material(material)

        return bibliografia

    def _sesion_a_dict(self, sesion) -> dict:
        return {
            "fecha": sesion.fecha.isoformat(),
            "material_id": sesion.material.id,
            "moderador": sesion.moderador,
            "asistentes": sesion.asistentes,
        }

    def _dict_a_sesion(self, datos: dict, materiales_por_id: dict):
        material = materiales_por_id.get(datos["material_id"])

        if material is None:
            return None

        sesion = SesionLectura(
            fecha=datetime.fromisoformat(datos["fecha"]),
            material=material,
            moderador=datos["moderador"],
        )

        for asistente in datos.get("asistentes", []):
            sesion.agregar_asistente(asistente)

        return sesion

    def _actualizar_contador_ids(self, materiales: list) -> None:
        if not materiales:
            MaterialBibliografico._contador_ids = 1
            return

        mayor_id = max(material.id for material in materiales)
        MaterialBibliografico._contador_ids = mayor_id + 1