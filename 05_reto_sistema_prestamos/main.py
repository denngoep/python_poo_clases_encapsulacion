# Sistema de Préstamos de Equipos
# Reto integrador utilizando Programación Orientada a Objetos.

from datetime import date

from equipo import Equipo
from usuario import Usuario
from prestamo import Prestamo


# Diccionario principal de equipos.
equipos = {
    "Portatil Dell": Equipo("Portatil Dell"),
    "Portatil HP": Equipo("Portatil HP"),
    "Tablet Samsung": Equipo("Tablet Samsung")
}

# Diccionario para almacenar usuarios.
usuarios = {}

# Lista general de préstamos.
prestamos = []


def mostrar_equipos():
    print("\n=== EQUIPOS REGISTRADOS ===")

    for equipo in equipos.values():
        print(equipo)


def registrar_prestamo():
    print("\n=== REGISTRAR PRÉSTAMO ===")

    mostrar_equipos()

    nombre_equipo = input(
        "\nIngrese el nombre exacto del equipo: "
    ).strip()

    if nombre_equipo not in equipos:
        print("El equipo no existe.")
        return

    equipo = equipos[nombre_equipo]

    if not equipo.disponible:
        print("El equipo se encuentra prestado.")
        return

    nombre_usuario = input(
        "Ingrese el nombre del usuario: "
    ).strip()

    if not nombre_usuario:
        print("El nombre del usuario no puede estar vacío.")
        return

    # Si el usuario no existe, se crea.
    if nombre_usuario not in usuarios:
        usuarios[nombre_usuario] = Usuario(nombre_usuario)

    usuario = usuarios[nombre_usuario]

    fecha_actual = date.today().strftime("%d/%m/%Y")

    # Creamos el objeto préstamo.
    prestamo = Prestamo(
        usuario,
        equipo,
        fecha_actual
    )

    # Actualizamos el estado del equipo.
    equipo.prestar()

    # Guardamos el préstamo en las colecciones.
    prestamos.append(prestamo)

    usuario.agregar_prestamo(prestamo)

    equipo.agregar_prestamo_historial(prestamo)

    print("\nPréstamo registrado correctamente.")
    print(prestamo)


def devolver_equipo():
    print("\n=== DEVOLVER EQUIPO ===")

    nombre_equipo = input(
        "Ingrese el nombre exacto del equipo: "
    ).strip()

    if nombre_equipo not in equipos:
        print("El equipo no existe.")
        return

    equipo = equipos[nombre_equipo]

    if equipo.disponible:
        print("El equipo ya se encuentra disponible.")
        return

    # Buscamos el préstamo activo del equipo.
    prestamo_activo = None

    for prestamo in prestamos:
        if (
            prestamo.equipo == equipo
            and prestamo.activo
        ):
            prestamo_activo = prestamo
            break

    if prestamo_activo is None:
        print("No se encontró un préstamo activo.")
        return

    prestamo_activo.devolver()
    equipo.devolver()

    print("Equipo devuelto correctamente.")
    print(prestamo_activo)


def ver_historial():
    print("\n=== HISTORIAL DE PRÉSTAMOS ===")

    for equipo in equipos.values():
        print(f"\nEquipo: {equipo.nombre}")

        if not equipo.historial_prestamos:
            print("Sin préstamos registrados.")
            continue

        for prestamo in equipo.historial_prestamos:
            print(prestamo)


def agregar_equipo():
    print("\n=== AGREGAR EQUIPO ===")

    nombre = input(
        "Ingrese el nombre del nuevo equipo: "
    ).strip()

    if not nombre:
        print("El nombre del equipo no puede estar vacío.")
        return

    if nombre in equipos:
        print("El equipo ya existe.")
        return

    equipos[nombre] = Equipo(nombre)

    print("Equipo registrado correctamente.")


def consultar_prestamo():
    print("\n=== CONSULTAR PRÉSTAMOS ===")

    nombre_usuario = input(
        "Ingrese el nombre del usuario: "
    ).strip()

    if nombre_usuario not in usuarios:
        print("El usuario no tiene préstamos registrados.")
        return

    usuario = usuarios[nombre_usuario]

    if not usuario.prestamos:
        print("El usuario no tiene préstamos registrados.")
        return

    for prestamo in usuario.prestamos:
        print(prestamo)


def modificar_prestamo():
    print("\n=== MODIFICAR PRÉSTAMO ===")

    nombre_equipo = input(
        "Ingrese el nombre del equipo: "
    ).strip()

    if nombre_equipo not in equipos:
        print("El equipo no existe.")
        return

    equipo = equipos[nombre_equipo]

    prestamo_activo = None

    for prestamo in prestamos:
        if (
            prestamo.equipo == equipo
            and prestamo.activo
        ):
            prestamo_activo = prestamo
            break

    if prestamo_activo is None:
        print("No existe un préstamo activo para ese equipo.")
        return

    nueva_fecha = input(
        "Ingrese la nueva fecha del préstamo: "
    ).strip()

    if not nueva_fecha:
        print("La fecha no puede estar vacía.")
        return

    prestamo_activo.modificar_fecha(nueva_fecha)

    print("Préstamo modificado correctamente.")
    print(prestamo_activo)


def menu():
    while True:
        print("\n===================================")
        print(" SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("===================================")

        print("1. Ver equipos")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial")
        print("5. Agregar equipo")
        print("6. Consultar préstamos por usuario")
        print("7. Modificar préstamo")
        print("8. Salir")

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        if opcion == "1":
            mostrar_equipos()

        elif opcion == "2":
            registrar_prestamo()

        elif opcion == "3":
            devolver_equipo()

        elif opcion == "4":
            ver_historial()

        elif opcion == "5":
            agregar_equipo()

        elif opcion == "6":
            consultar_prestamo()

        elif opcion == "7":
            modificar_prestamo()

        elif opcion == "8":
            print("\nPrograma finalizado.")
            break

        else:
            print(
                "Opción inválida. "
                "Seleccione una opción entre 1 y 8."
            )


if __name__ == "__main__":
    menu()