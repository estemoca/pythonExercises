import numpy as np
import matplotlib.pyplot as plt

m = 90
g = 9.81
k1 = 12
k2 = 140
t_open = 20
t_max = 40
dt = 0.1  # REDUCIDO para corregir la inestabilidad numérica

tiempo = []
velocidades = []
t = 0
v = 0

while t < t_max:
    if t < t_open:
        a = g - (k1 / m) * v
    else:
        a = g - (k2 / m) * v
    v = v + a * dt
    t = t + dt
    tiempo.append(t)
    velocidades.append(v)

# Gráfica optimizada
plt.figure(figsize=(8, 5))
plt.plot(tiempo, velocidades, color='darkblue', linewidth=2, label='Velocidad del paracaidista')
plt.axvline(x=20, color='red', linestyle='--', label='Apertura del paracaídas (t=20s)')

plt.title('Simulación de la Velocidad: Apertura del Paracaídas')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()
