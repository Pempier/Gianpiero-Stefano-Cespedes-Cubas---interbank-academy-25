import csv

def procesar_transacciones(nombre_archivo):
    balance = 0.0
    mayor_monto = 0.0
    id_mayor = None
    conteo = {"Crédito": 0, "Débito": 0}

    with open(nombre_archivo, newline='') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            tipo = fila["tipo"]
            monto = float(fila["monto"])
            id_transaccion = fila["id"]

            if tipo == "Crédito":
                balance += monto
                conteo["Crédito"] += 1
            elif tipo == "Débito":
                balance -= monto
                conteo["Débito"] += 1

            if monto > mayor_monto:
                mayor_monto = monto
                id_mayor = id_transaccion

    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {id_mayor} - {mayor_monto:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")

procesar_transacciones("data.csv")
