# DICCIONARIO como estructura principal.
# Tambien usa CONJUNTO para validar IDs, LISTA para resultados y TUPLA en creacion.

from modelos.producto import Producto
from servicios.gestor_archivos import GestorArchivos


class Inventario:
    """
    Clase que gestiona todos los productos de la tienda.
    Usa un diccionario como estructura principal de almacenamiento.
    La clave del diccionario es el ID del producto (unico).
    """

    def __init__(self):
        # DICCIONARIO: estructura principal del inventario
        # Clave: ID del producto (int) | Valor: objeto Producto
        self._productos = {}

        # CONJUNTO: guarda los IDs para verificar duplicados rapidamente
        # Los conjuntos no permiten valores repetidos, ideal para IDs unicos
        self._ids_registrados = set()

        # Creamos el gestor de archivos para guardar y cargar datos
        self._gestor = GestorArchivos("inventario.txt")

        # Cargamos los productos guardados cuando inicia el programa
        self._cargar_productos_del_archivo()

    def _cargar_productos_del_archivo(self):
        """Carga los productos desde el archivo y los guarda en el diccionario."""
        productos_cargados = self._gestor.cargar_productos()
        for producto in productos_cargados:
            id_producto = producto.obtener_id()
            # Guardamos en el diccionario con el ID como clave
            self._productos[id_producto] = producto
            # Registramos el ID en el conjunto
            self._ids_registrados.add(id_producto)

    def _guardar_en_archivo(self):
        """Convierte el diccionario a lista y guarda en el archivo."""
        # LISTA: convertimos los valores del diccionario para poder guardarlos
        lista_productos = list(self._productos.values())
        self._gestor.guardar_productos(lista_productos)

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Agrega un nuevo producto. Valida que el ID no exista antes."""
        # Verificamos en el CONJUNTO si el ID ya existe (muy rapido)
        if id_producto in self._ids_registrados:
            return False, "El ID ya existe en el inventario."

        # TUPLA: agrupamos los datos del producto antes de crear el objeto
        datos_producto = (id_producto, nombre, cantidad, precio)
        nuevo_producto = Producto(*datos_producto)

        # Guardamos en el DICCIONARIO con el ID como clave
        self._productos[id_producto] = nuevo_producto
        self._ids_registrados.add(id_producto)

        self._guardar_en_archivo()
        return True, "Producto agregado y guardado en archivo correctamente."

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto not in self._ids_registrados:
            return False, "No se encontro un producto con ese ID."

        # Eliminamos del DICCIONARIO directamente por clave
        del self._productos[id_producto]
        self._ids_registrados.discard(id_producto)

        self._guardar_en_archivo()
        return True, "Producto eliminado y archivo actualizado correctamente."

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o precio de un producto existente."""
        if id_producto not in self._ids_registrados:
            return False, "No se encontro un producto con ese ID."

        # Accedemos directamente al producto por clave del DICCIONARIO
        producto = self._productos[id_producto]

        if nueva_cantidad is not None:
            producto.establecer_cantidad(nueva_cantidad)
        if nuevo_precio is not None:
            producto.establecer_precio(nuevo_precio)

        self._guardar_en_archivo()
        return True, "Producto actualizado y archivo guardado correctamente."

    def buscar_por_nombre(self, nombre_busqueda):
        """Busca productos por nombre. Permite coincidencias parciales."""
        # LISTA: acumulamos los productos que coinciden con la busqueda
        resultados = []
        for producto in self._productos.values():
            if nombre_busqueda.lower() in producto.obtener_nombre().lower():
                resultados.append(producto)
        return resultados

    def obtener_todos(self):
        """Retorna todos los productos del inventario como lista."""
        return list(self._productos.values())

    def esta_vacio(self):
        """Retorna True si no hay productos en el inventario."""
        return len(self._productos) == 0

    def contar_productos(self):
        """Retorna el numero total de productos registrados."""
        return len(self._productos)