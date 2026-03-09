from flask import Flask, render_template, request, redirect, url_for
from models import Inventario

# IMPORT PARA ARCHIVOS
from inventario.productos import *

app = Flask(__name__)

# Crear inventario
inventario = Inventario()

# =========================
# INICIO
# =========================
@app.route("/")
def index():
    productos = inventario.mostrar_todos()
    return render_template("index.html", productos=productos)

# =========================
# LISTAR PRODUCTOS
# =========================
@app.route("/productos")
def listar_productos():
    productos = inventario.mostrar_todos()
    return render_template("productos.html", productos=productos)

# =========================
# AGREGAR PRODUCTO
# =========================
@app.route("/agregar", methods=["GET", "POST"])
def agregar_producto():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        cantidad = request.form.get("cantidad")
        precio = request.form.get("precio")

        if nombre and cantidad and precio:
            inventario.agregar_producto(nombre, int(cantidad), float(precio))
            return redirect(url_for("listar_productos"))

        else:
            return "Error: Faltan campos en el formulario", 400

    return render_template("agregar_producto.html")

# =========================
# EDITAR PRODUCTO
# =========================
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_producto(id):

    producto = inventario.productos.get(id)

    if request.method == "POST":

        nombre = request.form.get("nombre")
        cantidad = request.form.get("cantidad")
        precio = request.form.get("precio")

        if nombre and cantidad and precio:
            inventario.actualizar_producto(id, nombre, int(cantidad), float(precio))
            return redirect(url_for("listar_productos"))

        else:
            return "Error: Faltan campos para editar", 400

    return render_template("editar_producto.html", producto=producto)

# =========================
# ELIMINAR PRODUCTO
# =========================
@app.route("/eliminar/<int:id>")
def eliminar_producto():

    inventario.eliminar_producto(id)

    return redirect(url_for("listar_productos"))

# =========================
# LOGIN
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        return redirect(url_for("index"))

    return render_template("login.html")

# =========================
# REGISTRO DE USUARIO
# =========================
@app.route("/registro_usuario", methods=["GET", "POST"])
def registro_usuario():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        email = request.form.get("email")
        password = request.form.get("password")

        # Aquí podrías guardar el usuario en base de datos
        return redirect(url_for("login"))

    return render_template("registro_usuario.html")

# =========================
# FACTURA
# =========================
@app.route("/factura")
def factura():

    return render_template("factura.html")

# =========================
# ABOUT
# =========================
@app.route("/about")
def about():

    return render_template("about.html")

# =========================
# GUARDAR DATOS EN TXT JSON CSV
# =========================
@app.route("/datos", methods=["GET", "POST"])
def datos():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        precio = request.form.get("precio")

        if nombre and precio:

            guardar_txt(nombre, precio)
            guardar_json(nombre, precio)
            guardar_csv(nombre, precio)

    datos_txt = leer_txt()
    datos_json = leer_json()
    datos_csv = leer_csv()

    return render_template(
        "datos.html",
        txt=datos_txt,
        json=datos_json,
        csv=datos_csv
    )

# =========================
# EJECUTAR APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)