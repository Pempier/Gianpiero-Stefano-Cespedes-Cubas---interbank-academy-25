# Procesador de Transacciones Bancarias (CLI)

## Introducción
Esta es una aplicación de línea de comandos que procesa un archivo CSV con transacciones bancarias. Genera un reporte que incluye el balance final, la transacción de mayor monto y el conteo de transacciones por tipo ("Crédito" y "Débito").

## Instrucciones de Ejecución
1. Asegúrate de tener el archivo `data.csv` en el mismo directorio.
2. Ejecuta el script con:
    python transacciones.py

## Enfoque y Solución
Se utiliza Python con el módulo `csv` para leer y procesar los datos. El programa calcula el balance total, identifica la transacción con mayor monto y cuenta cuántas transacciones hay de cada tipo. La lógica es sencilla y no requiere librerías externas.

## Estructura del Proyecto
📦 Gianpiero-Stefano-Cespedes-Cubas---interbank-academy-25/
 ┣ 📄 README.md
 ┣ 📄 TransaccionMayorMonto.py
 ┗ 📄 data.csv
