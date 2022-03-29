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

    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    sum_column = 0
    for row in data:
        sum_column = sum_column + int(row[1])

    return sum_column


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

    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    count_letters = Counter()

    for row in data:
        count_letters[row[0]] += 1

    count_letters_tuples = list(count_letters.items())
    count_letters_tuples = sorted(count_letters_tuples)

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
    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    set_letters = []
    for row in data:
        letter = row[0]
        if letter not in set_letters:
            set_letters.append(letter)

    sum_letters = []
    for letter in set_letters:
        sum_letter = 0
        for row in data:
            if row[0] == letter:
                sum_letter = sum_letter + int(row[1])
        sum_letters.append(sum_letter)

    sum_letter_tuple = list(zip(set_letters, sum_letters))
    sum_letter_tuple = sorted(sum_letter_tuple)

    return sum_letter_tuple


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

    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    registers_date = []
    for row in data:
        date = row[2].split('-')
        registers_date.append(date)

    registers_by_month = Counter()

    for row in registers_date:
        registers_by_month[row[1]] += 1

    registers_by_month_tuples = list(registers_by_month.items())
    registers_by_month_tuples = sorted(registers_by_month_tuples)

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
    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    set_letters = []
    for row in data:
        letter = row[0]
        if letter not in set_letters:
            set_letters.append(letter)

    min_value_letter = []
    max_value_letter = []
    for letter in set_letters:
        values_letter = []
        for row in data:
            if row[0] == letter:
                values_letter.append(int(row[1]))
        max_value = None
        min_value = None
        for num in values_letter:
            if max_value is None or num > max_value:
                max_value = num
            if min_value is None or num < min_value:
                min_value = num
        min_value_letter.append(min_value)
        max_value_letter.append(max_value)

    tuple_min_max = list(zip(set_letters, max_value_letter, min_value_letter))
    tuple_min_max = sorted(tuple_min_max)

    return tuple_min_max


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
    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    key_value_dict = []
    for row in data:
        key_dict = row[4].split(',')
        for element in key_dict:
            elements_dict = element.split(':')
            key_value_dict.append([elements_dict[0], int(elements_dict[1])])

    set_keys = []
    for row in key_value_dict:
        value_key = row[0]
        if value_key not in set_keys:
            set_keys.append(value_key)

    min_value_key = []
    max_value_key = []
    for key in set_keys:
        values_key = []
        for row in key_value_dict:
            if row[0] == key:
                values_key.append(row[1])
        max_value = None
        min_value = None
        for num in values_key:
            if max_value is None or num > max_value:
                max_value = num
            if min_value is None or num < min_value:
                min_value = num
        min_value_key.append(min_value)
        max_value_key.append(max_value)

    tuple_min_max = list(zip(set_keys, min_value_key, max_value_key))
    tuple_min_max = sorted(tuple_min_max)

    return tuple_min_max


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
    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    set_numbers = []
    for row in data:
        number = int(row[1])
        if number not in set_numbers:
            set_numbers.append(number)

    numbers_letters = []
    for number in set_numbers:
        letters = []
        for row in data:
            if int(row[1]) == number:
                letters.append(row[0])
        numbers_letters.append(letters)

    numbers_letters_tuple = list(zip(set_numbers, numbers_letters))
    numbers_letters_tuple = sorted(numbers_letters_tuple)

    return numbers_letters_tuple


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
    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    set_numbers = []
    for row in data:
        number = int(row[1])
        if number not in set_numbers:
            set_numbers.append(number)

    numbers_letters = []
    for number in set_numbers:
        letters = []
        for row in data:
            if int(row[1]) == number:
                if row[0] not in letters:
                    letters.append(row[0])
                    letters = sorted(letters)
        numbers_letters.append(letters)

    numbers_letters_tuple = list(zip(set_numbers, numbers_letters))
    numbers_letters_tuple = sorted(numbers_letters_tuple)

    return numbers_letters_tuple


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
    from collections import Counter

    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    key_value_dict = []
    for row in data:
        key_dict = row[4].split(',')
        for element in key_dict:
            elements_dict = element.split(':')
            key_value_dict.append([elements_dict[0], int(elements_dict[1])])

    count_key = Counter()
    for row in key_value_dict:
        count_key[row[0]] += 1

    count_key = dict(count_key)

    count_key = {key: value for key, value in sorted(count_key.items(), key=lambda item: item[0])}

    return count_key


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
    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    def total_elements(data_list):
        count = 0
        for element in data_list:
            count += 1
        return count

    letters = []
    count_col4 = []
    count_col5 = []
    for row in data:
        col4 = total_elements(row[3].split(','))
        col5 = total_elements(row[4].split(','))
        letters.append(row[0])
        count_col4.append(col4)
        count_col5.append(col5)

    result = list(zip(letters, count_col4, count_col5))

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

    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    data_letters = []
    for row in data:
        letters = row[3].split(',')
        for element in letters:
            set_elements = [element, row[1]]
            data_letters.append(set_elements)

    set_letters = []
    for row in data_letters:
        letter = row[0]
        if letter not in set_letters:
            set_letters.append(letter)

    sum_letters = []
    for letter in set_letters:
        sum_letter = 0
        for row in data_letters:
            if row[0] == letter:
                sum_letter = sum_letter + int(row[1])
        sum_letters.append(sum_letter)

    my_dict = dict(zip(set_letters, sum_letters))
    my_dict = {key: value for key, value in sorted(my_dict.items(), key=lambda item: item[0])}

    return my_dict


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
    data = open("data.csv")
    data = [line.replace("\n", "") for line in data]
    data = [line.split('\t') for line in data]

    data_letters = []
    for row in data:
        letters = row[4].split(',')
        for element in letters:
            split_element = int(element.split(':')[1])
            set_elements = [row[0], split_element]
            data_letters.append(set_elements)

    set_letters = []
    for row in data_letters:
        letter = row[0]
        if letter not in set_letters:
            set_letters.append(letter)

    sum_letters = []
    for letter in set_letters:
        sum_letter = 0
        for row in data_letters:
            if row[0] == letter:
                sum_letter = sum_letter + int(row[1])
        sum_letters.append(sum_letter)

    my_dict = dict(zip(set_letters, sum_letters))
    my_dict = {key: value for key, value in sorted(my_dict.items(), key=lambda item: item[0])}

    return my_dict
