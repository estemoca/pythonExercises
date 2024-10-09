class RegistroTrabajo:
    def __init__(self):
        
        self.horasTrabajadas = 0
        self.TarifaPorHora =0
    def ingresarDatos(self):                
        self.horasTrabajadas = float(input("Ingrese el valor unitario del producto"))
        self.TarifaPorHora = float(input("Ingrese la cantidad a comprar del producto"))

        if self.horasTrabajadas>0 and self.TarifaPorHora>0:
            return True
        else:
            return False
    
    def calcularSalarioTotal(self):
            return self.horasTrabajadas*self.TarifaPorHora


def menu():
    print("Bienvenidos, a nuestra calculadora de descuento")
    salario = RegistroTrabajo()
    while True:
        opcion= int(input("1 ingresar datos\n 2 calcular salario \n 3 salir\n"))
        if opcion == 1:
            if salario.ingresarDatos() :
                print("datos ingresados correctamente ")
            else:
                print("el salario o las horas trabajadas deben ser mayores a 0 ")
                continue
        elif opcion ==2:
            print(f" El calculo del salario es {round(salario.calcularSalarioTotal(),2)}")
        elif opcion == 3:
            del salario
            break
        else:
            print("opcion invalida")

menu()
