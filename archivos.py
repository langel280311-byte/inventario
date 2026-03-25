import csv

def guardar_csv(inventario, ruta):
    """Guarda el inventario en un archivo CSV."""
    if not inventario:
        print("Inventario vacío, no se puede guardar.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print("Error al guardar:", e)


def cargar_csv(ruta):
    """Carga un CSV y retorna lista de productos."""
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido.")
                return []

            for fila in reader:
                try:
                    if len(fila) != 3:
                        raise ValueError

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"{errores} filas inválidas omitidas.")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Error:", e)

    return []