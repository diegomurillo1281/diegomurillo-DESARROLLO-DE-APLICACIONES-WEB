from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# =========================
# CONEXIÓN MYSQL
# =========================

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tienda_estilo_urbano"
)

cursor = conexion.cursor(dictionary=True)

# =========================
# INICIO
# =========================

@app.route("/")
def index():
    return redirect(url_for("productos_mysql"))

# =========================
# MOSTRAR PRODUCTOS
# =========================

@app.route("/productos_mysql")
def productos_mysql():

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    return render_template("productos_mysql.html", productos=productos)

# =========================
# AGREGAR PRODUCTO
# =========================

@app.route("/agregar_producto_mysql", methods=["GET","POST"])
def agregar_producto_mysql():

    if request.method == "POST":

        nombre = request.form["nombre"]
        precio = request.form["precio"]

        sql = "INSERT INTO productos (nombre, precio) VALUES (%s,%s)"
        valores = (nombre, precio)

        cursor.execute(sql, valores)
        conexion.commit()

        return redirect(url_for("productos_mysql"))

    return render_template("agregar_producto.html")

# =========================
# EDITAR PRODUCTO
# =========================

@app.route("/editar_producto/<int:id>", methods=["GET","POST"])
def editar_producto(id):

    if request.method == "POST":

        nombre = request.form["nombre"]
        precio = request.form["precio"]

        sql = "UPDATE productos SET nombre=%s, precio=%s WHERE id=%s"
        valores = (nombre, precio, id)

        cursor.execute(sql, valores)
        conexion.commit()

        return redirect(url_for("productos_mysql"))

    cursor.execute("SELECT * FROM productos WHERE id=%s", (id,))
    producto = cursor.fetchone()

    return render_template("editar_producto.html", producto=producto)

# =========================
# ELIMINAR PRODUCTO
# =========================

@app.route("/eliminar_producto/<int:id>")
def eliminar_producto(id):

    cursor.execute("DELETE FROM productos WHERE id=%s", (id,))
    conexion.commit()

    return redirect(url_for("productos_mysql"))

# =========================
# FACTURA
# =========================

@app.route("/factura")
def factura():
    return render_template("factura.html")

# =========================
# SOBRE NOSOTROS
# =========================
@app.route("/about")
def about():
    return render_template("about.html")

# =========================
# LOGIN
# =========================
@app.route("/login")
def login():
    return render_template("login.html")

# =========================
# DATOS
# =========================
@app.route("/datos")
def datos():
    return render_template("datos.html")

# =========================

if __name__ == "__main__":
    app.run(debug=True)