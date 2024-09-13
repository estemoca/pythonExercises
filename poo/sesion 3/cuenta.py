class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad}. Saldo actual: {self.saldo}€.")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}€. Saldo actual: {self.saldo}€.")
        else:
            print("Fondos insuficientes.")

    def consultar_saldo(self):
        return f"Saldo actual: {self.saldo}€."

# Ejemplo de uso
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.consultar_saldo())