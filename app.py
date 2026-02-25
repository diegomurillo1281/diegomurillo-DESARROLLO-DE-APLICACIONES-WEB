from flask import Flask, render_template, request, redirect, url_for
from models import Inventario

app = Flask(__name__)

# Crear inventario (usa diccionario + SQLite)
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
# AGREGAR
# =========================
@app.route("/agregar", methods=["GET", "POST"])
def agregar_producto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = int(request.form["cantidad"])
        precio = float(request.form["precio"])

        inventario.agregar_producto(nombre, cantidad, precio)
        return redirect(url_for("listar_productos"))

    return render_template("agregar_producto.html")


# =========================
# EDITAR
# =========================
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_producto(id):
    producto = inventario.productos.get(id)

    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = int(request.form["cantidad"])
        precio = float(request.form["precio"])

        inventario.actualizar_producto(id, nombre, cantidad, precio)
        return redirect(url_for("listar_productos"))

    return render_template("editar_producto.html", producto=producto)


# =========================
# ELIMINAR
# =========================
@app.route("/eliminar/<int:id>")
def eliminar_producto(id):
    inventario.eliminar_producto(id)
    return redirect(url_for("listar_productos"))


if __name__ == "__main__":
    app.run(debug=True)