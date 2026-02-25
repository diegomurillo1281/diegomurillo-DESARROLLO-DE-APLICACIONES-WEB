from flask import Flask, render_template, request, redirect
from models import Producto

app = Flask(__name__)

# Crear tabla al iniciar
Producto.crear_tabla()

@app.route("/")
def index():
    productos = Producto.obtener_todos()
    return render_template("index.html", productos=productos)

@app.route("/productos")
def listar_productos():
    productos = Producto.obtener_todos()
    return render_template("productos.html", productos=productos)

@app.route("/agregar", methods=["GET", "POST"])
def agregar_producto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = float(request.form["precio"])
        Producto.insertar(nombre, precio)
        return redirect("/productos")
    return render_template("agregar_producto.html")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_producto(id):
    producto = Producto.obtener_por_id(id)

    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = float(request.form["precio"])
        Producto.actualizar(id, nombre, precio)
        return redirect("/productos")

    return render_template("editar_producto.html", producto=producto)

@app.route("/eliminar/<int:id>")
def eliminar_producto(id):
    Producto.eliminar(id)
    return redirect("/productos")

if __name__ == "__main__":
    app.run(debug=True)