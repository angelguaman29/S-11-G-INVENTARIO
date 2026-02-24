# Sistema de Gestion de Inventario - Version con Colecciones

## Descripcion
Sistema de gestion de inventarios
Incorpora colecciones de Python (diccionarios, listas, conjuntos
y tuplas) para un manejo eficiente de los datos del inventario.

## Como ejecutar el programa
```bash
python main.py
```

## Estructura del proyecto
```
S-11-G-INVENTARIO/
├── modelos/
│   └── producto.py           (Clase Producto con getters y setters)
├── servicios/
│   ├── gestor_archivos.py    (Lectura y escritura del archivo inventario.txt)
│   └── inventario.py         (Clase Inventario con diccionario y colecciones)
├── main.py                   (Menu interactivo principal)
├── inventario.txt            (Se crea automaticamente al agregar productos)
└── README.md
```

## Colecciones utilizadas

**Diccionario** - estructura principal del inventario en `inventario.py`.
La clave es el ID y el valor es el objeto Producto. Permite buscar,
actualizar y eliminar de forma directa sin recorrer toda la coleccion.

**Conjunto** - guarda los IDs registrados para validar duplicados
rapidamente sin necesidad de recorrer el diccionario.

**Lista** - se usa para acumular resultados de busqueda por nombre
y para convertir el diccionario al momento de guardar en archivo.

**Tupla** - agrupa los datos del producto antes de crear el objeto
en el metodo agregar_producto.

## Almacenamiento persistente
Los productos se guardan automaticamente en `inventario.txt` cada vez
que se agrega, elimina o actualiza un producto. Al iniciar el programa
los datos se cargan automaticamente desde ese archivo.

Formato del archivo:
```
1|Celular Samsung|10|500.99
2|Television LG|5|800.99
```

## Manejo de excepciones
El programa maneja errores como archivo no encontrado, datos corruptos
y falta de permisos mediante bloques try/except en GestorArchivos.