import sqlite3

class Producto:

    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    @staticmethod
    def conectar():
        return sqlite3.connect("database.db")

    @staticmethod
    def crear_tabla():
        conn = Producto.conectar()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():
        conn = Producto.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        filas = cursor.fetchall()
        conn.close()

        productos = []
        for fila in filas:
            productos.append(Producto(fila[0], fila[1], fila[2]))

        return productos

    @staticmethod
    def insertar(nombre, precio):
        conn = Producto.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id):
        conn = Producto.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def obtener_por_id(id):
        conn = Producto.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        fila = cursor.fetchone()
        conn.close()

        if fila:
            return Producto(fila[0], fila[1], fila[2])
        return None

    @staticmethod
    def actualizar(id, nombre, precio):
        conn = Producto.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET nombre = ?, precio = ? WHERE id = ?",
            (nombre, precio, id)
        )
        conn.commit()
        conn.close()