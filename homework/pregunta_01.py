"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    import csv

    with open("archivo.csv", newline="") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

    Rta/
    214

    """
 
    ruta_archivo = './files/input/data.csv'

    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()  # Leer todas las líneas

        suma = 0
        for linea in lineas:
            columnas = linea.strip().split()  # Dividir la línea por espacios o tabulaciones
            valor = int(columnas[1])          # Obtener la segunda columna (índice 1)
            suma += valor

    return(suma)
