import pandas as pd

# Definición de la función para calcular estadísticas
def calcular_estadisticas(descargas: pd.DataFrame) -> pd.DataFrame:
    data = descargas[descargas["PAGO"] != 0]
    cant = data.groupby("MODELO")["PAGO"].count()
    prom = data.groupby("MODELO")["PAGO"].mean()
    estr = data.groupby("MODELO")["ESTRELLAS"].mean()
    desv = data.groupby("MODELO")["ESTRELLAS"].std().fillna(0.0)
    mayor = data.groupby("MODELO")["PAGO"].max()
    menor = data.groupby("MODELO")["PAGO"].min()
    comentarios = data[data["COMENTARIO"] == True].groupby("MODELO")["COMENTARIO"].count().fillna(0)

    datos = {"CANTIDAD": cant, "PROMEDIO": prom, "MAXIMO": mayor, "MINIMO": menor,
    "ESTRELLAS": estr, "DESV. ESTRELLAS": desv, "COMENTARIOS": comentarios}
    solucion = pd.DataFrame(datos).fillna(0)
    return round(solucion, 2)

# Datos de prueba
datos = {
'MODELO': ['Bus urbano #27', 'Silla tipo bar', 'Piano', 'Fuente con flores', 'Bus urbano #27', 'Puesto de Yogurt', 'Playground', 'Bus urbano #27', 'LeCorbusier_2020'],
'USUARIO': ['Ted Mosby', 'Art Vandelay', 'Art Vandelay', 'Michael', 'Mark Brendanawicz', 'Michael', 'Mark Brendanawicz', 'LeCorbusier_2020', 'LeCorbusier_2020'],
'PAGO': [24.99, 4.99, 4.99, 0, 12, 0, 14, 0, 0],
'ESTRELLAS': [5, 3.5, 3.5, 5, 4, 5, 4.5, 1, 1],
'COMENTARIO': [True, False, False, True, True, True, True, True, True]
}

df = pd.DataFrame(datos)

# Calculando estadísticas
resultado = calcular_estadisticas(df)
print(resultado)