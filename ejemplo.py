import pandas as pd

# Leer el archivo CSV
df = pd.read_excel('Ejercicio15000.xls')
print("Datos originales:\n", df)

# Calcular las ventas totales (Precio * Cantidad)
df['Nombre Completo '] = df['Apellidos'] + df['Nombres']

# Agrupar por producto y sumar las ventas totales
cartera_totales = df.groupby('Sexo')['Cartera'].reset_index()
print("Cartera por sexo:\n", cartera_totales)
print(df)

# Guardar las ventas totales por producto en un nuevo archivo CSV
cartera_totales.to_csv('cartera.csv', index=False)