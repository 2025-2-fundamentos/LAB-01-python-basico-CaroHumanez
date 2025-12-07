"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    ruta = "./files/input/data.csv"
    resultado = []

    with open(ruta, "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")

            letra = columnas[0]
            elementos_col4 = columnas[3].count(",") + 1 if columnas[3] else 0
            elementos_col5 = columnas[4].count(",") + 1 if columnas[4] else 0

            resultado.append((letra, elementos_col4, elementos_col5))

    return resultado
