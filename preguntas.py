"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.split('\t') for row in data]
    data = [int(row[1]) for row in data]

    result = sum(data)

    return result


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
    from collections import Counter
    from operator import itemgetter

    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row[0] for row in data]

    count_letters = Counter()

    for row in data:
        count_letters[row[0]] += 1

    count_letters_tuples = list(count_letters.items())
    count_letters_tuples = sorted(count_letters_tuples, key=itemgetter(0), reverse=False)

    return count_letters_tuples


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
    from operator import itemgetter

    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [row[:2] for row in data]

    result = {}
    for letter, value_letter in data:
        value_letter = int(value_letter)
        if letter in result.keys():
            result[letter] = result[letter] + value_letter
        else:
            result[letter] = value_letter

    result = [(key, value_letter) for key, value_letter in result.items()]
    result = sorted(result, key=itemgetter(0), reverse=False)

    return result


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
    from collections import Counter
    from operator import itemgetter

    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [row[2].split('-') for row in data]

    registers_by_month = Counter()

    for row in data:
        registers_by_month[row[1]] += 1

    registers_by_month_tuples = list(registers_by_month.items())
    registers_by_month_tuples = sorted(registers_by_month_tuples, key=itemgetter(0), reverse=False)

    return registers_by_month_tuples


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
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [row[:2] for row in data]

    result = {}

    for letter, letter_value in data:
        letter_value = int(letter_value)
        if letter in result.keys():
            result[letter].append(letter_value)
        else:
            result[letter] = [letter_value]

    result = [(key, max(letter_value), min(letter_value)) for key, letter_value in result.items()]

    result = sorted(result, key=itemgetter(0), reverse=False)

    return result


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
    from operator import itemgetter

    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.replace("\n", "") for row in data]
    data = [row.split('\t') for row in data]

    result = {}

    for row in data:
        elementos_dict = row[4].split(',')
        elementos_dict = [row.split(':') for row in elementos_dict]
        for letras, valor in elementos_dict:
            if letras in result.keys():
                result[letras].append(int(valor))
            else:
                result[letras] = [int(valor)]

    result = [(letras,  min(valor), max(valor)) for letras, valor in result.items()]

    result = sorted(result, key=itemgetter(0), reverse=False)

    return result


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
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [row[:2] for row in data]

    result = {}

    for letra, valor in data:
        valor = int(valor)
        if valor in result.keys():
            result[valor].append(letra)
        else:
            result[valor] = [letra]

    result = [(valor, letra) for valor, letra in result.items()]

    result = sorted(result, key=itemgetter(0), reverse=False)

    return result


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
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [row[:2] for row in data]

    result = {}

    for letter, letter_value in data:
        letter_value = int(letter_value)
        if letter_value in result.keys():
            result[letter_value].append(letter)
        else:
            result[letter_value] = [letter]

    result = {letter_value: list(set(letter)) for letter_value, letter in result.items()}

    result = [(letter_value, sorted(letter)) for letter_value, letter in result.items()]

    result = sorted(result, key=itemgetter(0), reverse=False)

    return result


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

    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.replace("\n", "") for row in data]
    data = [row.split('\t') for row in data]
    data = [row[4] for row in data]
    data = [row.split(',') for row in data]
    data = [line.split(':')[0] for row in data for line in row]

    result = {}
    for letters in data:
        if letters in result.keys():
            result[letters] = result[letters] + 1
        else:
            result[letters] = 1

    result = dict((key, letters) for key, letters in sorted(result.items(), key=lambda t: t[0]))

    return result


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
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.replace("\n", "") for row in data]
    data = [row.split('\t') for row in data]
    data = [[row[0]] + row[3:5] for row in data]

    result = []

    for row in data:
        col_four = len(row[1].split(','))
        col_five = len(row[2].split(','))
        tuple_elements = (row[0], col_four, col_five)
        result.append(tuple_elements)

    return result


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

    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.replace("\n", "") for row in data]
    data = [row.split('\t') for row in data]
    data = [[row[1]] + [row[3]] for row in data]

    result = {}

    for row in data:
        letter_value = int(row[0])
        letters = row[1].split(',')
        for row_letter in letters:
            if row_letter in result.keys():
                result[row_letter].append(letter_value)
            else:
                result[row_letter] = [letter_value]

    result = dict((key, sum(letter_value)) for key, letter_value in sorted(result.items(), key=lambda t: t[0]))

    return result


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
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.replace("\n", "") for row in data]
    data = [row.split('\t') for row in data]
    data = [[row[0]] + [row[4]] for row in data]

    result = {}

    for row in data:
        letter = row[0]
        letter_value= row[1].split(',')
        for row_value in letter_value:
            element = int(row_value.split(':')[1])
            if letter in result.keys():
                result[letter].append(element)
            else:
                result[letter] = [element]

    result = dict((key, sum(letter_value)) for key, letter_value in sorted(result.items(), key=lambda t: t[0]))

    return result
