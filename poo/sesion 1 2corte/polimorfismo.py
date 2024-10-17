class MotorElectrico:
    def encender(self):
        print("Motor eléctrico encendido")

class MotorGasolina:
    def encender(self):
        print("Motor de gasolina encendido")

class Coche:
    def __init__(self, motor):
        self.motor = motor

    def arrancar(self):
        self.motor.encender()

# Ejemplo de uso
motor_electrico = MotorElectrico()
coche_electrico = Coche(motor_electrico)
coche_electrico.arrancar()  # Output: Motor eléctrico encendido

motor_gasolina = MotorGasolina()
coche_gasolina = Coche(motor_gasolina)
coche_gasolina.arrancar()  # Output: Motor de gasolina encendido