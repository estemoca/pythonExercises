class Pasajero:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad    
    
    # mesaje de respuesta 
    def __str__(self):
        return f'Nombre: {self._nombre}, Edad: {self._edad}'
    
    #getters
    def get_nombre(self):
        return  self._nombre
    def get_edad(self):
        return  self._nombre
    #setter 
    def set_nombre(self,nombre):
        self._nombre = nombre
    def set_edad(self,edad):
        self._edad = edad
