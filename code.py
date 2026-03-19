from funciones import *

# MENU PRINCIPAL 
while True:
    print("\n========== MENÚ ==========")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    # Condicionales
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")