# ---------------- SERVICIOS ----------------

def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario si no existe ya."""
    nombre = nombre.strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return False
    if precio < 0 or cantidad < 0:
        print("El precio y la cantidad deben ser valores no negativos.")
        return False
    if buscar_producto(inventario, nombre):
        print(f"'{nombre}' ya existe. Usa la opción actualizar.")
        return False
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    return True


def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario."""
    if not inventario:
        print("Inventario vacío.")
        return
    print(f"\n{'Nombre':<20} {'Precio':>10} {'Cantidad':>10}")
    print("-" * 42)
    for p in inventario:
        print(f"{p['nombre']:<20} ${p['precio']:>9.2f} {p['cantidad']:>10}")


def buscar_producto(inventario, nombre):
    """Busca y retorna un producto por nombre (insensible a mayúsculas)."""
    for p in inventario:
        if p["nombre"].lower() == nombre.strip().lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto existente."""
    if nuevo_precio is not None and nuevo_precio < 0:
        print("El precio no puede ser negativo.")
        return False
    if nueva_cantidad is not None and nueva_cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return False
    p = buscar_producto(inventario, nombre)
    if p:
        if nuevo_precio is not None:
            p["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            p["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario por nombre."""
    for i, p in enumerate(inventario):
        if p["nombre"].lower() == nombre.strip().lower():
            inventario.pop(i)
            return True
    return False


def calcular_estadisticas(inventario):
    """Calcula y retorna estadísticas generales del inventario."""
    if not inventario:
        return None
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }