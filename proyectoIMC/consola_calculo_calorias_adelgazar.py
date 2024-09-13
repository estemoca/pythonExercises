import calculadora_indices as calc


print("Calcula la cantidad de calorías que una persona quema en reposo (tasa metabólica basal).")
peso = int(input("Ingrese el peso de la persona en KG"))
altura = float(input("Ingrese la altura de la persona en metros"))
edad = float(input("Ingrese la edad de la persona en metros"))
valor_genero = float(input("Ingrese el Valor que varía según el género de la persona: 5 para masculino y -161 para femenino."))

print(calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero))
