class Vehiculo:
    def __init__(self,marca,modelo,ano,color):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color
        self.encendido=False
        self.marcha = 0
    
    def encender(self):
        if not self.encendido:
            self.encendido=True
            print("el vehiculo ya fue encendido ")
        else:
            print("el vehiculo ya se encuentra encendido")
    def apagar(self):
        if  self.encendido:
            self.encendido=False
            print("el vehiculo ya fue apagado ")
        else:
            print("el vehiculo ya se encuentra apagado")
    def pitar(self):
        if self.encendido:
            print("Piiiiiiiiiiiiiiiiiiiii")
        else:
            print("el vehiculo no esta encendido")

    def girar(self,giro):
        if self.encendido:
            print(f"el vehiculo esta girando hacia la {giro}")
        else:
            print("el vehiculo no esta encendido")
    
    def mostrarInfo(self):
        print(f" El vehiculo de marca {self.marca} de modelo {self.modelo} del año {self.ano} de color {self.color}")

    def cambiarMarcha(self,marcha):
        if self.encendido:
           
            if self.marcha == marcha:
                print("el vehiculo ya se encuentra en esa marcha")
            else:   
                self.marcha = marcha
                print(f"la marcha del vehiculo es {self.marcha}")
        else:
            print("el vehiculo no esta encendido")            

def menu():
        print("bienvenidos a el sistema de vehiculos")
        marca = input("Ingrese la marca del vehiculo ")
        modelo = input("Ingrese la modelo del vehiculo ")
        año = input("Ingrese la año del vehiculo ")
        color = input("Ingrese la color del vehiculo ")

        veN = Vehiculo(marca,modelo,año,color)
        while True:        
            opcion = int(input("1: encender \n 2: apagar \n 3: pitar \n 4: girar \n 5:cambiar marcha \n 6:informacion vechiulo \n 7: salir\n"))
            if opcion==1:
                veN.encender()
            elif opcion==2:
                veN.apagar()
            elif opcion==3:
                veN.pitar()
            elif opcion==4:
                giro = input("ingrese hacia donde desea girar derecha - izquierda")
                veN.girar(giro)
            elif opcion==5:
                marcha = int(input("ingrese la marcha"))
                veN.cambiarMarcha(marcha)
            elif opcion==6:
                veN.mostrarInfo()
            elif opcion==7:
                del veN
                print("gracias por usarnos")
                break

menu()
