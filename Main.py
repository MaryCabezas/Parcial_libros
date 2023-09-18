from Autor import Autor
from Libro import Libro
from Categoria import Categoria
from Negocio import NegocioLibros
from datetime import datetime


def main():
    negocio = NegocioLibros()

    while True:
        print("\nMENU DE OPCIONES")
        print("1- Añadir libro")
        print("2- Editar libro")
        print("3- Eliminar libro")
        print("4- Reporte de libros")
        print("5- Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cod_libro = input("Ingrese el código del libro: ")
            titulo = input("Ingrese el título del libro: ")
            año = input("Ingrese el año del libro: ")
            tomo = input("Ingrese el tomo del libro: ")

            cod_autor = input("Ingrese el código del autor: ")
            nombre_autor = input("Ingrese el nombre del autor: ")
            ap_paterno_autor = input("Ingrese el apellido paterno del autor: ")
            ap_materno_autor = input("Ingrese el apellido materno del autor: ")
            fecha_nacimiento_autor = input("Ingrese la fecha de nacimiento del autor: ")
            pais_autor = input("Ingrese el país del autor: ")
            editorial_autor = input("Ingrese la editorial del autor: ")

            cod_categoria = input("Ingrese el código de la categoría: ")
            categoria = input("Ingrese la categoría: ")

            autor = Autor(cod_autor, pais_autor, editorial_autor, cod_autor, nombre_autor, ap_paterno_autor, ap_materno_autor, fecha_nacimiento_autor)
            categorias = [Categoria(cod_categoria, categoria)]  # Use a list for categorías
            libro = Libro(cod_libro, titulo, año, tomo, autor, categorias)  # Pass the list of categorías

            negocio.agregar_libro(libro)

        elif opcion == "2":
            cod_libro = input("Ingrese el código del libro que desea editar: ")
            nuevo_cod_libro = input("Ingrese el nuevo código del libro: ")
            nuevo_titulo = input("Ingrese el nuevo título del libro: ")
            nuevo_año = input("Ingrese el nuevo año del libro: ")
            nuevo_tomo = input("Ingrese el nuevo tomo del libro: ")

            nuevo_cod_autor = input("Ingrese el nuevo código del autor: ")
            nuevo_nombre_autor = input("Ingrese el nuevo nombre del autor: ")
            nuevo_ap_paterno_autor = input("Ingrese el nuevo apellido paterno del autor: ")
            nuevo_ap_materno_autor = input("Ingrese el nuevo apellido materno del autor: ")
            nuevo_fecha_nacimiento_autor = input("Ingrese la nueva fecha de nacimiento del autor: ")
            nuevo_pais_autor = input("Ingrese el nuevo país del autor: ")
            nuevo_editorial_autor = input("Ingrese la nueva editorial del autor: ")

            nuevo_cod_categoria = input("Ingrese el nuevo código de la categoría: ")
            nueva_categoria = input("Ingrese la nueva categoría: ")

            nuevo_autor = Autor(nuevo_cod_autor, nuevo_pais_autor, nuevo_editorial_autor, nuevo_cod_autor, nuevo_nombre_autor, nuevo_ap_paterno_autor, nuevo_ap_materno_autor, nuevo_fecha_nacimiento_autor)
            nueva_categoria = Categoria(nuevo_cod_categoria, nueva_categoria)
            nuevo_libro = Libro(nuevo_cod_libro, nuevo_titulo, nuevo_año, nuevo_tomo, nuevo_autor, nueva_categoria)

            negocio.editar_libro(cod_libro, nuevo_libro)


        elif opcion == "3":
            cod_libro = input("Ingrese el código del libro que desea eliminar: ")
            negocio.eliminar_libro(cod_libro)

        elif opcion == "4":
            negocio.reporte_libros()
            print(f"Reporte de libros generado en 'reporte_fecha.txt' (nombre incluye la fecha actual)")

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()