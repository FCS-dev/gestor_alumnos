import os
import estadisticas as nacho
import funciones_alumnos as func


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
            case "1": 
                func.mostrar_lista(alumnos)
            case "2": 
                func.agregar_alumno(alumnos)
            case "3": 
                func.buscar_alumno(alumnos)
            case "4": 
                nacho.estadisticas(alumnos)

            case "0":
                print("👋 Adios!")
                break
            case _:
                print("\n🚫 Opción no válida. Intente nuevamente.")
        input("\nPresione <Enter> para continuar...")


if __name__ == "__main__":
    main()
