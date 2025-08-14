class Libro:
    def __init__(self,codigo, titulo, autor, anio):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def get_libro(self):
        return f"Codigo: {self.codigo} - Titulo: {self.titulo} - Autor: {self.autor} - Año: {self.anio}"

class ListaLibros:
    def __init__(self):
        self.libros = {}

    def agregar(self):
        codigo = input("Ingrese el codigo del libro: ")

        if codigo in self.libros:
            print("El libro ya existe")
        else:
            self.libros[codigo] = Libro(
                input("Ingrese el codigo del libro: "),
                input("Ingrese el titulo del libro: "),
                input("Ingrese el autor del libro: "),
                input("Ingrese el anio del libro: ")
            )

class Usuario:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def get_usuario(self):
        return f"Nombre: {self.nombre} - Carrera: {self.carrera}"

class ListaUsuarios:
    def __init__(self):
        self.usuarios = {}

class Gestiones:
