# Procesador de Transacciones Bancarias (CLI)

## Introducción
Esta es una aplicación de línea de comandos que procesa un archivo CSV con transacciones bancarias. Genera un reporte que incluye el balance final, la transacción de mayor monto y el conteo de transacciones por tipo ("Crédito" y "Débito").

## Instrucciones de Ejecución
1. Asegúrate de tener el archivo `data.csv` en el mismo directorio.
2. Ejecuta el script con:
    py ProcesarTransaccion.py
3. El código también funciona al ejecutarlo directamente desde windows, asegurate de cumplir el paso 1.

## Enfoque y Solución
Se utiliza Python con el módulo `csv` para leer y procesar los datos; además del módulo `os` para el funcionamiento en sistemas operativos como windows. El programa calcula el balance total, identifica la transacción con mayor monto y cuenta cuántas transacciones hay de cada tipo. La lógica es sencilla y no requiere librerías externas, se formula el siguiente Pseudocódigo estructurado:
    
    1. Importa los módulos necesarios: csv, que sirve para leer archivos en formato CSV; y os, que permite trabajar con rutas del sistema operativo.
    2. Define una función llamada procesar_transacciones que reciba el nombre del archivo CSV como parámetro.
    3. Dentro de la función, maneja los errores usando un bloque try-except. En el bloque try, realiza las siguientes acciones:
        3.1. Inicializa las siguientes variables: balance como 0.0, para acumular la diferencia entre créditos y débitos; mayor_monto como 0.0, para registrar el monto más alto encontrado; id_mayor como None (o “ninguno”), para guardar el ID de la transacción de mayor valor; y un diccionario llamado conteo, con los tipos "Crédito" y "Débito", ambos inicializados en cero, para contar las transacciones por tipo.
        3.2. Abre el archivo CSV usando with open(...) para asegurar que se cierre automáticamente al finalizar. Especifica la codificación como utf-8-sig para garantizar compatibilidad con sistemas Windows.
        3.3. Usa csv.DictReader para leer las filas del archivo como diccionarios. Para cada fila del archivo: extrae el tipo de transacción (por ejemplo, "Crédito" o "Débito"), el monto (conversión a número), y el ID de   la transacción. Si el tipo es "Crédito", suma el monto al balance y aumenta en uno el contador de créditos. Si el tipo es "Débito", resta el monto del balance y aumenta en uno el contador de débitos. Si el monto actual es mayor que mayor_monto, actualiza mayor_monto con este valor y guarda su ID en id_mayor.
        3.4. Al finalizar la lectura del archivo, imprime un reporte con la siguiente información: el balance final (resultado de créditos menos débitos), la transacción de mayor monto (mostrando su ID y su valor), y el número de transacciones de tipo "Crédito" y "Débito".
    4. En caso de que el archivo no exista, muestra un mensaje de error indicando que no se encontró el archivo, y muestra también la ruta actual del sistema usando os.getcwd().
    5. Si ocurre cualquier otro error, muestra un mensaje genérico de error.
    6. Fuera de la función, llama a procesar_transacciones("data.csv") para ejecutar todo el proceso sobre un archivo llamado data.csv.
    7. Finalmente, espera que el usuario presione Enter antes de cerrar el programa.

## Estructura del Proyecto
📦 Gianpiero-Stefano-Cespedes-Cubas---interbank-academy-25/
 ┣ 📄 ProcesarTransaccion.py
 ┣ 📄 README.md
 ┗ 📄 data.csv
