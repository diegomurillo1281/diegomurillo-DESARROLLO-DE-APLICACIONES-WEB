import os
import json
import csv

ruta_txt = "inventario/data/datos.txt"
ruta_json = "inventario/data/datos.json"
ruta_csv = "inventario/data/datos.csv"


# ================= TXT =================

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


# ================= JSON =================

def guardar_json(nombre, precio):

    datos = []

    if os.path.exists(ruta_json):

        with open(ruta_json, "r") as archivo:

            try:
                datos = json.load(archivo)
            except:
                datos = []

    nuevo = {
        "nombre": nombre,
        "precio": precio
    }

    datos.append(nuevo)

    with open(ruta_json, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def leer_json():

    if os.path.exists(ruta_json):

        with open(ruta_json, "r") as archivo:
            return json.load(archivo)

    return []


# ================= CSV =================

def guardar_csv(nombre, precio):

    with open(ruta_csv, "a", newline="") as archivo:

        writer = csv.writer(archivo)

        writer.writerow([nombre, precio])


def leer_csv():

    datos = []

    if os.path.exists(ruta_csv):

        with open(ruta_csv, "r") as archivo:

            reader = csv.reader(archivo)

            for fila in reader:

                datos.append({
                    "nombre": fila[0],
                    "precio": fila[1]
                })

    return datos