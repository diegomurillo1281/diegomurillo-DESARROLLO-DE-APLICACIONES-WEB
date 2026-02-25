import sqlite3


# =========================
# CLASE PRODUCTO
# =========================
class Producto:

    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


# =========================
# CLASE INVENTARIO
# =========================
class Inventario:

    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}
        self.conectar_db()
        self.crear_tabla()
        self.cargar_productos()

    # --------- SQLITE ---------

    def conectar_db(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        """)
        self.conn.commit()

    # --------- CARGAR DESDE BD A DICCIONARIO ---------

    def cargar_productos(self):
    self.cursor.execute("SELECT * FROM productos")
    filas = self.cursor.fetchall()

    for fila in filas:
        producto = Producto(fila[0], fila[1], fila[2], fila[3])
        self.productos[fila[0]] = producto

    # 🔥 SI ESTÁ VACÍA, INSERTAR PRODUCTOS AUTOMÁTICOS
    if len(self.productos) == 0:
        print("Base de datos vacía. Insertando productos iniciales...")

        self.agregar_producto("Camisa Urbana", 15, 29.99)
        self.agregar_producto("Pantalón Slim Fit", 10, 49.99)
        self.agregar_producto("Chaqueta Streetwear", 8, 79.99)

    # --------- CRUD ---------

    def agregar_producto(self, nombre, cantidad, precio):
        self.cursor.execute(
            "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
            (nombre, cantidad, precio)
        )
        self.conn.commit()

        nuevo_id = self.cursor.lastrowid
        producto = Producto(nuevo_id, nombre, cantidad, precio)
        self.productos[nuevo_id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            self.cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
            self.conn.commit()
            del self.productos[id]

    def actualizar_producto(self, id, nombre, cantidad, precio):
        if id in self.productos:
            self.cursor.execute("""
                UPDATE productos
                SET nombre = ?, cantidad = ?, precio = ?
                WHERE id = ?
            """, (nombre, cantidad, precio, id))
            self.conn.commit()

            self.productos[id].nombre = nombre
            self.productos[id].cantidad = cantidad
            self.productos[id].precio = precio

    def buscar_por_nombre(self, nombre):
        return [
            p for p in self.productos.values()
            if nombre.lower() in p.nombre.lower()
        ]

    def mostrar_todos(self):
        return list(self.productos.values())