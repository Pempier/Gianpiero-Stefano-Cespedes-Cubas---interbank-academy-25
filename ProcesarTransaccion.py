import csv   # Importa el módulo 'csv' para leer y escribir archivos CSV
import os    # Importa el módulo 'os' para interactuar con el sistema operativo

def procesar_transacciones(nombre_archivo):    # Define una función llamada 'procesar_transacciones' que recibe el nombre del archivo CSV
    try:  # Inicia un bloque para capturar errores
        balance = 0.0        # Inicializa el balance
        mayor_monto = 0.0    # Guardará el monto más alto encontrado
        id_mayor = None      # Almacenará el ID de la transacción con el mayor monto
        conteo = {"Crédito": 0, "Débito": 0}    # Diccionario para contar transacciones de crédito y débito

        # Abre el archivo CSV en modo lectura:
        # - 'newline=""' evita problemas con saltos de línea
        # - 'encoding="utf-8-sig"' soporta archivos con BOM (común en Windows)
        with open(nombre_archivo, newline='', encoding='utf-8-sig') as archivo:
            lector = csv.DictReader(archivo)     # Crea un lector de CSV que interpreta cada fila como diccionario
            for fila in lector:                  # Itera sobre cada fila del archivo CSV
                tipo = fila["tipo"]              # Obtiene el tipo de transacción (Crédito/Débito) de la columna "tipo"
                monto = float(fila["monto"])     # Convierte el monto (texto) a número decimal (float)
                id_transaccion = fila["id"]      # Obtiene el ID de la transacción de la columna "id"

                # Si es un crédito, suma al balance y aumenta su contador
                if tipo == "Crédito":
                    balance += monto
                    conteo["Crédito"] += 1
                # Si es un débito, resta del balance y aumenta su contador
                elif tipo == "Débito":
                    balance -= monto
                    conteo["Débito"] += 1

                # Verifica si el monto actual es el mayor encontrado
                if monto > mayor_monto:
                    mayor_monto = monto  # Actualiza el mayor monto
                    id_mayor = id_transaccion  # Guarda su ID
        
        # --- Imprime el reporte ---
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance:.2f}")    # Muestra el balance con 2 decimales
        print(f"Transacción de Mayor Monto: ID {id_mayor} - {mayor_monto:.2f}")    # Muestra el ID y monto de la transacción más grande
        print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")    # Muestra cuántas transacciones hubo de cada tipo

    # Si el archivo no existe, muestra este error
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}' en la ruta: {os.getcwd()}")    # 'os.getcwd()' obtiene la carpeta actual donde se busca el archivo
        
    # Si ocurre otro error inesperado, lo muestra
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

# Llama a la función y procesa "data.csv"
procesar_transacciones("data.csv")
input("Presiona Enter para salir...")    # Pausa antes de cerrar (útil al ejecutar en Windows)

