import matplotlib.pyplot as plt

def solicitar_variables():
    print("welcome to calc ")
    masa = input("ingrese el valor de la masa del paracaidista (kg) [default: 90]: ")
    gravedad = input("ingrese el valor de la gravedad (m/s^2) [default: 9.81]: ")
    coef1 = input("ingrese el valor del coeficiente 1 (kg/s) [default: 12.5]: ")
    coef2 = input("ingrese el valor del coeficiente 2 (kg/s) [default: 90.0]: ")
    tiempo_abrir = input("ingrese el tiempo de apertura del paracaidas (s) [default: 5.0]: ")
    tiempo_total = input("ingrese el tiempo total de caida (s) [default: 60.0]: ")
    delta_t = input("ingrese el paso de tiempo (s) [default: 0.1]: ")   

    return (float(masa) if masa else 90.0,
            float(gravedad) if gravedad else 9.81,
            float(coef1) if coef1 else 12.5,
            float(coef2) if coef2 else 90.0,
            float(tiempo_abrir) if tiempo_abrir else 5.0,
            float(tiempo_total) if tiempo_total else 60.0,
            float(delta_t) if delta_t else 0.1)

def simular_caida(m, g, k1, k2, t_open, t_max, dt):
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

def graficar_resultados(time, vel):
    plt.figure(figsize=(8, 5))
    plt.plot(time, vel, color='darkblue', linewidth=2, label='Velocidad del paracaidista')
    plt.axvline(x=20, color='red', linestyle='--', label='Apertura del paracaídas (t=20s)')

    plt.title('Simulación de la Velocidad: Apertura del Paracaídas')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Velocidad (m/s)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.show()

masa, gravedad, coef1, coef2, tiempo_abrir, tiempo_total, delta_t = solicitar_variables()

tiempo, velocidades = simular_caida(masa, gravedad, coef1, coef2, tiempo_abrir, tiempo_total, delta_t)
graficar_resultados(tiem=po, velocidades)