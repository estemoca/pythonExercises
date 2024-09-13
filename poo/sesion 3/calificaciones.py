class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
        print(f"Calificación {calificacion} añadida para {self.nombre}.")

    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0

# Ejemplo de uso
estudiante = Estudiante("María López")
estudiante.agregar_calificacion(90)
estudiante.agregar_calificacion(85)
estudiante.agregar_calificacion(92)
print(f"Promedio de {estudiante.nombre}: {estudiante.promedio()}")