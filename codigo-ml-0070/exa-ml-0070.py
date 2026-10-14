# Luis Axel Guzman Martinez NC=0070
# Examen de Machine Learning - Pandas
# Numero de lista 27: Datos de mascotas

import pandas as pd
import importlib.util
from pathlib import Path
import io
from contextlib import redirect_stdout

# 1. Definir las rutas
carpeta_proyecto = Path(__file__).resolve().parent.parent

ruta_diccionario = (
    carpeta_proyecto
    / "datos-de-entrada-ml-0070"
    / "dicc-0070.py"
)

carpeta_resultados = carpeta_proyecto / "resultados-0070"
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Cargar el diccionario
especificacion = importlib.util.spec_from_file_location(
    "diccionario_mascotas", ruta_diccionario
)

diccionario = importlib.util.module_from_spec(especificacion)
especificacion.loader.exec_module(diccionario)

# 3. Convertir a DataFrame
df = pd.DataFrame(diccionario.datos_mascotas)

print("\nDATAFRAME DE MASCOTAS")
print(df)

# 4. Primeras dos filas
print("\n2.1 PRIMERAS FILAS")
print(df.head(2))

# 5. Ultimas dos filas
print("\n2.2 ULTIMAS FILAS")
print(df.tail(2))

# 6. Dimensiones
print("\n2.3 DIMENSIONES")
print(df.shape)

# 7. Tipos de datos
print("\n2.4 TIPOS DE DATOS")
print(df.dtypes)

# 8. Informacion general
print("\n2.5 INFORMACION GENERAL")
df.info()

# 9. Estadisticas de edad
print("\n3. ESTADISTICAS DE EDAD")
print(df["Edad"].describe())

# 10. Orden ascendente por edad
print("\n4. ORDEN ASCENDENTE POR EDAD")
df_ascendente = df.sort_values(by="Edad", ascending=True)
print(df_ascendente.to_string(index=False))

# 11. Orden descendente por edad
print("\n5. ORDEN DESCENDENTE POR EDAD")
df_descendente = df.sort_values(by="Edad", ascending=False)
print(df_descendente.to_string(index=False))

# 12. Crear el reporte
contenido = io.StringIO()

with redirect_stdout(contenido):
    print("EXAMEN DE MACHINE LEARNING - PANDAS")
    print("Alumno: Luis Axel Guzman Martinez")
    print("NC: 0070")
    print("Numero de lista: 27")
    print("\nDATAFRAME DE MASCOTAS")
    print(df)
    print("\n2.1 PRIMERAS FILAS")
    print(df.head(2))
    print("\n2.2 ULTIMAS FILAS")
    print(df.tail(2))
    print("\n2.3 DIMENSIONES")
    print(df.shape)
    print("\n2.4 TIPOS DE DATOS")
    print(df.dtypes)
    print("\n2.5 INFORMACION GENERAL")
    df.info()
    print("\n3. ESTADISTICAS DE EDAD")
    print(df["Edad"].describe())
    print("\n4. ORDEN ASCENDENTE POR EDAD")
    print(df_ascendente.to_string(index=False))
    print("\n5. ORDEN DESCENDENTE POR EDAD")
    print(df_descendente.to_string(index=False))

ruta_reporte = carpeta_resultados / "resultados-ml-0070.md"

with open(ruta_reporte, "w", encoding="utf-8") as archivo:
    archivo.write(contenido.getvalue())

print("\nReporte guardado en:")
print(ruta_reporte)
print("Programa realizado por Axel Guzman 0070")