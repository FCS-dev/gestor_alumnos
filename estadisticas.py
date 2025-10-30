# `estadisticas.py`(nota media, máxima y mínima)

def calcular_media_nota(alumnos):
    total = 0
    for i in alumnos:
        total += float(i['nota'])
    media_nota = total / len(alumnos)
    return media_nota

def calcular_media_edad(alumnos):
    total = 0
    for i in alumnos:
        total += float(i['edad'])
    media_edad = total / len(alumnos)
    return media_edad

def calcular_maxima_minima(alumnos):
    notas = []
    edades = []
    for i in alumnos:
        notas.append(float(i.get('nota')))
        edades.append(float(i.get('edad')))
    nota_maxima = max(notas)
    nota_minima = min(notas)
    edad_maxima = max(edades)
    edad_minima = min(edades)
    return nota_maxima, nota_minima, edad_maxima, edad_minima

def estadisticas(alumnos):
    if not alumnos:
        print('Lista alumnos vacía.')
        return
    a, b, c, d = calcular_maxima_minima(alumnos)
    print(f'\nResultados:\n\t-La nota media es: {round(calcular_media_nota(alumnos),2)}\n\t-La edad media es: {calcular_media_edad(alumnos):.2f} años\n\t-La nota máxima es: {round(a,2)}\n\t-La nota mínima es: {round(b,2)}\n\t-La edad máxima es: {c:.2f}\n\t-La edad mínima es: {d:.2f}')


      


        

