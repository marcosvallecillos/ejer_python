import pandas as pd 

#1
empleados = pd.DataFrame({
    'nombre': ['Carlos', 'María', 'Juan', 'Ana', 'Pedro', 'Laura', 'Diego', 'Sofía', 'Miguel', 'Valentina'],
    'apellido': ['García', 'Rodríguez', 'Martínez', 'López', 'González', 'Fernández', 'Sánchez', 'Ramírez', 'Torres', 'Flores'],
    'salario': [45000, 52000, 38000, 55000, 42000, 48000, 35000, 60000, 50000, 40000],
    'departamento': ['Ventas', 'IT', 'Marketing', 'IT', 'Ventas', 'RRHH', 'Marketing', 'IT', 'RRHH', 'Ventas'],
    'jefe': ['Ana', 'Ana', 'Sofía', None, 'Ana', 'Miguel', 'Sofía', None, None, 'Ana'],
    'cargo': ['Vendedor', 'Desarrollador', 'Asistente', 'Directora IT', 'Vendedor', 'Analista', 'Diseñador', 'Directora IT', 'Director RRHH', 'Vendedor Junior']
})
empleados.to_csv('empleados.csv',index=False)
# Mostrar el DataFrame
print(empleados)
print("\n")
print(f"Total de empleados: {len(empleados)}")
print(f"\nEstadísticas de salarios:")
print(empleados['salario'].describe())