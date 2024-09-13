import numpy as np
temperaturas = np.array([
    [20.1, 21.3, 22.5, 23.2, 21.8, 20.7, 22.1],  # Lunes
    [19.8, 20.4, 21.2, 22.0, 21.0, 20.3, 21.7],  # Martes
    [18.7, 19.5, 20.3, 21.1, 20.0, 19.2, 20.8],  # Miércoles
    [20.3, 21.0, 22.1, 23.0, 22.2, 21.1, 22.9],  # Jueves
    [19.9, 20.7, 21.6, 22.4, 21.5, 20.9, 22.2],  # Viernes
    [18.9, 19.8, 20.7, 21.5, 20.6, 19.9, 21.3],  # Sábado
    [20.5, 21.6, 22.8, 23.5, 22.7, 21.5, 23.1]   # Domingo
])
promedioDias=[]

for dia in temperaturas :    
    promedioDia=0
    for pro in dia:
        print(pro)
        promedioDia+=pro
    promedioDias.append(promedioDia/7)
    print(promedioDias)
# lunesDia = np.mean(temperaturas[0][0])
# martesDia = np.mean(temperaturas[0][1])
# miercolesDia = np.mean(temperaturas[0][2])
# juevesDia = np.mean(temperaturas[0][3])
# viernesDia = np.mean(temperaturas[0][4])
# sabadoDia = np.mean(temperaturas[0][5])
# domingoDia = np.mean(temperaturas[0][6])
# print(lunesDia)
# print(martesDia)
# print(miercolesDia)
# print(juevesDia)
# print(viernesDia)
# print(sabadoDia)
# print(domingoDia)
max_diarios = np.max(temperaturas, axis=1)
min_diarios = np.min(temperaturas, axis=1)
print("Temperatura máxima de cada día:", max_diarios)
print("Temperatura mínima de cada día:", min_diarios)

promedios_diarios = np.mean(temperaturas, axis=1)
print("Temperatura promedio de cada día:", promedios_diarios)
# 2. Calcular la temperatura máxima y mínima de cada día
max_diarios = np.max(temperaturas, axis=1)
min_diarios = np.min(temperaturas, axis=1)
print("Temperatura máxima de cada día:", max_diarios)
print("Temperatura mínima de cada día:", min_diarios)

# 3. Calcular la temperatura promedio semanal
promedio_semanal = np.mean(temperaturas)
print("Temperatura promedio semanal:", promedio_semanal)

# 4. Calcular la desviación estándar de las temperaturas de la semana
desviacion_std = np.std(temperaturas)
print("Desviación estándar de las temperaturas:", desviacion_std)

# 5. Obtener la temperatura más alta y más baja de la semana
max_semanal = np.max(temperaturas)
min_semanal = np.min(temperaturas)
print("Temperatura más alta de la semana:", max_semanal)
print("Temperatura más baja de la semana:", min_semanal)
