from Autor import Autor
from Libro import Libro
from Categoria import Categoria
import datetime
import json

class NegocioLibros:
    def __init__(self):
        self.libros = []
        self.autores = []
        self.categorias = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.autores.append(libro.autor)
        self.categorias.append(libro.categorias)

    def editar_libro(self, cod_libro, nuevo_libro):
        for i, libro in enumerate(self.libros):
            if libro.get_cod_libro() == cod_libro:
                self.libros[i] = nuevo_libro
                self.autores[i] = nuevo_libro.autor
                self.categorias[i] = nuevo_libro.categoria
                break
        self.reporte_libros() # si no funciona sacarlo

    def eliminar_libro(self, cod_libro):
        for i, libro in enumerate(self.libros):
            if libro.get_cod_libro() == cod_libro:
                del self.libros[i]
                del self.autores[i]
                del self.categorias[i]
                break

    def reporte_libros(self):
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
        nombre_archivo = f"reporte_{fecha_actual}.txt"

        libros_serializados = []
        for libro in self.libros:
            libros_serializados.append({
                "Código de Libro": libro.get_cod_libro(),
                "Título": libro.get_titulo(),
                "Año": libro.get_año(),
                "Tomo": libro.get_tomo(),
                "Autor": {
                    "Código de Autor": libro.get_autor().get_cod_autor(),
                    "Nombre del Autor": libro.get_autor().get_nombre(),
                    "Apellido Paterno del Autor": libro.get_autor().get_ap_paterno(),
                    "Apellido Materno del Autor": libro.get_autor().get_ap_materno(),
                    "Fecha de Nacimiento del Autor": libro.get_autor().get_fecha_nacimiento(),
                    "País del Autor": libro.get_autor().get_pais(),
                    "Editorial del Autor": libro.get_autor().get_editorial()
                },
                "Categorías": [
                    {
                        "Código de Categoría": categoria.get_cod_categoria(),
                        "Categoría": categoria.get_categoria()
                    }
                    for categoria in libro.get_categorias()
                ]
            })

        with open(nombre_archivo, "w") as file:
            json.dump(libros_serializados, file, indent=4)

        print(f"Reporte de libros generado en '{nombre_archivo}'")
