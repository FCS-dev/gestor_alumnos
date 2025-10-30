import os
import nacho
import jose


def menu():
    print(
        "Gestor de Alumnos"
        "\n-----------------------"
        "\n1. Ver lista de alumnos"
        "\n2. Añadir alumno"
        "\n3. Buscar alumno"
        "\n4. Mostrar estadisticas"
        "\n0. Salir"
        "\n-----------------------"
    )
    opc = input("\nIngrese su opción -> ").strip()
    return opc


def main():
    """
    Procedimiento principal. Maneja todas las funcionalidades de la app,
    y hace las solicitudes según sea el caso a todas los módulos donde se
    hacen las operaciones del menú de opciones.
    """

    alumnos = []

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        opc = menu()
        ##os.system("cls" if os.name == "nt" else "clear")
        match opc:
            case "1":  # Listar productos
                jose.listar(alumnos)
            case "2":  # Añadir productos al carrito
                jose.agregar(alumnos)
            case "3":  # Eliminar productos del carrito
                jose.buscar(alumnos)
            case "4":  # Formalizar compra
                nacho.estadisticas(alumnos)
            case "0":
                print("👋 Adios!")
                break
            case _:
                print("\n🚫 Opción no válida. Intente nuevamente.")
        input("\nPresione <Enter> para continuar...")


if __name__ == "__main__":
    main()
