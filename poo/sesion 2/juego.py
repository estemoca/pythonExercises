import random

def playTurn(jugAta, jugDef, vidaJugAta, vidaJugDef):    
    ataque = int(input(f"{jugAta} Ingrese su valor de ataque de 1 a 5"))       
    defensa = int(input(f"{jugDef} Ingrese su valor de defensa de 1 a 5")) 
    print(f"{jugAta} ataca con {ataque}. {jugDef} defiende con {defensa}.")
    if ataque != defensa:
        vidaJugDef -= 10
        print(f"{jugDef} ha fallado la defensa. Pierde 10 puntos de vida.")
    else:
        print(f"{jugDef} ha acertado la defensa. No pierde puntos de vida.")
    print(f"Vida de {jugAta}: {vidaJugAta}, Vida de {jugDef}: {vidaJugDef}\n")
    
    return vidaJugAta, vidaJugDef

def play():
    vida_a = 50
    vida_b = 50
    turno = random.randint(1, 2)
    print(turno)
    print(f" Juego ataque defensa COMIENZA ...") 
    jugA = input("ingrese el nombre del jugador 1")
    jugB = input("ingrese el nombre del jugador 2")
    print(f"{jugA} y {jugB} tienen 50 puntos de vida cada uno.\n")
    
    while vida_a > 0 and vida_b > 0:
        if turno == 1:
            print("Turno de ataque de "+ jugA)
            vida_a, vida_b = playTurn(jugA, jugB, vida_a, vida_b)
            turno = 2
        else:
            print("Turno de ataque de "+jugB)
            vida_b, vida_a = playTurn(jugB, jugA, vida_b, vida_a)
            turno = 1

    if vida_a <= 0:
        print(f"{jugB} ha derrotado al {jugA}")
    else:
        print(f"{jugA} ha derrotado al {jugB}")

play()