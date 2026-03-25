# Sistema de Gestión de Inventario en Python

## Descripción
Aplicación de consola en Python que permite gestionar un inventario de productos. Incluye operaciones CRUD, cálculo de estadísticas y manejo de archivos CSV.

## Estructura del Proyecto
inventario/
├── code.py        # Menú principal  
├── funciones.py   # Lógica del inventario  
├── archivos.py    # Manejo de archivos CSV  

## Estructura de Datos
El inventario se maneja como una lista de diccionarios:

{
    "nombre": str,
    "precio": float,
    "cantidad": int
}

## Funcionalidades
- Agregar producto  
- Mostrar inventario  
- Buscar producto  
- Actualizar producto  
- Eliminar producto  
- Calcular estadísticas:
  - Unidades totales  
  - Valor total  
  - Producto más caro  
  - Producto con mayor stock  
- Guardar en CSV  
- Cargar desde CSV (sobrescribir o fusionar)

## Formato del CSV
nombre,precio,cantidad

## Ejecución
python code.py

## Validaciones
- Manejo de errores con try/except  
- Validación de datos al cargar CSV  
- Omisión de filas inválidas  

## Conceptos aplicados
- Listas y diccionarios  
- Funciones y modularización  
- Manejo de archivos  
- Control de errores  

## Autor
Luis Fuentes

# link Github 
https://github.com/langel280311-byte/inventario.git
