from models import Inventario

# Crear inventario
inventario = Inventario()


def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto por nombre")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")


def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
            print("✅ Producto agregado correctamente.")

        elif opcion == "2":
            productos = inventario.mostrar_todos()
            print("\n--- LISTA DE PRODUCTOS ---")
            for producto in productos:
                print(producto)

        elif opcion == "3":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            print("\n--- RESULTADOS ---")
            for producto in resultados:
                print(producto)

        elif opcion == "4":
            id_producto = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_producto, nombre, cantidad, precio)
            print("✅ Producto actualizado.")

        elif opcion == "5":
            id_producto = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)
            print("✅ Producto eliminado.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    ejecutar()