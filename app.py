from flask import Flask, render_template

app = Flask(__name__)

productos = [
    {
        "id": 1,
        "nombre": "Camiseta Oversize Urban Black",
        "marca": "TrendVibe",
        "precio": 29.99,
        "descripcion": "Camiseta oversize color negro, estilo urbano moderno.",
        "tallas": ["S", "M", "L", "XL"],
        "stock": 18
    },
    {
        "id": 2,
        "nombre": "Jeans Slim Fit Blue Classic",
        "marca": "DenimPro",
        "precio": 49.99,
        "descripcion": "Jeans slim fit azul clásico con tela stretch.",
        "tallas": ["28", "30", "32", "34"],
        "stock": 12
    },
    {
        "id": 3,
        "nombre": "Chaqueta de Cuero Premium Rider",
        "marca": "TrendVibe",
        "precio": 85.00,
        "descripcion": "Chaqueta de cuero sintético premium.",
        "tallas": ["M", "L", "XL"],
        "stock": 5
    }
]

@app.route('/')
def inicio():
    # Enviamos la lista 'productos' al archivo index.html
    return render_template('index.html', lista_productos=productos)

if __name__ == '__main__':
    app.run(debug=True)