from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/producto/<nombre>')
def ver_producto(nombre):
    # Pasamos la variable 'nombre' a la plantilla
    return render_template('producto.html', producto=nombre)

if __name__ == '__main__':
    app.run(debug=True)