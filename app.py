from flask import Flask, render_template, request, redirect, url_for
from models import Inventario

app = Flask(__name__)
inventario = Inventario()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/productos")
def productos():
    lista_productos = inventario.obtener_todos()
    return render_template("productos.html", productos=lista_productos)


@app.route("/agregar", methods=["GET", "POST"])
def agregar_producto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = int(request.form["cantidad"])
        precio = float(request.form["precio"])

        inventario.agregar_producto(nombre, cantidad, precio)
        return redirect(url_for("productos"))

    return render_template("agregar_producto.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_producto(id):
    producto = inventario.obtener_producto(id)

    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = int(request.form["cantidad"])
        precio = float(request.form["precio"])

        inventario.actualizar_producto(id, nombre, cantidad, precio)
        return redirect(url_for("productos"))

    return render_template("editar_producto.html", producto=producto)


@app.route("/eliminar/<int:id>")
def eliminar_producto(id):
    inventario.eliminar_producto(id)
    return redirect(url_for("productos"))


if __name__ == "__main__":
    app.run(debug=True)