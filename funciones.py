

# FUNCION 
def agregar_producto():
    # Lista donde se guardarán los productos
    inventario = []
    print("\n--- Agregar producto ---")

    # Validar nombre
    while True:
        nombre = input("Nombre del producto: ").strip().capitalize()
        if nombre == "":
            print("El nombre no puede estar vacío.")
        elif nombre.isnumeric():
            print("El nombre no puede ser solo números.")
        else:
            break

    # Validar precio
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingresa un número válido.")

    # Validar cantidad
    while True:
        try:
            cantidad = int(input("Cantidad del producto: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("Ingresa un número entero válido.")

    # Crear diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Guardar en la lista inventario
    inventario.append(producto)

    print("Producto agregado correctamente ")


# FUNCION
def mostrar_inventario(inventario):
    print("\n--- Inventario ---")

    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        # Recorrer con for
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


#  FUNCION 
def mostrar_estadistica(inventario):
    print("\n--- Estadísticas ---")

    if len(inventario) == 0:
        print("No hay productos para calcular.")
        return

    total_valor = 0
    total_cantidad = 0

    # Recorrer inventario
    for producto in inventario:
        total_valor += producto["precio"] * producto["cantidad"]
        total_cantidad += producto["cantidad"]

    print(f"Valor total del inventario: {total_valor}")
    print(f"Cantidad total de productos: {total_cantidad}")