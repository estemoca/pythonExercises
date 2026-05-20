import random

def generar_mazo():
    """Genera un mazo de 52 cartas de póker desordenado."""
    palos = ['c', 't', 'd', 'p']
    valores = list(range(1, 14))
    
    mazo = []
    for palo in palos:
        for valor in valores:
            mazo.append(f"{valor}{palo}")
            
    random.shuffle(mazo)
    return mazo

# Generar y mostrar el mazo
mazo_desordenado = generar_mazo()
print(mazo_desordenado)
print(f"\nNúmero de cartas en el mazo: {len(mazo_desordenado)}")


def separar_cartas_por_palo(mazo):
    """
    Separa las cartas de un mazo en 4 listas, una por palo,
    y conserva solo los valores numéricos.
    """
    corazones = []
    treboles = []
    diamantes = []
    picas = []
    
    for carta in mazo:
        palo = carta[-1]
        valor = int(carta[:-1])
        
        if palo == 'c':
            corazones.append(valor)
        elif palo == 't':
            treboles.append(valor)
        elif palo == 'd':
            diamantes.append(valor)
        elif palo == 'p':
            picas.append(valor)
            
    return corazones, treboles, diamantes, picas

# Generar el mazo desordenado
mazo_desordenado = generar_mazo()

# Separar y obtener las 4 listas con solo los números
corazones, treboles, diamantes, picas = separar_cartas_por_palo(mazo_desordenado)

# Imprimir los resultados
print("Cartas de Corazones (c):", corazones)
print("Cartas de Treboles (t):", treboles)
print("Cartas de Diamantes (d):", diamantes)
print("Cartas de Picas (p):", picas)
