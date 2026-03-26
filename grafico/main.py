import matplotlib.pyplot as plt
import numpy as np
notas = [4, 5, 6, 6, 7, 8, 9, 10]

minimo = np.min(notas)
print(minimo)
maximo = np.max(notas)

plt.boxplot(notas)
print(maximo)
