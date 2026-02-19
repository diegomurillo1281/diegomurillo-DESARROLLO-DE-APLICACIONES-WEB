from flask import Flask, render_template

# ESTA LÍNEA ES LA QUE FALTA (La que busca Render)
app = Flask(__name__)

# Tu base de datos corregida
productos = [
    {
        "id": 1,
        "nombre": "Camiseta Oversize Urban Black",
        "marca": "TrendVibe",
        "precio": 29.99,
        "descripcion": "Camiseta oversize color negro, estilo urbano moderno, 100% algodón premium, ideal para outfits casuales.",
        "colores": ["Negro", "Blanco", "Gris"],
        "tallas": ["S", "M", "L", "XL"],
        "stock": 18
    },
    {
        "id": 2,
        "nombre": "Jeans Slim Fit Blue Classic",
        "marca": "DenimPro",
        "precio": 49.99,
        "descripcion": "Jeans slim fit azul clásico con tela stretch de alta resistencia y costuras reforzadas.",
        "colores": ["Azul Oscuro", "Azul Claro"],
        "tallas": ["28", "30", "32", "34", "36"],
        "stock": 12
    },
    {
        "id": 3,
        "nombre": "Chaqueta de Cuero Premium Rider",
        "marca": "TrendVibe",
        "precio": 85.00,
        "descripcion": "Chaqueta de cuero sintético premium con forro térmico y cierres reforzados.",
        "colores": ["Negro", "Café"],
        "tallas": ["M", "L", "XL"],
        "stock": 5
    }
]

@app.route('/')
def inicio():
    return "¡Tienda TrendVibe en línea!"

if __name__ == '__main__':
    app.run(debug=True)