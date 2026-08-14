import numpy as np
import matplotlib.pyplot as plt

def solicitar_variables():

    print("=== CONFIGURACIÓN DE LA SIMULACIÓN DE CAÍDA LIBRE ===")
    print("Presiona [Enter] en cualquier opción para usar el valor sugerido.\n")
    
    def pedir_float(mensaje, default):
        entrada = input(f"{mensaje} [{default}]: ").strip()
        return float(entrada) if entrada else default

    try:
        m = pedir_float("Masa del paracaidista (kg)", 90.0)
        g = pedir_float("Aceleración de la gravedad (m/s²)", 9.81)
        k1 = pedir_float("Coeficiente de resistencia en caída libre (k1)", 12.0)
        k2 = pedir_float("Coeficiente de resistencia con paracaídas (k2)", 140.0)
        t_open = pedir_float("Tiempo en el que abre el paracaídas (segundos)", 20.0)
        t_max = pedir_float("Tiempo total de simulación (segundos)", 40.0)
        dt = pedir_float("Paso de tiempo numérico - dt (segundos recomendado < 0.1)", 0.05)
        
        return m, g, k1, k2, t_open, t_max, dt
    except ValueError:
        print("\n❌ Error: Ingresaste un valor no numérico. Se usarán los valores por defecto.")
        return 90.0, 9.81, 12.0, 140.0, 20.0, 40.0, 0.05


def simular_caida(m, g, k1, k2, t_open, t_max, dt):
    """Calcula las listas de tiempo y velocidad usando el método de Euler."""
    tiempo = []
    velocidades = []
    t, v = 0.0, 0.0

    while t < t_max:
        if t < t_open:
            a = g - (k1 / m) * v
        else:
            a = g - (k2 / m) * v
            
        v = v + a * dt
        t = t + dt
        
        tiempo.append(t)
        velocidades.append(v)
        
    return tiempo, velocidades


def graficar_resultados(tiempo, velocidades, t_open):
    """Genera y muestra la gráfica personalizada con los datos obtenidos."""
    plt.figure(figsize=(8, 5))
    plt.plot(tiempo, velocidades, color='teal', linewidth=2.5, label='Velocidad calculada')
    plt.axvline(x=t_open, color='crimson', linestyle='--', linewidth=1.5, label=f'Apertura (t={t_open}s)')

    plt.title('Simulación Personalizada: Velocidad del Paracaidista', fontsize=12, fontweight='bold')
    plt.xlabel('Tiempo (segundos)', fontsize=10)
    plt.ylabel('Velocidad (m/s)', fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.show()


# --- Flujo Principal del Programa ---

    # 1. Solicitar los datos al usuario de forma dinámica
masa, gravedad, coef1, coef2, tiempo_abrir, tiempo_total, delta_t = solicitar_variables()
print("\nSimulando... Por favor espera...")
    
    # 2. Correr la simulación matemática con las variables elegidas
lista_t, lista_v = simular_caida(masa, gravedad, coef1, coef2, tiempo_abrir, tiempo_total, delta_t)
    
    # 3. Entregar los resultados visuales en la gráfica
print("¡Listo! Mostrando la gráfica en pantalla.")
graficar_resultados(lista_t, lista_v, tiempo_abrir)

