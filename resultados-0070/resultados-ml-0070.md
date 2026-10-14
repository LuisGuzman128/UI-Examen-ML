# EXAMEN DE MACHINE LEARNING - PANDAS
Alumno: Luis Axel Guzman Martinez
NC: 0070
Numero de lista: 27

---

1. DATAFRAME DE MASCOTAS
```
    Mascota Especie  Edad
0  Firulais   Perro     3
1     Michi    Gato     2
2      Luna   Perro     5
3     Rocky   Perro     1
4      Coco    Loro     8
5    Pelusa    Gato     4
```

2. INFORMACIÓN DEL DATAFRAME

2.1 PRIMERAS FILAS
```
    Mascota Especie  Edad
0  Firulais   Perro     3
1     Michi    Gato     2
```

2.2 ÚLTIMAS FILAS
```
  Mascota Especie  Edad
4    Coco    Loro     8
5  Pelusa    Gato     4
```

2.3 DIMENSIONES (Filas, Columnas)
(6, 3)

2.4 TIPOS DE DATOS
Mascota      str
Especie      str
Edad       int64
dtype: object

2.5 INFORMACIÓN GENERAL
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   Mascota  6 non-null      str  
 1   Especie  6 non-null      str  
 2   Edad     6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

3. ESTADÍSTICAS DE EDAD
count    6.000000
mean     3.833333
std      2.483277
min      1.000000
25%      2.250000
50%      3.500000
75%      4.750000
max      8.000000
Name: Edad, dtype: float64

4. ORDEN ASCENDENTE POR EDAD
```
 Mascota Especie  Edad
   Rocky   Perro     1
   Michi    Gato     2
Firulais   Perro     3
  Pelusa    Gato     4
    Luna   Perro     5
    Coco    Loro     8
```

5. ORDEN DESCENDENTE POR EDAD
```
 Mascota Especie  Edad
    Coco    Loro     8
    Luna   Perro     5
  Pelusa    Gato     4
Firulais   Perro     3
   Michi    Gato     2
   Rocky   Perro     1
```
programa realizado por Axel Guzman 0070
