import pandas as pd 
#Concatena estos DataFrames verticalmente.
df1 = pd.DataFrame({
    'ID': ['A1', 'A2', 'A3'],
    'Sales': [100, 200, 300]
})

df2 = pd.DataFrame({
    'ID': ['A4', 'A5', 'A6'],
    'Revenue': [400, 500, 600]
})
concatenar = pd.concat([df1, df2], axis=0)
print("\nConcatenación Verticalmente:")
print(concatenar)

#concaténalos verticalmente, reseteando el índice
df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

df2 = pd.DataFrame({
    'A': [5, 6],
    'B': [7, 8]
})

concatenar = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nConcatenación Verticalmente reseteando index:")
print(concatenar)

# Utilizando join='inner' y join='outer'

df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df2 = pd.DataFrame({
    'A': [10, 11, 12],
    'D': [13, 14, 15]
})
# Inner solo junta los valores con  index iguales en ambos dataframes sino
#los elimina
df_interseccion = pd.concat([df1, df2], axis=0, join='inner')
print("\nConcatenación con join='inner':")
print(df_interseccion)
# outer Junta o a;ade valores al index 
df_outer = pd.concat([df1, df2], axis=0, join='outer')
print("\nConcatenación con join='outer':")
print(df_outer)
#Concatena los siguientes DataFrames horizontalmente y luego calcula la suma de todas las columnas.

df1 = pd.DataFrame({
    'X': [1, 2, 3],
    'Y': [4, 5, 6]
})

df2 = pd.DataFrame({
    'Z': [7, 8, 9],
    'W': [10, 11, 12]
})

df_concat = pd.concat([df1,df2], axis=1).sum()
print("Concatenando horizontalmente y calculando la suma:")
print(df_concat)

#Usa los siguientes DataFrames y realiza un merge utilizando `left_on` y `right_on`. Luego realiza un `outer_join` y muestra el resultado.

df1 = pd.DataFrame({
    'Product_ID': ['P1', 'P2', 'P3'],
    'Sales': [100, 200, 300]
})

df2 = pd.DataFrame({
    'ID': ['P1', 'P3', 'P4'],
    'Discount': [10, 15, 20]
})
df_merge = pd.merge(df1, df2, left_on='Product_ID', right_on='ID')

# Outer join
df_outer = pd.merge(df1, df2, left_on='Product_ID', right_on='ID', how='outer')

print("Merge con left_on y right_on:")
print(df_merge)
print("\nOuter join:")
print(df_outer)


# Haciendo merge utilizado indicator=True
#Se crea una nueva columna indicando en q df se ha encontrado las coincidencias
print("Usando indicator=True")
df_ind = pd.merge(df1, df2, how="outer", left_on="Product_ID",right_on='ID', indicator=True)
print(df_ind)

#Utilizando merge con multiples claves
df1 = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Region': ['North', 'South', 'East'],
    'Sales': [250, 150, 300]
})

df2 = pd.DataFrame({
    'Product': ['A', 'B', 'D'],
    'Region': ['North', 'East', 'West'],
    'Profit': [50, 60, 70]
})
df_merge = pd.merge(df1,df2, how='inner',on=['Product','Region'])
print(df_merge)

# Concatenando verticalmente utilizando join

df1 = pd.DataFrame({
    'A': [1, 2, None],
    'B': [4, None, 6]
})

df2 = pd.DataFrame({
    'A': [None, 8, 9],
    'C': [10, 11, 12]
})

df_concat = pd.concat([df1,df2], axis=0, join='outer')

df_concat = df_concat.fillna(df_concat.mean())
print(df_concat)


df1 = pd.DataFrame({
    'Employee_ID': ['E1', 'E2', 'E3'],
    'Name': ['John', 'Jane', 'Doe'],
    'Salary': [70000, 80000, 90000]
})

df2 = pd.DataFrame({
    'ID': ['E1', 'E4', 'E3'],
    'Department': ['HR', 'Finance', 'IT'],
    'Bonus': [5000, 7000, 6000]
})
#HaY q poner el left y el right pqq no tienen los mismos index
df_outer = pd.merge(df1,df2,left_on='Employee_ID',how='outer',right_on='ID')

print(df_outer)
