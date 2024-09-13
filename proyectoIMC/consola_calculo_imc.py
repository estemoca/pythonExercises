# import calculadora_indices as calc
def calcular_IMC(peso:float, altura:float)->float:    
    imc = peso / ((altura) ** 2)
    return imc 

peso = input("Ingrese el peso de la persona en KG")
Altura = input("Ingrese la altura de la persona en metros")
iMC=calcular_IMC(float(peso),float(Altura))
print("El indice de masa corporal es",iMC)
