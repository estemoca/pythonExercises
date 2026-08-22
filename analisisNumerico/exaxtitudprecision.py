#Problema real: tu celular da 10 lecturas de GPS en el mismo punto. Si todas caen juntas pero desplazadas 15 m del punto real, el GPS es preciso pero inexacto (sesgo de calibración).#

import numpy as np
import matplotlib.pyplot as plt
 
g_real = 9.80
 
instrumento_A = np.random.normal(9.95, 0.02, 8)  # preciso, sesgado
instrumento_B = np.random.normal(9.80, 0.15, 8)  # exacto, disperso
 
for nombre, datos in [("A", instrumento_A), ("B", instrumento_B)]:
    exactitud = abs(np.mean(datos) - g_real)
    precision = np.std(datos)
    print(f"{nombre}: media={np.mean(datos):.3f}  "
          f"exactitud(error)={exactitud:.3f}  precision(std)={precision:.3f}")


plt.figure(figsize=(8, 5))

# Graficar los puntos de cada instrumento (usamos el índice 1 a 8 para el eje X)
plt.scatter(range(1, 9), instrumento_A, color='blue', label='Instrumento A (Preciso, Sesgado)', s=100)
plt.scatter(range(1, 9), instrumento_B, color='orange', label='Instrumento B (Exacto, Disperso)', s=100)

# Línea horizontal que representa el valor real de la gravedad
plt.axhline(y=g_real, color='red', linestyle='--', linewidth=2, label=f'Valor Real (g = {g_real})')

# Personalización del gráfico
plt.title('Comparación de Instrumentos: Exactitud vs Precisión')
plt.xlabel('Número de Medición')
plt.ylabel('Valor de Gravedad medido (m/s²)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Mostrar la gráfica en pantalla
plt.show()