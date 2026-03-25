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

    opcion = input("Opción: ")

    try:
        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Buscar: ")
            p = buscar_producto(inventario, nombre)
            print(p if p else "Producto no encontrado")

        elif opcion == "4":
            nombre = input("Producto: ")
            precio = input("Nuevo precio: ")
            cantidad = input("Nueva cantidad: ")

            precio = float(precio) if precio else None
            cantidad = int(cantidad) if cantidad else None

            if actualizar_producto(inventario, nombre, precio, cantidad):
                print("Producto actualizado")
            else:
                print("No encontrado")

        elif opcion == "5":
            nombre = input("Eliminar: ")
            print("Eliminado" if eliminar_producto(inventario, nombre) else "No encontrado")

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            if stats:
                print("Unidades totales:", stats["unidades_totales"])
                print("Valor total:", stats["valor_total"])
                print("Más caro:", stats["producto_mas_caro"]["nombre"])
                print("Mayor stock:", stats["producto_mayor_stock"]["nombre"])
            else:
                print("Inventario vacío")

        elif opcion == "7":
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta archivo: ")
            nuevos = cargar_csv(ruta)

            if nuevos:
                op = input("¿Sobrescribir? (S/N): ").upper()

                if op == "S":
                    inventario.clear()
                    inventario.extend(nuevos)
                    print("Inventario reemplazado")
                else:
                    for p in nuevos:
                        existente = buscar_producto(inventario, p["nombre"])
                        if existente:
                            existente["cantidad"] += p["cantidad"]
                            existente["precio"] = p["precio"]
                        else:
                            inventario.append(p)
                    print("Inventario fusionado")

        elif opcion == "9":
            print("Adiós")
            break

        else:
            print("Opción inválida")

    except Exception as e:
        print("Error:", e)
