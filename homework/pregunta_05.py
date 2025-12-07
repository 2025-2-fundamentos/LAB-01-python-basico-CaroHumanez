"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    ruta = './files/input/data.csv'
    resultados = {}

    with open(ruta, mode='r', encoding='utf-8') as archivo:
        for linea in archivo:
            columnas = linea.strip().split()
            letra = columnas[0]
            valor = int(columnas[1])

            if letra in resultados:
                resultados[letra][0] = max(resultados[letra][0], valor)
                resultados[letra][1] = min(resultados[letra][1], valor)
            else:
                resultados[letra] = [valor, valor]

    # Convertir a lista de tuplas y ordenar alfabéticamente
    return sorted((letra, max_val, min_val) for letra, (max_val, min_val) in resultados.items())
