import os

ruta_txt = "inventario/data/datos.txt"

def guardar_txt(nombre, precio):

    with open(ruta_txt, "a") as archivo:
        archivo.write(f"{nombre},{precio}\n")


def leer_txt():

    datos = []

    if os.path.exists(ruta_txt):

        with open(ruta_txt, "r") as archivo:

            for linea in archivo:
                nombre, precio = linea.strip().split(",")
                datos.append({
                    "nombre": nombre,
                    "precio": precio
                })

    return datos