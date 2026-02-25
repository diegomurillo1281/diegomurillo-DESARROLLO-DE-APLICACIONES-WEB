import sqlite3
import os

# Ruta compatible con Render
DB_PATH = os.path.join("/tmp", "database.db")


# -----------------------------
# CLASE PRODUCTO
# -----------------------------
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio


# -----------------------------
# CLASE INVENTARIO
# -----------------------------
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}
        self.conectar_db()
        self.cargar_productos()

    def conectar_db(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        """)
        self.conn.commit()

    def cargar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()

        for row in rows:
            producto = Producto(row[0], row[1], row[2], row[3])
            self.productos[row[0]] = producto

    # CRUD

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

            self.productos[id].set_nombre(nombre)
            self.productos[id].set_cantidad(cantidad)
            self.productos[id].set_precio(precio)

    def obtener_producto(self, id):
        return self.productos.get(id)

    def obtener_todos(self):
        return self.productos.values()

    def buscar_por_nombre(self, nombre):
        return [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]