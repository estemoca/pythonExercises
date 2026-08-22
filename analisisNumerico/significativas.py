#Problema real: una balanza de laboratorio solo entrega 3 dígitos confiables (68.1 kg). Si el cálculo final imprime 53.409398 m/s, estás mintiendo sobre la precisión del dato.#

def cifras_significativas(numero_str):
    s = numero_str.strip().lower()
    if 'e' in s:
        print(s)
        s = s.split('e')[0]
        print(s)
    s = s.lstrip('0')
    if '.' in s:
        print(s)
        s = s.replace('.', '')
    else:
        s = s.rstrip('0') or '0'

    print(s)
    return len(s) if s else 0


lista = ["0.0025", "2500", "2.5e3", "100.03", "68.1"]

for e in lista:
    print(f"{e:>8} -> {cifras_significativas(e)} cifras")
 
# Regla de oro: no reportar más precisión de la que hay
velocidad = 53.409398471
print(f"Reporte correcto: {velocidad:.1f} m/s")  #
