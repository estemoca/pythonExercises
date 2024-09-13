import pandas as pd

saldo2 = 1500000
# Crear el DataFrame
data = {
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E'],
    'Categoría': ['Categoría 1', 'Categoría 2', 'Categoría 1', 'Categoría 3', 'Categoría 2'],
    'Cantidad': [50, 20, 30, 10, 40],
    'Precio Unitario': [10.0, 20.0, 15.0, 25.0, 10.0]
}

df = pd.DataFrame(data)

# 1. Calcular el valor total del inventario por producto
df['Valor Total'] = df['Cantidad'] * df['Precio Unitario']
print("Datos con valor total del inventario por producto:\n", df)

# 2. Calcular el valor total del inventario de la tienda
valor_total_inventario = df['Valor Total'].sum()
print("\nValor total del inventario de la tienda:", valor_total_inventario)

# 4. Calcular el valor total del inventario por categoría
valor_total_por_categoria = df.groupby('Categoría')['Valor Total'].sum()
print("\nValor total del inventario por categoría:\n", valor_total_por_categoria)
