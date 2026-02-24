# Maneja la lectura y escritura del archivo inventario.txt
# Incluye manejo de excepciones para errores comunes de archivos.

from modelos.producto import Producto


class GestorArchivos:
    """Clase encargada de guardar y cargar productos desde un archivo de texto."""

    def __init__(self, nombre_archivo):
        # Guardamos el nombre del archivo que vamos a usar
        self._nombre_archivo = nombre_archivo

    def guardar_productos(self, lista_productos):
        """
        Guarda todos los productos en el archivo.
        Formato de cada linea: ID|Nombre|Cantidad|Precio
        """
        try:
            with open(self._nombre_archivo, "w") as archivo:
                for producto in lista_productos:
                    linea = (f"{producto.obtener_id()}|"
                             f"{producto.obtener_nombre()}|"
                             f"{producto.obtener_cantidad()}|"
                             f"{producto.obtener_precio()}\n")
                    archivo.write(linea)
            print("Datos guardados en archivo correctamente.")
        except PermissionError:
            print("Error: no hay permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar_productos(self):
        """
        Carga los productos desde el archivo al iniciar el programa.
        Si el archivo no existe, retorna una lista vacia.
        """
        productos = []
        try:
            with open(self._nombre_archivo, "r") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        partes = linea.split("|")
                        # Validamos que la linea tenga los 4 datos esperados
                        if len(partes) == 4:
                            id_p = int(partes[0])
                            nombre = partes[1]
                            cantidad = int(partes[2])
                            precio = float(partes[3])
                            productos.append(Producto(id_p, nombre, cantidad, precio))
        except FileNotFoundError:
            # Si el archivo no existe aun, simplemente retornamos lista vacia
            print("Archivo de inventario no encontrado. Se creara uno nuevo.")
        except PermissionError:
            print("Error: no hay permisos para leer el archivo.")
        except Exception as e:
            print(f"Error al cargar datos: {e}")
        return productos