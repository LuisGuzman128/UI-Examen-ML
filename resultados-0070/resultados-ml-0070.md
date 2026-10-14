# EXAMEN DE MACHINE LEARNING - PANDAS
**Alumno:** Luis Axel Guzman Martinez
**NC:** 0070
**Numero de lista:** 27

---

## 0. VERIFICACIÓN DE ENTORNO Y SISTEMA
```text
Versión de Python: 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)]
Versión de Pandas: 3.0.6
```

## 1. DATAFRAME DE MASCOTAS (DATOS DE ENTRADA)
```text
    Mascota Especie  Edad
0  Firulais   Perro     3
1     Michi    Gato     2
2      Luna   Perro     5
3     Rocky   Perro     1
4      Coco    Loro     8
5    Pelusa    Gato     4
```

## 2. INFORMACIÓN DEL DATAFRAME

### 2.1 PRIMERAS FILAS (head(2))
```text
    Mascota Especie  Edad
0  Firulais   Perro     3
1     Michi    Gato     2
```

### 2.2 ÚLTIMAS FILAS (tail(2))
```text
  Mascota Especie  Edad
4    Coco    Loro     8
5  Pelusa    Gato     4
```

### 2.3 DIMENSIONES (Filas, Columnas)
```text
Dimensiones (shape): (6, 3)
```

### 2.4 TIPOS DE DATOS (dtypes)
```text
Mascota    object
Especie    object
Edad        int64
```

### 2.5 INFORMACIÓN GENERAL (info())
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Mascota  6 non-null      object
 1   Especie  6 non-null      object
 2   Edad     6 non-null      int64 
dtypes: int64(1), object(2)
memory usage: 276.0+ bytes
```

## 3. ESTADÍSTICAS DE LA COLUMNA EDAD (describe())
```text
count    6.000000
mean     3.833333
std      2.483277
min      1.000000
25%      2.250000
50%      3.500000
75%      4.750000
max      8.000000
```

## 4. ORDEN ASCENDENTE POR EDAD
```text
 Mascota Especie  Edad
   Rocky   Perro     1
   Michi    Gato     2
Firulais   Perro     3
  Pelusa    Gato     4
    Luna   Perro     5
    Coco    Loro     8
```

## 5. ORDEN DESCENDENTE POR EDAD
```text
 Mascota Especie  Edad
    Coco    Loro     8
    Luna   Perro     5
  Pelusa    Gato     4
Firulais   Perro     3
   Michi    Gato     2
   Rocky   Perro     1
```

---

Programa realizado por Axel Guzman 0070
