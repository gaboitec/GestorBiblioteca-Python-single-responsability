import clases
lista_libros = clases.ListaLibros()
lista_usuarios = clases.ListaUsuarios()

while True:
    print ("\n** MENU PRINPCIPAL **")
    print("1. Agregar libro")
    print("2. Agregar usuario")
    print("3. Mostrar libro")
    print("4. Mostrar usuario")
    print("5. Eliminar libro")
    print("6. Eliminar usuario")
    print("0. Salir")

    opcion = input("Elija una ocpion: ")

    match opcion:
        case "1":
            pass
