from flask import Flask, render_template

# Esta es la línea que le falta a tu código
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Esto es lo que ya tienes al final
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)