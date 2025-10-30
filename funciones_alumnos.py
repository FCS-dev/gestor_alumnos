def agregar_alumno(lista_alumnos):
    '''
    Se solicitan los datos de cada alumno
    y se valida que sean del tipo y rango
    correcto, posteriormente se agrega
    como diccionario a lista_alumnos
    '''
    while True:
        try:
            n = int(input('Cuántas calificaciones quieres agregar?: '))
            if n <= 0:
                print('Debes introducir un número positivo...')
                continue
            break
        except ValueError:
            print('Debes introducir un número entero...')

    for i in range(n):
        print(f'\nAlumno {i + 1} de {n}:')

        while True:
            nombre = input('Escribe el nombre del alumno: ').strip().lower()
            if nombre:
                break
            print('El nombre no puede estar vacío...')

        while True:
            try:
                edad = int(input('Escribe la edad del alumno: '))
                if edad <= 0:
                    print('La edad debe ser un número positivo...')
                else:
                    break
            except ValueError:
                print('Debes introducir un número entero...')

        while True:
            try:
                nota = float(input('Escribe la nota del alumno (0-10): '))
                if 0 <= nota <= 10:
                    break
                else:
                    print('Debes ingresar una nota entre 0 y 10...')
            except ValueError:
                print('Debes introducir un número válido...')

        lista_alumnos.append({'nombre': nombre, 'edad': edad, 'nota': nota})

    print('Datos agregados correctamente.')
    return lista_alumnos     


def mostrar_lista(lista_alumnos):
    '''
    Se muestra con formato tabla la data
    almacenada para cada alumno.
    Se valida si no hay alumnos en la lista.
    '''
    if not lista_alumnos:
        print('\ No hay alumnos en la lista...\n')
        return

    print('\ LISTA DE ALUMNOS')
    print('-' * 45)
    print('NOMBRE'.ljust(25), 'EDAD'.ljust(8), 'NOTA'.ljust(8))
    print('-' * 45)

    for alumno in lista_alumnos:
        print(f"{alumno['nombre'].capitalize().ljust(25)}"
              f"{str(alumno['edad']).ljust(8)}"
              f"{str(alumno['nota']).ljust(8)}")
    print('-' * 45)


def buscar_alumno(lista_alumnos):
    '''
    Se usa como criterio de búsqueda
    el nombre del alumno. 
    Se almacenan en una lista por comprensión
    (coincidencias) y se muestran todos
    aquellos alumnos que tengan el mismo nombre.
    Se valida si no existen coincidencias
    o si no hay alumnos en la lista.

    '''
    if lista_alumnos:
        while True:
            nombre_buscado = input('Escribe el nombre del alumno: ').strip().lower()
            if nombre_buscado:
                break
            else:
                print('El nombre no puede estar vacío...')

        coincidencias = [alumno for alumno in lista_alumnos if nombre_buscado in alumno['nombre']]

        if coincidencias:
            print(f' Se han encontrado las siguientes coincidencias para "{nombre_buscado}": ')
            for alumno in coincidencias:
                print(f"Nombre: {alumno['nombre'].capitalize()}, Edad: {alumno['edad']}, Nota: {alumno['nota']}")
        else:
            print(f' No se encontró ningún alumno con el nombre "{nombre_buscado}".')
    else: 
        print('No hay alumnos en la lista...')
        return

    return coincidencias