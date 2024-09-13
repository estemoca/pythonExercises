class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def incrementar_stock(self, cantidad):
        self.cantidad += cantidad
        print(f"Stock de {self.nombre} incrementado en {cantidad}. Total: {self.cantidad} unidades.")

    def reducir_stock(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Stock de {self.nombre} reducido en {cantidad}. Total: {self.cantidad} unidades.")
        else:
            print("No hay suficiente stock para reducir esa cantidad.")

    def consultar_precio(self):
        return f"Precio de {self.nombre}: {self.precio}€ por unidad."

# Ejemplo de uso
producto = Producto("Manzana", 0.5, 100)
producto.incrementar_stock(50)
producto.reducir_stock(30)
print(producto.consultar_precio())

producto2 = Producto("pera",1500,50)
print(producto2.consultar_precio())