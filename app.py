from flask import Flask, render_template, request, redirect, url_for
from models import Inventario

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
# AGREGAR (CORREGIDO)
# =========================
@app.route("/agregar", methods=["GET", "POST"])
def agregar_producto():
    if request.method == "POST":
        # Usamos .get para evitar el "Bad Request" si falta un campo
        nombre = request.form.get("nombre")
        cantidad = request.form.get("cantidad")
        precio = request.form.get("precio")

        # Validación básica: si todo existe, guardamos
        if nombre and cantidad and precio:
            inventario.agregar_producto(nombre, int(cantidad), float(precio))
            return redirect(url_for("listar_productos"))
        else:
            return "Error: Faltan campos en el formulario", 400

    return render_template("agregar_producto.html")

# =========================
# EDITAR (CORREGIDO)
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
# ELIMINAR
# =========================
@app.route("/eliminar/<int:id>")
def eliminar_producto(id):
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

if __name__ == "__main__":
    app.run(debug=True)


# =========================
# FACTURA
# =========================
@app.route("/factura")
def factura():
    return render_template("factura.html")