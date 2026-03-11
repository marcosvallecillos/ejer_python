import pandas as pd

data = {
    "Producto": ["Laptop", "Laptop", "Mouse", "Mouse", "Monitor", "Monitor", "Teclado", "Teclado"],
    "Marca": ["Dell", "HP", "Logitech", "Razer", "Samsung", "LG", "Logitech", "Razer"],
    "Categoria": ["Computadoras", "Computadoras", "Accesorios", "Accesorios", "Monitores", "Monitores", "Accesorios", "Accesorios"],
    "Precio": [900, 850, 25, 40, 300, 280, 45, 60],
    "Unidades_Vendidas": [10, 15, 50, 30, 20, 18, 35, 25]
}
df = pd.DataFrame(data)

#1 
print('============ EJERCICIO 1 ==============')

ventas_producto = df.groupby('Producto').agg({
    'Unidades_Vendidas': 'sum'
})

print("Total de unidades vendidas por Producto:", ventas_producto)

#2
print('============ EJERCICIO 2 ==============')

ventas_categoria = df.groupby('Categoria').agg({
    'Unidades_Vendidas': 'sum'
})

print("Total de unidades vendidas por Categoria", ventas_categoria)

#3
print('============ EJERCICIO 3 ==============')

dataframe = df.pivot_table(
    index='Categoria',
    values='Unidades_Vendidas',
    columns='Producto',
    aggfunc='sum'
)
print(dataframe)

#4
print('============ EJERCICIO 4 ==============')

dataframe = df.pivot_table(
    index='Producto',
    columns='Marca',
    values='Precio'
)
print(dataframe)
#5
print('============ EJERCICIO 5 ==============')
pivot_df = df.pivot(index='Producto', columns='Marca', values='Precio')

#6
print('============ EJERCICIO 6 ==============')

stacked_df = pivot_df.stack()
print("Uso de stack:",stacked_df)

#7
print('============ EJERCICIO 7 ==============')

unstacked_df = stacked_df.unstack()
print("Uso de unstack:",unstacked_df)
#8
print("========= EJERCICIO 8 ========")
dataframe = df.pivot_table(
    index='Marca',
    columns='Categoria',
    values='Unidades_Vendidas',
    aggfunc='sum'
)
print(dataframe)

#9
print("========= EJERCICIO 9 ========")

precioByCategoria = df.groupby('Categoria').agg({
    'Precio' : 'mean'
})

print('Precio medio por categoria',precioByCategoria)

#10
print("========= EJERCICIO 10 ========")

dataframe = df.pivot_table(
    index=['Categoria','Producto'],
    columns='Marca',
    values='Unidades_Vendidas',
    aggfunc='sum'
)
print(dataframe)