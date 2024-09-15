"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def peticion():
    with open("data.csv", "r") as file:
        datos=file.readlines()
    datos=[line.split("\n") for line in datos]
    datos=[[elemento for elemento in sublist.split('\t') if elemento] for sublist, _ in datos]
    return datos

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    datos=peticion()
    suma=map(lambda fila: fila[1], datos)
    suma=sum(map(int, suma))

    return suma

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    datos=peticion()
    conteo = {}
    for sublist in datos:
        letra = sublist[0][0]
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    conteo_ordenado = sorted(conteo.items())
    return conteo_ordenado

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    datos=peticion()
    conteo = {}
    for sublist in datos:
        letra = sublist[0][0]
        suma=int(sublist[1][0])
        if letra in conteo:
            conteo[letra] += suma
        else:
            conteo[letra] = suma
    conteo_ordenado = sorted(conteo.items())
    return conteo_ordenado

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    datos=peticion()
    conteo = {}
    for sublist in datos:
        mes = sublist[2]
        mes = mes.split("-")
        mes = mes[1]
        if mes in conteo:
            conteo[mes] += 1
        else:
            conteo[mes] = 1
    conteo_ordenado = sorted(conteo.items())
    return conteo_ordenado

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    datos=peticion()
    conteo = {}
    for sublist in datos:
        letra = sublist[0][0]
        comparacion=int(sublist[1][0])
        if letra in conteo:
            if conteo[letra][0] < comparacion:
                conteo[letra][0] = comparacion
            elif conteo[letra][1] > comparacion:
                conteo[letra][1] = comparacion
        else:
            conteo[letra] = [comparacion,comparacion]
    lista1=list(conteo.items())
    conteo_ordenado = []
    for i in range(len(lista1)):
        conteo_ordenado.append((lista1[i][0],lista1[i][1][0],lista1[i][1][1]))
    conteo_ordenado = sorted(conteo_ordenado, key=lambda x: x[0])
    return conteo_ordenado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    datos=peticion()
    conteo = {}
    for sublist in datos:
        linea = sublist[4]
        comparacion=linea.split(",")
        for par in comparacion:
            par=par.split(":")
            letras=par[0]
            numero=int(par[1])
            if letras in conteo:
                if conteo[letras][0] > numero:
                    conteo[letras][0] = numero
                elif conteo[letras][1] < numero:
                    conteo[letras][1] = numero
            else:
                conteo[letras] = [numero,numero]
    lista1=list(conteo.items())
    conteo_ordenado = []
    for i in range(len(lista1)):
        conteo_ordenado.append((lista1[i][0],lista1[i][1][0],lista1[i][1][1]))
    conteo_ordenado = sorted(conteo_ordenado, key=lambda x: x[0])
    return conteo_ordenado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    datos=peticion()
    conteo = {}
    for sublist in datos:
        linea = sublist[1]
        letra = sublist[0]
        for par in linea:
            numero=int(par)
            if numero in conteo:
                conteo[numero].append(letra)
            else:
                conteo[numero] = [letra]
    lista1=list(conteo.items())
    conteo_ordenado = []
    for i in range(len(lista1)):
        conteo_ordenado.append((lista1[i][0],lista1[i][1]))
    conteo_ordenado = sorted(conteo_ordenado, key=lambda x: x[0])
    return conteo_ordenado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    datos=peticion()
    conteo = {}
    for sublist in datos:
        linea = sublist[1]
        letra = sublist[0]
        for par in linea:
            numero=int(par)
            if numero in conteo:
                if not letra in conteo[numero]:
                    conteo[numero].append(letra)
            else:
                conteo[numero] = [letra]
    lista1=list(conteo.items())
    conteo_ordenado = []
    for i in range(len(lista1)):
        conteo_ordenado.append((lista1[i][0],sorted(lista1[i][1])))
    conteo_ordenado = sorted(conteo_ordenado, key=lambda x: x[0])
    return conteo_ordenado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    datos=peticion()
    conteo = {}
    for sublist in datos:
        linea = sublist[4]
        comparacion=linea.split(",")
        for par in comparacion:
            par=par.split(":")
            letras=par[0]
            if letras in conteo:
                conteo[letras] += 1
            else:
                conteo[letras] = 1
    return conteo

print(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    datos=peticion()
    conteo_ordenado = []
    for sublist in datos:
        letra=sublist[0]
        abecedario=sublist[3].split(",")
        linea = sublist[4].split(",")
        conteo_ordenado.append((letra,len(abecedario),len(linea)))
    return conteo_ordenado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    datos=peticion()
    conteo_ordenado ={}
    for sublist in datos:
        letra=sublist[1]
        abecedario=sublist[3].split(",")
        for i in abecedario:
            if i in conteo_ordenado:
                conteo_ordenado[i] += int(letra)
            else:
                conteo_ordenado[i] = int(letra)
    return conteo_ordenado

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    datos=peticion()
    conteo_ordenado ={}
    letras = set()
    for fila in datos:
        letras.add(fila[0])
    for sublist in datos:
        letra=sublist[0]
        abecedario=sublist[4].split(",")
        for i in abecedario:
            probar=i.split(":")
            if letra in conteo_ordenado:
                conteo_ordenado[letra] += int(probar[1])
            else:
                conteo_ordenado[letra] = int(probar[1])
    return conteo_ordenado
