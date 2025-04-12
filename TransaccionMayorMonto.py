import csv  # Importa el módulo csv para trabajar con archivos CSV

# Define la función principal que recibe el nombre del archivo a procesar
def procesar_transacciones(nombre_archivo):
    balance = 0.0                 # Inicializa el balance en cero
    mayor_monto = 0.0             # Almacena el mayor monto encontrado
    id_mayor = None               # Guarda el ID de la transacción con mayor monto
    conteo = {"Crédito": 0, "Débito": 0}  # Contador para cada tipo de transacción

    # Abre el archivo CSV en modo lectura
    with open(nombre_archivo, newline='') as archivo:
        lector = csv.DictReader(archivo)  # Lee el CSV como diccionarios por fila
        for fila in lector:               # Itera sobre cada fila del archivo
            tipo = fila["tipo"]           # Obtiene el tipo de transacción ("Crédito" o "Débito")
            monto = float(fila["monto"])  # Convierte el monto de texto a número decimal
            id_transaccion = fila["id"]   # Obtiene el ID de la transacción

            # Si es un crédito, suma el monto al balance y cuenta uno más
            if tipo == "Crédito":
                balance += monto
                conteo["Crédito"] += 1

            # Si es un débito, resta el monto del balance y cuenta uno más
            elif tipo == "Débito":
                balance -= monto
                conteo["Débito"] += 1

            # Si el monto es mayor al máximo anterior, actualiza el registro
            if monto > mayor_monto:
                mayor_monto = monto
                id_mayor = id_transaccion

    # Imprime el reporte final en consola
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance:.2f}")  # Muestra el balance con 2 decimales
    print(f"Transacción de Mayor Monto: ID {id_mayor} - {mayor_monto:.2f}")  # ID y monto mayor
    print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")  # Cantidad por tipo

# Llama a la función con el nombre del archivo a analizar
procesar_transacciones("data.csv")
