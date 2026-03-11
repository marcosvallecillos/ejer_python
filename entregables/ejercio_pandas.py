import numpy as np
import pandas as pd
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

#Empleados
#1
print("\n")
print("===========EJERCICIO EMPLEADOS=========")
empleados = pd.DataFrame({
    'nombre': ['Javi', 'María', 'Juan', 'Ana', 'Pedro', 'Laura', 'Diego', 'Sofía', 'Miguel', 'Valentina'],
    'apellido': ['García', 'Rodríguez', 'Martínez', 'López', 'González', 'Fernández', 'Sánchez', 'Ramírez', 'Torres', 'Flores'],
    'salario': [45000, 2000, 2900, 55000, 2000, 48000, 35000, 60000, 50000, 40000],
    'departamento': ['Ventas', 'IT', 'Marketing', 'IT', 'Ventas', 'RRHH', 'Marketing', 'IT', 'RRHH', 'Ventas'],
    'jefe': ['Ana', 'Ana', 'Sofía', None, 'Ana', 'Miguel', 'Sofía', None, None, 'Ana'],
    'cargo': ['Vendedor', 'Desarrollador', 'Asistente', 'Gerente', 'gerente', 'Analista', 'Diseñador', 'Directora IT', 'Director RRHH', 'Vendedor Junior']
})
empleados.to_csv('empleados.csv',index=False)
# Mostrar el DataFrame
#print(empleados)
print("\n")
#Nombre de los empleados que tengan un  salario inferior a 3000
resultado = empleados[empleados["salario"] < 3000]["nombre"]
print(f"Empleados con salario inferior a 3000: {resultado}")
print("\n")

#Nombre de los empleados que empieza por j
empieceJ = empleados[empleados['nombre'].str.startswith('J')]["nombre"]
print('Nombre de los empleados que empiezan por J:')
print(empieceJ)
print("\n")

# Apellido contenga h
cotengaH = empleados[empleados['apellido'].str.contains('h')][["nombre", "apellido"]]
print('Nombre  y apellido de los empleados que su apellido contenga h:')
print(cotengaH)
print("\n")
# Ordenaor empleados por departamento
ordenar = empleados.sort_values(by='departamento')
print("Ordenar empleados a base de su departamento:")
print(ordenar)
print("\n")

# Obtener empleado q es el gerente de la empresa

gerente = empleados[empleados['cargo'] == 'gerente']
print("Obtiendo el empleado q tiene el cargo de gerente:")
print(gerente)
print("\n")

# Obtener empleado q estan a cargo de un jefe

empleados_con_jefe = empleados[empleados['jefe'].notna()]

print("Empleados a carga de un jefe")
print(empleados_con_jefe)

#print(f"\nEstadísticas de salarios:") 
#print(empleados['salario'].describe())