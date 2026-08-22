#Problema real: un banco acumula pequeños errores al sumar tasas de interés muchas veces, porque 0.1 no tiene representación exacta en binario.#
import math

# =====================================================================
# 1. ERROR DE REPRESENTACIÓN EN PUNTO FLOTANTE
# =====================================================================
# Las computadoras guardan decimales en binario (base 2). Como 0.1 y 0.2 
# se vuelven infinitos en binario, la PC los corta y redondea. 
# Ese micro-redondeo acumulado hace que la suma no de 0.3 exacto.
print(0.1 + 0.2)  # Imprime: 0.30000000000000004


# =====================================================================
# 2. PÉRDIDA DE SIGNIFICACIÓN (CANCELACIÓN CATASTRÓFICA)
# =====================================================================

# FORMA INGENUA: Sufre matemáticamente al procesar números muy grandes.
# Si x es gigante, sqrt(x^2 + 1) es casi idéntico a x.
# Restar dos números gigantescos y casi iguales destruye los decimales 
# correctos porque la PC cancela los dígitos del frente y deja basura binaria.
def forma_ingenua(x):
    return math.sqrt(x**2 + 1) - x


# FORMA REESCRITA: Es la solución óptima usando álgebra (racionalización).
# Se transformó la resta en una SUMA dentro del denominador.
# Sumar dos números gigantescos no genera pérdida de precisión. Al final 
# dividimos 1 entre ese número grande, manteniendo los decimales perfectos.
def forma_reescrita(x):
    return 1 / (math.sqrt(x**2 + 1) + x)


# =====================================================================
# 3. PRUEBA CON DIFERENTES TAMAÑOS DE X
# =====================================================================
# Evaluamos x con mil (1e3), un millón (1e6) y cien millones (1e8)
for x in [1e3, 1e6, 1e8]:
    # .0e  -> Muestra x en notación científica sin decimales (ej: 1e+08)
    # .10f -> Fuerza a la consola a mostrar exactamente 10 dígitos decimales
    print(f"x={x:.0e}  ingenua={forma_ingenua(x):.10f}  "
          f"reescrita={forma_reescrita(x):.10f}")

# NOTA AL EJECUTAR: Notarás que en 1e8, la versión "ingenua" ya empieza 
# a dar un resultado totalmente erróneo (cero o valores descontrolados), 
# mientras que la versión "reescrita" conserva la precisión impecable.
