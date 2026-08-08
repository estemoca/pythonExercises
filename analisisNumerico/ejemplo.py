import matplotlib.pyplot as plt

# Definición de variables y constantes
m, c, g = 68.1, 12.5, 9.8
dt, t_max, t, v = 2.0, 20.0, 0.0, 0.0

# Listas para almacenar los datos que se van a graficar
tiempos = [t]
velocidades = [v]

# Bucle de simulación (Método de Euler)
while t < t_max:
    dvdt = g - (c/m)*v
    v = v + dvdt*dt
    t = t + dt
    
    # Guardar los valores calculados en las listas
    tiempos.append(t)
    velocidades.append(v)
    
    print(f"t={t:5.1f}  v={v:7.3f}")

# Configuración de la gráfica con matplotlib
plt.figure(figsize=(8, 5))
plt.plot(tiempos, velocidades, marker='o', color='blue', label='Método de Euler')

# Diseño y etiquetas
plt.title('Velocidad del Paracaidista en función del Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.legend()

# Mostrar la gráfica en pantalla
plt.show()
