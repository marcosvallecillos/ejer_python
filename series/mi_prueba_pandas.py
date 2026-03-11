import pandas as pd 
#1
diccionario = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

data = pd.Series(diccionario)
print(data) 
#2

elemento1 = data.iloc[2]  
elemento2 = data["d"]  
elemento3 = data[["b", "e"]]  

print("Posicion 2:", elemento1)
print("Etiqueta d:", elemento2)
print("Etiquetas b y e:", elemento3)

#3

elementos = data.iloc[0:3]
elementos = data.loc["b":"d"]
print("Elementos de la posición 0 a 2:", elementos)
print("Elementos de las etiquetas b a d:", elementos)

#4
data.index = ["A", "B", "C", "D", "E"]
print("Nuevo índice:",data)

#5
minimo = data.min()
minimo_index = data.idxmin()
maximo_index = data.idxmax()

maximo = data.max()
print("Valor mínimo:", minimo)
print("Valor máximo:", maximo)
print("Índice del valor mínimo:", minimo_index)
print("Índice del valor máximo:", maximo_index)

#6
print("Suma de todos los valores:", data.sum())
print("Media de todos los valores:", data.mean())
print("Elementos unicos en la serie:", data.unique() )

#7
filtered_data = data[(data > 25) & (data < 45)]
print("Elementos mayores a 25 y menores a 45:", filtered_data)

#8
media_data = data.median()
print("Elementos mayores a la mediana:", data[data > media_data])

#9
if data["C":"F"] is not None:
    print("La etiqueta 'C' y 'F' existe en la serie. ")

#10
serie = pd.Series([1.5, 2.5, 3.5, 4.5, 5.5], index=['a', 'b', 'c', 'd', 'e'])
print("Nueva serie:")
print(serie)

#11
serie_values_doubled = serie.values * 2
newserie_doubled = pd.Series(serie_values_doubled, index=serie.index)
print("Valores de la serie multiplicados por 2:")
print(serie_values_doubled)
print("Nueva serie con valores duplicados:")
print(newserie_doubled)

#12

data = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'], index = ['A', 'B', 'C', 'D', 'E'])
print("Serie con valores de texto")
print(data)

#13
mayus = data.str.upper()
print("Convirtiendo elementos a mayuscula:",mayus)
remplaza = data.str.replace('a','o')
print("Remplazando las vocales a por o",remplaza)
#14
serie = pd.Series(['100','200','300','400'], index = ['x','y','z','w'])
print("Nueva serie:",serie)

#15
nueva_serie = serie.reindex(['a','b','c','d','e'])
print("Reindexar la serie anterior:")
print(nueva_serie)

#16
nuevos_valores = nueva_serie.fillna(0)
print(nuevos_valores)

#17
if True:
    eliminar_nan = nueva_serie.dropna()
    print("Valores nan eliminados")
else:
    print("No se han eliminado")

#18

diccionario = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

data = pd.Series(diccionario)
print("Serie ejer1:")
print(data)

print("Tres primeras filas",data.head(3))
print("Dos ultimas filas", data.tail(2))

#19
print("Estadisticas",data.describe(percentiles=None,include=None,exclude=None))

#21
new_serie = pd.Series([2,4,6,8,10],index = ['a','b','c','d','e'])
#22
serie_cuadrado = new_serie.apply(lambda x: x**2)
print(serie_cuadrado)

#23
diccionario = {2: "two", 4: "four", 6: "six", 9: "eight", 10: "ten"}

data = pd.Series(diccionario)
print(data)
print(data.map(
{"two":"dos","four":"cuatro","six":"seis","eight":"ocho","ten":"diez"}
)   )

#ENVIAR
import numpy as np

#1
meses = ['Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'Enero', 
         'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']

notas = np.random.randint(70, 101, size=10)

serie_notas = pd.Series(notas, index=meses, name='Notas')
print(f"Nota media del año: {serie_notas.mean()}")

primera_mitad = serie_notas.head(5)
segunda_mitad = serie_notas.tail(5)
mejora = segunda_mitad.mean()-primera_mitad.mean()
empeoro = primera_mitad.mean()-segunda_mitad.mean()
print(serie_notas)
print("\n--- Estadísticas ---")
print(f"Nota media del año: {serie_notas.mean()}")
print(f"Nota media de los primeros cinco meses: {primera_mitad.mean()}")
print(f"Nota media de los ultimos cinco meses: {segunda_mitad.mean()}")
if primera_mitad.mean() < segunda_mitad.mean():
    print(f"Si mejoro las notas {mejora:.2f} puntos")
else:
    print(f"No mejoro las notas ")


#2
print("===============EJERCICIO 2============")
meses = ['Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'Enero', 
         'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']

notas = np.random.randint(40, 60, size=10)

puntuacion = pd.Series(notas, index=meses, name='Notas')
media = puntuacion.mean()
diferencia = 85 - media
notas_ajustadas = puntuacion + diferencia

print(notas_ajustadas)
print(puntuacion)
print(f"Nota media del año: {media}")
print(f"Diferencia {diferencia}")
print(notas_ajustadas)
print(f"\nNueva media: {notas_ajustadas.mean():.2f}")

#3 
print("===============EJERCICIO 3============")
numeros = np.random.randint(0, 100, size=10)
puntuacion = pd.Series(numeros, index=[(n % 100) // 10 for n in numeros], name='Notas')

print(puntuacion)