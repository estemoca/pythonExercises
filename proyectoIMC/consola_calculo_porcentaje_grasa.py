import calculadora_indices as calc


print("Calcula el porcentaje de grasa corporal de una persona.")
peso = int(input("Ingrese el peso de la persona en KG"))
altura = float(input("Ingrese la altura de la persona en metros"))
edad = float(input("Ingrese la edad de la persona en metros"))
valor_genero = float(input("Ingrese el valor de genero de la persona en metros 10.8 masculino y 0 femenino"))

iMC=calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)

print(f"El indice de grasa corporal es {iMC}")
