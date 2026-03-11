import pandas as pd
import zipfile
#1
with zipfile.ZipFile(r'C:\Users\vboxuser\Downloads\03 - Dataframes Avanzado.zip') as z:
    z.extract('tienda.csv.zip')

# Ahora leer desde tienda.csv.zip
df = pd.read_csv('tienda.csv.zip', compression='zip')
print(df)
#2
print('============ EJERCICIO 2 ==============')

dataframe = df.groupby('Categoria').agg({
    'Unidades_Vendidas': 'sum',
    'Precio_Unitario': 'mean'
})
print(dataframe)

#3
print('============ EJERCICIO 3 ==============')

dataframe = df.pivot_table(
    values='Inventario_Disponible',
    columns='Producto',
    aggfunc='max'
)
print(dataframe)

#4
print('============ EJERCICIO 4 ==============')
dataframe = df.pivot_table(
    values='Precio_Unitario',
    index='Categoria',
    columns='Producto',
    aggfunc='min'
)
print(dataframe)

#5

print('============ EJERCICIO 5 ==============')

dataframe = df.set_index(['Oferta', 'Resolución']).stack()
print(dataframe)