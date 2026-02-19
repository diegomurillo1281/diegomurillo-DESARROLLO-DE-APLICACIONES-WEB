from flask import Flask, render_template

app = Flask(__name__)

# Ruta Principal: Carga tu diseño de TrendVibe
@app.route('/')
def home():
    # Render busca automáticamente en la carpeta /templates
    return render_template('index.html')

# Ruta Dinámica: Detalle de producto
@app.route('/producto/<nombre>')
def ver_producto(nombre):
    # Diccionario simulado para dar una respuesta coherente al negocio
    detalles = {
        "camiseta": "Camiseta Oversize - Algodón 100% Premium. Disponible en colores neutros.",
        "jeans": "Jeans Slim Fit - Corte moderno con stretch. Tallas 28 a 36.",
        "chaqueta": "Chaqueta de Cuero - Estilo clásico con forro térmico. ¡Últimas unidades!"
    }
    
    # Buscamos si el nombre ingresado coincide con algo de nuestra "tienda"
    info = detalles.get(nombre.lower(), "Producto no encontrado en el catálogo actual.")
    
    return f"""
    <h1>TrendVibe Store - Detalle</h1>
    <p>Usted está viendo: <strong>{nombre.capitalize()}</strong></p>
    <p>Estado: {info}</p>
    <hr>
    <a href='/'>Volver al catálogo</a>
    """

if __name__ == '__main__':
    app.run(debug=True)