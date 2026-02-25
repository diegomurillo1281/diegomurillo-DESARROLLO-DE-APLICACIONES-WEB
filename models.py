import sqlite3

# ===============================
# CLASE PRODUCTO (POO)
# ===============================

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_tuple(self):
        return (self.id, self.nombre, self.cantidad, self.precio)


# ===============================
# CLASE INVENTARIO (POO + Colecciones)
# ===============================

class Inventario:

    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}
        self.conectar_db()
        self.cargar_productos()

    def conectar_db(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                cantidad INTEGER,
                precio REAL
            )
        """)
        self.conn.commit()

    # ================= CRUD =================

    def añadir_producto(self, producto):
        self.productos[producto.id] = producto

        self.cursor.execute(
            "INSERT INTO productos VALUES (?, ?, ?, ?)",
            producto.to_tuple()
        )
        self.conn.commit()

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

        self.cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        self.conn.commit()

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio

        self.cursor.execute("""
            UPDATE productos
            SET cantidad = ?, precio = ?
            WHERE id = ?
        """, (cantidad, precio, id))
        self.conn.commit()

    def buscar_por_nombre(self, nombre):
        self.cursor.execute(
            "SELECT * FROM productos WHERE nombre LIKE ?",
            ('%' + nombre + '%',)
        )
        return self.cursor.fetchall()

    def mostrar_todos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def cargar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        filas = self.cursor.fetchall()

        for fila in filas:
            producto = Producto(*fila)
            self.productos[producto.id] = producto