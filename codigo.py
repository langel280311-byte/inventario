opcion= 1
while opcion== 1: # El ciclo se repetirá mientras el usuario ingrese 1 para registrar otra venta
    print("------------------------------------------")
    print("-------- Registro de ventas --------------")
    print("------------------------------------------")

    # Primer validacion del nombre del producto
    while True:
        nombre = input("Nombre del producto: ").strip().capitalize()
        if nombre == "":
            print("El nombre no puede estar vacío.")
        elif nombre.isnumeric():
            print("El nombre no puede ser solo números.")
        else:
            break
    # Segundo bucle para validar precio (solo números, no negativos)
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Error: Debes ingresar un número válido para el precio.")

    # Tercer bucle para validar cantidad (solo enteros)
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad comprada: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
    

    # Validacion final antes de calcular el costo total
    if precio >= 0 and cantidad >= 0:
        costo_total= precio * cantidad
        print("el costo total es: ", costo_total)
    else:
        print("error precio o cantidad invalida")

    # Impresión de resultados
    print("----Resultado Inventario----")
    print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} |Costo total: {costo_total}")
    

    # Preguntar si desea registrar otra venta
    opcion = input("¿Deseas registrar otra venta? (1 para sí, cualquier otra tecla para no): ")
    opcion = int(opcion) if opcion.isdigit() else 0 # Convertir a entero si es un número, de lo contrario asignar 0 para salir del ciclo