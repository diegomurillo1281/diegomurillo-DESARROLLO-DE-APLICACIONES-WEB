import os
import mysql.connector

# Leer configuración desde variables de entorno
conexion = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", 3306)),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database=os.getenv("DB_NAME", "tienda_estilo_urbano")
)

# =============================================================================
# 🔧 CONFIGURACIÓN DE BASE DE DATOS (DINÁMICA - Funciona en local y Render)
# =============================================================================

def get_db_connection():
    """
    Crea y retorna una nueva conexión a MySQL.
    Usa variables de entorno en Render, valores por defecto en local.
    """
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "tienda_estilo_urbano")
    )

def close_db_connection(conn):
    """Cierra la conexión de forma segura"""
    if conn and conn.is_connected():
        conn.close()

# =============================================================================
# 🏠 RUTAS PRINCIPALES
# =============================================================================

@app.route('/')
def home():
    """Página de inicio"""
    return render_template('index.html')

@app.route('/test-db')
def test_db():
    """
    Ruta de prueba para verificar conexión a MySQL.
    Accede a: https://tu-app.onrender.com/test-db
    """
    conn = None
    try:
        conn = get_db_connection()
        if conn.is_connected():
            return jsonify({
                "status": "success",
                "message": "✅ Conexión a MySQL exitosa!",
                "host": os.getenv("DB_HOST", "localhost"),
                "database": os.getenv("DB_NAME", "tienda_estilo_urbano")
            })
    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": f"❌ Error: {str(err)}"}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": f"❌ Error inesperado: {str(e)}"}), 500
    finally:
        close_db_connection(conn)

# =============================================================================
# 🔐 AUTENTICACIÓN
# =============================================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Formulario y lógica de login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            
            # 🔐 Consulta segura con parámetros
            query = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            usuario = cursor.fetchone()
            
            if usuario:
                session['user_id'] = usuario['id']
                session['user_email'] = usuario['email']
                flash('✅ Login exitoso', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('❌ Credenciales incorrectas', 'error')
                return redirect(url_for('login'))
                
        except mysql.connector.Error as err:
            flash(f'❌ Error de base de datos: {err}', 'error')
            return redirect(url_for('login'))
        finally:
            if conn and conn.is_connected():
                cursor.close()
                close_db_connection(conn)
    
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """Formulario y lógica de registro"""
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # 🔐 Insertar nuevo usuario con parámetros
            query = "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre, email, password))
            conn.commit()
            
            flash('✅ Registro exitoso. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
            
        except mysql.connector.Error as err:
            flash(f'❌ Error: {err}', 'error')
            return redirect(url_for('registro'))
        finally:
            if conn and conn.is_connected():
                cursor.close()
                close_db_connection(conn)
    
    return render_template('registro.html')

@app.route('/logout')
def logout():
    """Cerrar sesión"""
    session.clear()
    flash('👋 Sesión cerrada', 'info')
    return redirect(url_for('login'))

# =============================================================================
# 📦 PRODUCTOS
# =============================================================================

@app.route('/productos')
def listar_productos():
    """Listar todos los productos"""
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM productos ORDER BY nombre")
        productos = cursor.fetchall()
        
        return render_template('productos.html', productos=productos)
        
    except mysql.connector.Error as err:
        flash(f'❌ Error: {err}', 'error')
        return render_template('productos.html', productos=[])
    finally:
        if conn and conn.is_connected():
            cursor.close()
            close_db_connection(conn)

@app.route('/producto/<int:id>')
def ver_producto(id):
    """Ver detalle de un producto"""
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        producto = cursor.fetchone()
        
        if producto:
            return render_template('producto_detalle.html', producto=producto)
        else:
            flash('❌ Producto no encontrado', 'error')
            return redirect(url_for('listar_productos'))
            
    except mysql.connector.Error as err:
        flash(f'❌ Error: {err}', 'error')
        return redirect(url_for('listar_productos'))
    finally:
        if conn and conn.is_connected():
            cursor.close()
            close_db_connection(conn)

@app.route('/producto/agregar', methods=['POST'])
def agregar_producto():
    """Agregar nuevo producto (API)"""
    if not session.get('user_id'):
        return jsonify({"error": "No autorizado"}), 401
    
    data = request.get_json()
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """INSERT INTO productos (nombre, descripcion, precio, stock, imagen) 
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (
            data.get('nombre'),
            data.get('descripcion'),
            data.get('precio'),
            data.get('stock', 0),
            data.get('imagen', '')
        ))
        conn.commit()
        
        return jsonify({"status": "success", "id": cursor.lastrowid}), 201
        
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if conn and conn.is_connected():
            cursor.close()
            close_db_connection(conn)

# =============================================================================
# 👥 USUARIOS (Admin)
# =============================================================================

@app.route('/usuarios')
def listar_usuarios():
    """Listar usuarios (solo admin)"""
    if not session.get('user_id'):
        return redirect(url_for('login'))
    
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT id, nombre, email, created_at FROM usuarios ORDER BY created_at DESC")
        usuarios = cursor.fetchall()
        
        return render_template('usuarios.html', usuarios=usuarios)
        
    except mysql.connector.Error as err:
        flash(f'❌ Error: {err}', 'error')
        return render_template('usuarios.html', usuarios=[])
    finally:
        if conn and conn.is_connected():
            cursor.close()
            close_db_connection(conn)

# =============================================================================
# 🛒 CARRITO (Ejemplo básico)
# =============================================================================

@app.route('/carrito')
def ver_carrito():
    """Ver carrito de compras"""
    carrito = session.get('carrito', [])
    
    if not carrito:
        return render_template('carrito.html', items=[], total=0)
    
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Obtener detalles de productos en el carrito
        placeholders = ','.join(['%s'] * len(carrito))
        query = f"SELECT * FROM productos WHERE id IN ({placeholders})"
        cursor.execute(query, list(carrito.keys()))
        productos = cursor.fetchall()
        
        # Calcular totales
        total = sum(
            producto['precio'] * carrito[producto['id']] 
            for producto in productos
        )
        
        return render_template('carrito.html', items=productos, carrito=carrito, total=total)
        
    except mysql.connector.Error as err:
        flash(f'❌ Error: {err}', 'error')
        return render_template('carrito.html', items=[], total=0)
    finally:
        if conn and conn.is_connected():
            cursor.close()
            close_db_connection(conn)

@app.route('/carrito/agregar/<int:producto_id>', methods=['POST'])
def agregar_al_carrito(producto_id):
    """Agregar producto al carrito (sesión)"""
    if 'carrito' not in session:
        session['carrito'] = {}
    
    carrito = session['carrito']
    carrito[str(producto_id)] = carrito.get(str(producto_id), 0) + 1
    session.modified = True
    
    flash('✅ Producto agregado al carrito', 'success')
    return redirect(url_for('listar_productos'))

# =============================================================================
# ⚙️ CONFIGURACIÓN PARA RENDER
# =============================================================================

@app.errorhandler(404)
def not_found(error):
    """Manejar errores 404"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Manejar errores 500"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # 🎯 Puerto dinámico para Render + host 0.0.0.0 obligatorio
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)