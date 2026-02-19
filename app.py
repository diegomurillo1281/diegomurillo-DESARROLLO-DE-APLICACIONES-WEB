from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal - Ahora renderiza index.html
@app.route('/')
def index():
    return render_template('index.html')

# Ruta Acerca de
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta Productos
@app.route('/productos')
def productos():
    # Datos de ejemplo para productos
    productos = [
        {'nombre': 'Camiseta Oversize', 'precio': 25.00, 'imagen': 'camiseta.jpg'},
        {'nombre': 'Jeans Slim Fit', 'precio': 45.00, 'imagen': 'jeans.jpg'},
        {'nombre': 'Chaqueta de Cuero', 'precio': 85.00, 'imagen': 'chaqueta.jpg'}
    ]
    return render_template('productos.html', productos=productos)

# Ruta Factura (ejemplo)
@app.route('/factura')
def factura():
    # Datos de ejemplo para una factura
    factura_data = {
        'cliente': 'Juan Pérez',
        'fecha': '2026-02-19',
        'productos': [
            {'nombre': 'Camiseta Oversize', 'cantidad': 2, 'precio': 25.00},
            {'nombre': 'Jeans Slim Fit', 'cantidad': 1, 'precio': 45.00}
        ],
        'total': 95.00
    }
    return render_template('factura.html', factura=factura_data)

if __name__ == '__main__':
    app.run(debug=True)