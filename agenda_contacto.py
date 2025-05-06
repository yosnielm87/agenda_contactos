def mostrar_menu():
    print("\nAgenda de Contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente:")
    print("3. Buscar contacto:")
    print("4. Lista de contactos:")
    print("Salir del programa..")


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        op = input("Por favor elija una opcion...")

        if op == "1":
            pass
        elif op == "2":
            pass
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "5":
            print("Cerrando la agenda de contactos...")
            break
        else:
            print("Por favor escoja una opcion valida", mostrar_menu())

agenda_contactos()
