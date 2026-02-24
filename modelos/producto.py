# Representa un producto del inventario.
# Usa encapsulamiento con atributos privados y metodos getter/setter.

class Producto:
    """Clase que representa un producto de la tienda."""

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados del producto
        self._id = id_producto        # ID unico del producto (entero)
        self._nombre = nombre         # Nombre del producto (texto)
        self._cantidad = cantidad     # Cantidad disponible (entero)
        self._precio = precio         # Precio unitario (decimal)

    # Metodos getter: permiten obtener el valor de cada atributo
    def obtener_id(self):
        return self._id

    def obtener_nombre(self):
        return self._nombre

    def obtener_cantidad(self):
        return self._cantidad

    def obtener_precio(self):
        return self._precio

    # Metodos setter: permiten cambiar el valor de cada atributo con validacion
    def establecer_nombre(self, nuevo_nombre):
        if nuevo_nombre:
            self._nombre = nuevo_nombre

    def establecer_cantidad(self, nueva_cantidad):
        # La cantidad no puede ser negativa
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad

    def establecer_precio(self, nuevo_precio):
        # El precio debe ser mayor a cero
        if nuevo_precio > 0:
            self._precio = nuevo_precio