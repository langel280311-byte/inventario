from funciones import *

inventario = []

while True:
    print("\n========== MENÚ ==========")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto(inventario)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        mostrar_estadistica(inventario)

    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida.")
