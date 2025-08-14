class Libro:
    def __init__(self, codigo, titulo, autor, anio):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def get_libro(self):
        return f"Codigo: {self.codigo} - Titulo: {self.titulo} - Autor: {self.autor} - Año: {self.anio}"


class Usuario:
    def __init__(self, carne, nombre, carrera):
        self.carne = carne
        self.nombre = nombre
        self.carrera = carrera

    def get_usuario(self):
        return f"Carne: {self.carne} - Nombre: {self.nombre} - Carrera: {self.carrera}"

