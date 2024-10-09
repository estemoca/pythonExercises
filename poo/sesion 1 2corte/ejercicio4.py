#    archivo         clase       alias
from Pasajero import Pasajero as ClasePasajeroImp
#esta es la clase principal de pasajero
# class Pasajero:
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad    
    
#     # mesaje de respuesta 
#     def __str__(self):
#         return f'Nombre: {self._nombre}, Edad: {self._edad}'
    
#     #getters
#     def get_nombre(self):
#         return  self._nombre
#     def get_edad(self):
#         return  self._nombre
#     #setter 
#     def set_nombre(self,nombre):
#         self._nombre = nombre
#     def set_edad(self,edad):
#         self._edad = edad

# clase hija de pasajero agrega el nivel
class PasajeroVip(ClasePasajeroImp):
    def __init__(self, nombre, edad, nivel):
        super().__init__(nombre, edad)
        self._nivel =nivel    
    # se muestra mensaje respuesta    
    def __str__(self):
        return f'Nombre: {self._nombre}, Edad: {self._edad}  Nivel: {self._nivel}'
        
    #getter    
    def get_nivel(self):
        return self._nivel
    #setter 
    def set_nivel(self,nivel):
        self._nivel = nivel

# clase principal de ejercicio
class sistemaGestionVuelos:
    def __init__(self):
        self._pasajeros = []
    
    # agrega un pasajero a la lista 
    def  agregar_pasajero(self, pasajero):
        self._pasajeros.append(pasajero)


    def registrar_pasajero(self): 
        nombre = input("Ingrese el nombre del pasajero: ")
        edad = int(input("Ingrese la edad del pasajero: "))
        clase = input("Es usted clase diferente a economy? s/n").lower()
        #1 forma 
        if clase =="s":
            nivel = input("Ingrese el nivel de vip: ")
            pasajero = PasajeroVip(nombre, edad, nivel)
        elif  clase == "n":
            pasajero = ClasePasajeroImp(nombre,edad)  
        # # 2 forma 
        # nivel = input("Ingrese el nivel del pasajero: ") 
        # pasajero = PasajeroVip(nombre,edad,nivel)    
        self.agregar_pasajero(pasajero)
    def mostrar_Pasajero(self):
        for pasajero in self._pasajeros:
            print(pasajero)
    
    def menu(self):
        while True:
            #opciones principales
            print("\nSistema de Gestión de Vuelos")
            op = int(input("1. Registrar Pasajero \n 2.mostrar pasajeros \n 3. salir\n"))
            # condicional con opciones
            if op == 1:
                self.registrar_pasajero()
            elif op == 2:    
                self.mostrar_Pasajero()
            elif op == 3:
                print("Gracias por tu compra")
                break
            else:
                print("Opción no válida")

sistemTravel =  sistemaGestionVuelos()
sistemTravel.menu()


    


        
    