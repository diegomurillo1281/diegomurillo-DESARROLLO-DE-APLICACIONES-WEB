from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia
productos_lista = [
    {
        "id": 1,
        "nombre": "Camiseta Oversize",
        "precio": 25,
        "descripcion": "Camiseta urbana estilo oversize 100% algodón",
        "tallas": ["S", "M", "L", "XL"]
    },
    {
        "id": 2,
        "nombre": "Jeans Slim Fit",
        "precio": 45,
        "descripcion": "Jeans ajustados modernos color azul oscuro",
        "tallas": ["30", "32", "34", "36"]
    },
    {
        "id": 3,
        "nombre": "Chaqueta de Cuero",
        "precio": 85,
        "descripcion": "Chaqueta premium de cuero sintético",
        "tallas": ["M", "L", "XL"]
    }
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/productos")
def productos():
    return render_template("productos.html", productos=productos_lista)

@app.route("/producto/<int:id>")
def detalle(id):
    producto = next((p for p in productos_lista if p["id"] == id), None)
    return render_template("detalle.html", producto=producto)

@app.route("/factura")
def factura():
    return render_template("factura.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)