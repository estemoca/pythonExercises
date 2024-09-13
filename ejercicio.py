import numpy as np # type: ignore

# Cargar datos desde un archivo CSV
data = np.genfromtxt('15000.csv', delimiter=';')

# Calcular estadísticas básicas de una columna
columna = data[:,14 ]  # Suponiendo que la segunda columna contiene los datos de interés
nn= data[:,1]

media = np.mean(columna)
mediana = np.median(columna)
desviacion_estandar = np.std(columna)

print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion_estandar)

# Filtrar datos basados en condiciones
columna_filtrada = data[data[:, 15] > 50, 0]  # Filtrar las filas donde el valor en la segunda columna es mayor que 50 y seleccionar la primera columna

print("Columna filtrada:", columna_filtrada)

