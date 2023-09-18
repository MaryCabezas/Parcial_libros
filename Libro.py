from Persona import Persona
from Categoria import Categoria
from Autor import Autor

import sys
import datetime

class Libro:

    cod_libro = ''
    titulo = ''
    año = ""
    tomo = ""

    def __init__(self, cod_libro, titulo, año, tomo, autor, categorias):
        self.cod_libro = cod_libro
        self.titulo = titulo
        self.año = año
        self.tomo = tomo
        self.autor = autor
        self.categorias = categorias

    # Métodos GET y SET para los atributos de Libro
    def get_cod_libro(self):
        return self.cod_libro

    def set_cod_libro(self, cod_libro):
        self.cod_libro = cod_libro

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_año(self):
        return self.año

    def set_año(self, año):
        self.año = año

    def get_tomo(self):
        return self.tomo

    def set_tomo(self, tomo):
        self.tomo = tomo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_categorias(self):  # Use 'get_categorias' instead of 'get_categoria'
        return self.categorias

    def set_categorias(self, categorias):  # Use 'set_categorias' instead of 'set_categoria'
        self.categorias = categorias

    # Método para imprimir la información del libro, incluyendo la información del autor y las categorías
    def imprimir_libro(self, file=None):
        if file is None:
            file = sys.stdout

        print(f"Código de Libro: {self.cod_libro}", file=file)
        print(f"Título: {self.titulo}", file=file)
        print(f"Año: {self.año}", file=file)
        print(f"Tomo: {self.tomo}", file=file)
        print("Autor:", file=file)
        self.autor.imprimir_autor(file)
        print("Categorías:", file=file)  # Update the print statement for 'categorias'
        for categoria in self.categorias:
            categoria.imprimir_categoria(file)
    