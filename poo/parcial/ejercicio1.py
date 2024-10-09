class CalculadoraDescuento:
    def __init__(self):
        
        self.precioUnitario = 0
        self.cantidad =0
    def ingresarDatos(self):                
        self.precioUnitario = float(input("Ingrese el valor unitario del producto"))
        self.cantidad = float(input("Ingrese la cantidad a comprar del producto"))

        if self.precioUnitario>0 and self.cantidad>0:
            return True
        else:
            return False
    
    def calcularPrecioFinal(self):
        if self.cantidad>=10:
            return (self.cantidad*self.precioUnitario)*0.9
            # return (self.cantidad*self.precioUnitario)-((self.cantidad*self.precioUnitario)*10/100)
        else:
            return (self.cantidad*self.precioUnitario)

def menu():
    print("Bienvenidos, a nuestra calculadora de descuento")
    finalProducto = CalculadoraDescuento()
    while True:
        opcion= int(input("1 ingresar datos\n 2 calcular precio final \n 3 salir\n"))
        if opcion == 1:
            if finalProducto.ingresarDatos() :
                print("datos ingresados correctamente ")
            else:
                print("la cantidad o el precio deben ser mayores a 0 ")
                continue
        elif opcion ==2:
            print(f" el precio total es {round(finalProducto.calcularPrecioFinal(),2)}")
        elif opcion == 3:
            del finalProducto
            break
        else:
            print("opcion invalida")

menu()
