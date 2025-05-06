def mostrar_menu():
    print("\nAgenda de Contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente:")
    print("3. Buscar contacto:")
    print("4. Lista de contactos:")
    print("Salir del programa..")
    print("_" * 50)

def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre del contacto: ")
    telefono = input("Por favor introduzca el telefono del contacto: ")
    email = input("Por favor introduzca el email del contacto: ")

    agenda[nombre] = { "telefono": telefono, "email": email}

    print (f"¡Se ha adicionado el contacto{nombre}!")

def eliminar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre del contacto a eliminar: ")

    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado!!")
    else:
        print(f"No existe un contacto con el nombre de {nombre}")

def buscar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre del contacto a buscar: ")

    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado.")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de Contactos: ")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Email: {info['email']}")
            print(f"Telefono: {info['telefono']}")
            print("-" * 20)
    else:
        print("La agenda aun esta vacia...")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        op = input("Por favor elija una opcion...")
        print("\n")

        if op == "1":
            agregar_contacto(agenda)
        elif op == "2":
            eliminar_contacto(agenda)
        elif op == "3":
            buscar_contacto(agenda)
        elif op == "4":
            listar_contactos(agenda)
        elif op == "5":
            print("Cerrando la agenda de contactos...")
            break
        else:
            print("Por favor escoja una opcion valida", mostrar_menu())

agenda_contactos()
