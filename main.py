# Menu interactivo en consola.
# Usa la clase Inventario que internamente trabaja con colecciones de Python.

from servicios.inventario import Inventario


def mostrar_menu():
    """Muestra las opciones disponibles al usuario en consola."""
    print("\n======================================")
    print("   SISTEMA DE GESTION DE INVENTARIO")
    print("======================================")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Listar todos los productos")
    print("0. Salir")
    print("--------------------------------------")


def mostrar_producto(producto):
    """Muestra la informacion de un producto en pantalla."""
    print(f"  ID: {producto.obtener_id()} | "
          f"Nombre: {producto.obtener_nombre()} | "
          f"Cantidad: {producto.obtener_cantidad()} | "
          f"Precio: {producto.obtener_precio()}")


def agregar_producto(inventario):
    """Pide los datos al usuario y agrega un nuevo producto."""
    print("\n-- Agregar Producto --")
    try:
        id_producto = int(input("ID del producto: "))
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))

        exito, mensaje = inventario.agregar_producto(id_producto, nombre, cantidad, precio)
        print(f"\n{mensaje}")
    except ValueError:
        print("\nError: ingresa valores validos (ID y cantidad enteros, precio decimal).")


def eliminar_producto(inventario):
    """Pide el ID al usuario y elimina el producto correspondiente."""
    print("\n-- Eliminar Producto --")
    try:
        id_producto = int(input("ID del producto a eliminar: "))
        exito, mensaje = inventario.eliminar_producto(id_producto)
        print(f"\n{mensaje}")
    except ValueError:
        print("\nError: el ID debe ser un numero entero.")


def actualizar_producto(inventario):
    """Permite al usuario actualizar la cantidad o precio de un producto."""
    print("\n-- Actualizar Producto --")
    try:
        id_producto = int(input("ID del producto a actualizar: "))

        nueva_cantidad = None
        nuevo_precio = None

        cambiar_cantidad = input("Actualizar cantidad? (s/n): ").strip().lower()
        if cambiar_cantidad == "s":
            nueva_cantidad = int(input("Nueva cantidad: "))

        cambiar_precio = input("Actualizar precio? (s/n): ").strip().lower()
        if cambiar_precio == "s":
            nuevo_precio = float(input("Nuevo precio: "))

        exito, mensaje = inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
        print(f"\n{mensaje}")
    except ValueError:
        print("\nError: ingresa valores validos.")


def buscar_producto(inventario):
    """Busca productos por nombre y muestra los resultados encontrados."""
    print("\n-- Buscar Producto --")
    nombre = input("Ingresa el nombre o parte del nombre: ")
    resultados = inventario.buscar_por_nombre(nombre)

    if resultados:
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        for producto in resultados:
            mostrar_producto(producto)
    else:
        print("\nNo se encontraron productos con ese nombre.")


def listar_productos(inventario):
    """Muestra todos los productos registrados en el inventario."""
    print("\n-- Lista de Productos --")
    if inventario.esta_vacio():
        print("El inventario esta vacio.")
        return

    todos = inventario.obtener_todos()
    print(f"Total de productos: {inventario.contar_productos()}")
    for producto in todos:
        mostrar_producto(producto)


def main():
    """Funcion principal que ejecuta el menu interactivo del sistema."""
    # Al crear el Inventario se cargan automaticamente los datos del archivo
    inventario = Inventario()
    print("Sistema iniciado. Productos cargados desde archivo.")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            eliminar_producto(inventario)
        elif opcion == "3":
            actualizar_producto(inventario)
        elif opcion == "4":
            buscar_producto(inventario)
        elif opcion == "5":
            listar_productos(inventario)
        elif opcion == "0":
            print("\nSaliendo del sistema. Hasta luego.")
            break
        else:
            print("\nOpcion no valida. Intenta de nuevo.")


if __name__ == "__main__":
    main()