import random

def tirar_dados():    
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
        
    print(f"Tirada del dado 1: {dado1}")
    print(f"Tirada del dado 2: {dado2}")
        
    suma = dado1 + dado2
    print(f"Suma de los dos dados: {suma}")

def main():
    while True:
        tirar_dados()
                
        respuesta = input("¿Quieres tirar los dados otra vez? (s/n): ").strip().lower()
        
        if respuesta != 's':
            print("¡Gracias por jugar! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()