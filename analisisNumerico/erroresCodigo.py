# ==========================================
# PARTE 1: Evaluación con el Valor Verdadero
# ==========================================
# Problema real: Un túnel de viento mide 53.4 m/s (valor real).
# Tu modelo numérico calculó 52.8 m/s (valor aproximado).
# Usamos esta función para saber qué tan desfasado está el modelo.

def errores(v_verdadero, v_aprox):
    # Error absoluto (Et): Diferencia directa entre el valor real y el aproximado.
    # Mide la discrepancia en las mismas unidades originales (m/s).
    Et = v_verdadero - v_aprox  
    
    # Error relativo (et_rel): Pone el error en perspectiva dividiéndolo entre el valor real.
    et_rel = Et / v_verdadero
    
    # Error porcentual (et_pct): Convierte el error relativo en un porcentaje fácil de interpretar.
    # Usamos abs() por si el valor aproximado fuera mayor que el real, evitando porcentajes negativos.
    et_pct = abs(et_rel) * 100
    
    return Et, et_rel, et_pct
 
# Llamamos a la función con los datos del túnel de viento (53.4 real vs 52.8 del modelo)
Et, et_rel, et_pct = errores(53.4, 52.8)

# Imprimimos los resultados formateados con decimales específicos
print(f"Error absoluto: {Et:.3f}")        # Muestra la diferencia neta
print(f"Error relativo: {et_rel:.5f}")    # Muestra la proporción del error
print(f"Error porcentual: {et_pct:.2f}%\n") # Muestra el porcentaje de desviación (aprox. 1.12%)


# ==========================================================
# PARTE 2: Error Aproximado (Cuando NO hay valor verdadero)
# ==========================================================
# En la vida real, muchas veces no conocemos el resultado exacto de antemano.
# Por lo tanto, medimos qué tanto cambia el resultado de una iteración (paso) a la siguiente.

def error_aproximado(v_nuevo, v_anterior):
    # Compara el valor actual con el anterior para ver el cambio porcentual.
    # Si el cambio es muy pequeño, significa que el modelo ya se estabilizó (convergió).
    return abs((v_nuevo - v_anterior) / v_nuevo) * 100
 
# Historial de simulaciones iterativas: el modelo va afinando su cálculo paso a paso
historial = [40.0, 48.5, 52.1, 53.0, 53.35]

# Recorremos el historial desde la segunda posición (índice 1) en adelante 
# para poder restarle el valor anterior (i - 1).
for i in range(1, len(historial)):
    # Calculamos el error aproximado entre el paso actual y el paso anterior
    ea = error_aproximado(historial[i], historial[i - 1])
    
    # Imprimimos el progreso de cada iteración y su respectivo error de cambio
    print(f"Iteración {i}: v={historial[i]:.2f}  ea={ea:.2f}%")