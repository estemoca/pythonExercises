# Clase base
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        return f"Motor {self.tipo} encendido"

# Clase derivada que usa composición
class Coche:
    def __init__(self, marca, motor_tipo):
        self.marca = marca
        self.motor = Motor(motor_tipo)

    def descripcion(self):
        return f"Marca: {self.marca}, {self.motor.encender()}"

# Uso de las clases
mi_coche = Coche("Toyota", "Eléctrico")
print(mi_coche.descripcion())