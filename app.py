from flask import Flask, render_template, request, redirect, url_for
from Conexion.conexion import obtener_conexion

app = Flask(__name__)

# =========================
# INICIO
# =========================
@app.route("/")
def index():
    return render_template("index.html")

# =========================
# REGISTRO DE USUARIO
# =========================
@app.route("/registro_usuario", methods=["GET","POST"])
def registro_usuario():

    if request.method == "POST":

        nombre = request.form["nombre"]
        email = request.form["email"]
        password = request.form["password"]

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = "INSERT INTO usuarios (nombre, mail, password) VALUES (%s,%s,%s)"
        valores = (nombre, email, password)

        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("ver_usuarios"))

    return render_template("registro_usuario.html")

# =========================
# VER USUARIOS
# =========================
@app.route("/usuarios")
def ver_usuarios():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("usuarios.html", usuarios=usuarios)

# =========================
# EJECUTAR APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)