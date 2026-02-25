from flask import Flask, render_template, redirect, url_for, request
from models import Inventario, Producto

app = Flask(__name__)

inventario = Inventario()


# =============================
# RUTAS BÁSICAS
# =============================

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# =============================
# MOSTRAR PRODUCTOS (READ)
# =============================

@app.route('/productos')
def productos():
    productos = inventario.mostrar_todos()
    return render_template('productos.html', productos=productos)


# =============================
# AGREGAR PRODUCTO (CREATE)
# =============================

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    precio = float(request.form['precio'])

    nuevo_producto = Producto(None, nombre, cantidad, precio)
    inventario.añadir_producto(nuevo_producto)

    return redirect(url_for('productos'))


# =============================
# ELIMINAR PRODUCTO (DELETE)
# =============================

@app.route('/eliminar/<int:id>')
def eliminar(id):
    inventario.eliminar_producto(id)
    return redirect(url_for('productos'))


# =============================
# ACTUALIZAR PRODUCTO (UPDATE)
# =============================

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    cantidad = int(request.form['cantidad'])
    precio = float(request.form['precio'])

    inventario.actualizar_producto(id, cantidad, precio)

    return redirect(url_for('productos'))


if __name__ == '__main__':
    app.run(debug=True)