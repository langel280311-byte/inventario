from funciones import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv

inventario = []

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Error: el precio debe ser un número decimal y la cantidad un entero.")
            continue
        if agregar_producto(inventario, nombre, precio, cantidad):
            print(f"'{nombre}' agregado correctamente.")

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Buscar: ").strip()
        p = buscar_producto(inventario, nombre)
        if p:
            print(f"Encontrado → {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}")
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        nombre = input("Nombre del producto a actualizar: ").strip()
        precio_str = input("Nuevo precio (Enter para omitir): ").strip()
        cantidad_str = input("Nueva cantidad (Enter para omitir): ").strip()
        try:
            precio = float(precio_str) if precio_str else None
            cantidad = int(cantidad_str) if cantidad_str else None
        except ValueError:
            print("Error: valor ingresado no válido.")
            continue
        if actualizar_producto(inventario, nombre, precio, cantidad):
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    elif opcion == "5":
        nombre = input("Nombre del producto a eliminar: ").strip()
        confirmacion = input(f"¿Seguro que deseas eliminar '{nombre}'? (S/N): ").strip().upper()
        if confirmacion == "S":
            if eliminar_producto(inventario, nombre):
                print(f"'{nombre}' eliminado.")
            else:
                print("Producto no encontrado.")
        else:
            print("Operación cancelada.")

    elif opcion == "6":
        stats = calcular_estadisticas(inventario)
        if stats:
            print(f"Unidades totales : {stats['unidades_totales']}")
            print(f"Valor total      : ${stats['valor_total']:.2f}")
            print(f"Más caro         : {stats['producto_mas_caro']['nombre']} (${stats['producto_mas_caro']['precio']:.2f})")
            print(f"Mayor stock      : {stats['producto_mayor_stock']['nombre']} ({stats['producto_mayor_stock']['cantidad']} unidades)")
        else:
            print("Inventario vacío.")

    elif opcion == "7":
        ruta = input("Ruta del archivo CSV: ").strip()
        if ruta:
            guardar_csv(inventario, ruta)
        else:
            print("Ruta no válida.")

    elif opcion == "8":
        ruta = input("Ruta del archivo CSV: ").strip()
        if not ruta:
            print("Ruta no válida.")
            continue
        nuevos = cargar_csv(ruta)
        if nuevos:
            op = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
            if op == "S":
                inventario.clear()
                inventario.extend(nuevos)
                print("Inventario reemplazado.")
            else:
                for p in nuevos:
                    existente = buscar_producto(inventario, p["nombre"])
                    if existente:
                        existente["cantidad"] += p["cantidad"]
                        existente["precio"] = p["precio"]
                    else:
                        inventario.append(p)
                print("Inventario fusionado.")
        else:
            print("No se cargaron productos.")

    elif opcion == "9":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Elige un número del 1 al 9.")