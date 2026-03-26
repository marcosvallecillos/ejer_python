import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np
import pandas as pd

# EJERCICIO 1
x = np.linspace(0, 10, 100)
y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(0.3*x)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y1, color='blue', linestyle='-', linewidth=2, label='Lineal')
axs[0, 0].set_title('Relación lineal')
axs[0, 0].legend()
axs[0, 0].grid(True)

axs[0, 1].plot(x, y2, color='red', linestyle='--', linewidth=2, label='Cuadrática')
axs[0, 1].set_title('Relación cuadrática')
axs[0, 1].legend()
axs[0, 1].grid(True)

axs[1, 0].plot(x, y3, color='green', linestyle='-.', linewidth=2, label='Sinusoidal')
axs[1, 0].set_title('Relación sinusoidal')
axs[1, 0].legend()
axs[1, 0].grid(True)

axs[1, 1].plot(x, y4, color='purple', linestyle=':', linewidth=2, label='Exponencial')
axs[1, 1].set_title('Relación exponencial')
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()

# EJERCICIO 2: 
tamaño = [1,2,3,4,5,6,7,8,9,10]
peso = [1.2,2.4,3.0,4.1,5.1,6.8,7.3,8.5,9.2,10.0]

plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.scatter(tamaño, peso, color='darkcyan', s=80, alpha=0.7)
plt.title('Relación Tamaño-Peso (Scatter)')

plt.subplot(3,1,2)
plt.plot(tamaño, peso, color='green', linestyle='--', marker='o')
plt.title('Gráfico de Líneas')

plt.subplot(3,1,3)
plt.hist(tamaño, bins=5, color='skyblue', edgecolor='black')
plt.title('Histograma de Tamaño')

plt.tight_layout()
plt.show()

# EJERCICIO 3:

fig = plt.figure(figsize=(10,10))
gs = gridspec.GridSpec(3,3)

ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :2])
ax3 = fig.add_subplot(gs[1, 2])

ax1.plot(range(10), 'r-', label='Datos 1')
ax2.plot(range(10), 'g-', label='Datos 2')
ax3.plot(range(10), 'b-', label='Datos 3')

ax1.set_title('Gráfico grande')
ax2.set_title('Gráfico pequeño 1')
ax3.set_title('Gráfico pequeño 2')

ax1.legend(); ax2.legend(); ax3.legend()
plt.tight_layout()
plt.show()

# EJERCICIO 4
plt.figure(figsize=(8,5))
plt.plot(tamaño, peso, color='green', linestyle='--', linewidth=2, label='Serie de datos')
plt.title('Gráfico de Líneas con Anotaciones')
plt.xlabel('Tamaño')
plt.ylabel('Peso')
plt.legend()

plt.annotate('Mínimo', xy=(1,1.2), xytext=(2,0.5),
             arrowprops=dict(facecolor='red', arrowstyle='->'), color='red')
plt.annotate('Gran aumento', xy=(5,5.1), xytext=(6,3.5),
             arrowprops=dict(facecolor='orange', arrowstyle='fancy'), color='orange')
plt.annotate('Máximo', xy=(10,10.0), xytext=(8,11),
             arrowprops=dict(facecolor='blue', arrowstyle='-|>'), color='blue')
plt.show()

# EJERCICIO 5: 
plt.style.use('classic')
plt.plot(tamaño, peso, marker='o')
plt.title('Estilo Classic')
plt.show()

plt.style.use('seaborn')
plt.plot(tamaño, peso, marker='o')
plt.title('Estilo Seaborn')
plt.show()

# EJERCICIO 6:
plt.rcParams.update({
    'figure.facecolor':'#f0f0f0',
    'axes.facecolor':'#ffffff',
    'axes.grid':True,
    'grid.color':'#bbbbbb',
    'grid.linestyle':'--',
    'grid.linewidth':0.8,
    'axes.labelcolor':'#111111',
    'axes.titlesize':14
})

x_scatter = np.random.rand(20)
y_scatter = np.random.rand(20)
plt.figure(figsize=(6,4))
plt.scatter(x_scatter, y_scatter, color='purple', s=100, alpha=0.7)
plt.title("Scatter con estilo personalizado")
plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.show()

# EJERCICIO 7: 
meses = np.arange(1,13)
temp_ciudad1 = [5,6,9,12,16,20,23,22,18,13,8,5]
temp_ciudad2 = [2,3,6,10,14,18,21,21,17,12,6,3]

plt.figure(figsize=(8,4))
plt.fill_between(meses, temp_ciudad1, color='orange', alpha=0.4, label='Ciudad 1')
plt.fill_between(meses, temp_ciudad2, color='blue', alpha=0.4, label='Ciudad 2')
plt.plot(meses, temp_ciudad1, color='orange', marker='o')
plt.plot(meses, temp_ciudad2, color='blue', marker='o')
plt.title("Temperaturas medias mensuales")
plt.xlabel("Mes")
plt.ylabel("Temperatura (°C)")
plt.xticks(meses)
plt.legend()
plt.show()

# EJERCICIO 8
gastos = [700,250,100,150,50]
categorias = ['Alquiler','Comida','Transporte','Entretenimiento','Otros']
colors = sns.color_palette('pastel')[0:5]

plt.figure(figsize=(5,5))
plt.pie(gastos, labels=categorias, autopct='%1.1f%%', colors=colors, startangle=90, shadow=True)
plt.title("Distribución de gastos mensuales")
plt.show()

# EJERCICIO 9
np.random.seed(0)
grupo_A = np.random.normal(80,5,20)
grupo_B = np.random.normal(75,10,20)
grupo_C = np.random.normal(85,7,20)

data_box = [grupo_A, grupo_B, grupo_C]
labels_box = ['Grupo A','Grupo B','Grupo C']

plt.figure(figsize=(6,4))
plt.boxplot(data_box, labels=labels_box, patch_artist=True,
            boxprops=dict(facecolor='lightblue'),
            medianprops=dict(color='red', linewidth=2))
plt.title("Distribución de calificaciones por grupo")
plt.ylabel("Calificaciones")
plt.show()

# EJERCICIO 10
cat1 = np.random.normal(50,5,30)
cat2 = np.random.normal(55,7,30)
cat3 = np.random.normal(60,6,30)
cat4 = np.random.normal(65,4,30)

data_violin = pd.DataFrame({
    'Cat 1': cat1,
    'Cat 2': cat2,
    'Cat 3': cat3,
    'Cat 4': cat4
})

plt.figure(figsize=(8,4))
sns.violinplot(data=data_violin, palette='Set2')
plt.title("Comparación de distribuciones (Violin Plot)")
plt.ylabel("Valores")
plt.show()

# Violin con media y mediana
plt.figure(figsize=(8,4))
sns.violinplot(data=data_violin, palette='Set3', inner=None)
sns.pointplot(data=data_violin, estimator=np.mean, color='red', markers='o', linestyles='')
sns.pointplot(data=data_violin, estimator=np.median, color='blue', markers='D', linestyles='')
plt.title("Violin Plot con media (rojo) y mediana (azul)")
plt.show()

# Violin con datos simulados de estudiantes
estudiantes = pd.DataFrame({
    'Matemáticas': np.random.normal(75,10,50),
    'Física': np.random.normal(70,12,50),
    'Química': np.random.normal(65,15,50)
})

plt.figure(figsize=(8,4))
sns.violinplot(data=estudiantes, palette='Pastel1', inner='quartile')
plt.title("Distribución de calificaciones por materia")
plt.ylabel("Calificación")
plt.show()