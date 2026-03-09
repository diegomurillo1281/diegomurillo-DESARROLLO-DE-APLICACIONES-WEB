import mysql.connector

def conectar_mysql():
try:
conexion = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="tienda_estilo_urbano"
)
if conexion.is_connected():
print("Conexión exitosa a MySQL")
return conexion
except mysql.connector.Error as e:
print("Error al conectar:", e)
return None