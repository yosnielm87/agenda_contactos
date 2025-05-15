from pydantic import BaseModel, EmailStr, ValidationError


# Definimos el modelo Contacto
class Contacto(BaseModel):
    telefono: str
    email: EmailStr


def mostrar_menu():
    print("\nAgenda de Contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("Salir del programa..")
    print("_" * 50)


def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre del contacto: ")
    telefono = input("Por favor introduzca el telefono del contacto: ")
    email = input("Por favor introduzca el email del contacto: ")

    try:
        contacto = Contacto(telefono=telefono, email=email)
        agenda[nombre] = contacto
        print(f"¡Se ha añadido el contacto {nombre}!")
    except ValidationError as e:
        print("Error en los datos ingresados:", e)


def eliminar_contacto(ag):
    nombre = input("Por favor introduzca el nombre del contacto a eliminar: ")
    if nombre in ag:
        del ag[nombre]
        print(f"El contacto {nombre} ha sido eliminado!!")
    else:
        print(f"No existe un contacto con el nombre de {nombre}")


def buscar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre del contacto a buscar: ")
    if nombre in agenda:
        contacto = agenda[nombre]
        print(f"Nombre: {nombre}")
        print(f"Telefono: {contacto.telefono}")
        print(f"Email: {contacto.email}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado.")


def listar_contactos(agenda):
    if agenda:
        print("\nLista de Contactos:")
        for nombre, contacto in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Email: {contacto.email}")
            print(f"Telefono: {contacto.telefono}")
            print("-" * 20)
    else:
        print("La agenda aún está vacía...")


def agenda_contactos():
    agenda = {}

    # Definir los handlers para cada opción
    def agregar():
        agregar_contacto(agenda)

    def eliminar():
        eliminar_contacto(ag=agenda)

    def buscar():
        buscar_contacto(agenda)

    def listar():
        listar_contactos(agenda)
 
    def salir():
        print("Cerrando la agenda de contactos...")

    # Diccionario de handlers
    # Un handler es una función que responde a un evento o acción específica. 
    # Son las funciones que gestionan cada opción del menú.
    handlers = {
        "1": agregar, 
        "2": eliminar, "3": buscar, "4": listar, "5": salir}

    while True:
        mostrar_menu()
        op = input("Por favor, elija una opción: ")
        print()

        if op == "5":
            handlers[op]()
            break
        elif op in handlers:
            handlers[op]()
        else:
            print("Por favor, escoja una opción válida.")


if __name__ == "__main__":
    agenda_contactos()
