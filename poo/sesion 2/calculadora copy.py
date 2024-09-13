import operaciones
import mensaje

def calculadora():
    print("Bienvenido a calculadora")
    num1 = int(input("ingrese el primer numero"))
    num2 = int(input("ingrese el segundo numero"))

    resSuma= operaciones.resta(num1,num2)
    print(resSuma)
calculadora()


