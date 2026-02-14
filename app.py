from flask import Flask, render_template
import os

# Inicializamos la aplicación
app = Flask(__name__)

# RUTA 1: Página de inicio (Tu tienda de ropa)
@app.route('/')
def home():
    # Flask buscará el archivo index.html dentro de la carpeta 'templates'
    return render_template('index.html')

# RUTA 2: Página de Login
@app.route('/login')
def login():
    # Flask buscará el archivo login.html dentro de la carpeta 'templates'
    return render_template('login.html')

# Configuración para que Render pueda asignar el puerto automáticamente
if __name__ == "__main__":
    # Render usa la variable de entorno PORT, si no existe usa el 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)