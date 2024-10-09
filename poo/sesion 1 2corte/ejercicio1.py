class vehiculo:
    def __init__ (self,marca,modelo):
        self.__marca =marca
        self.__modelo =modelo
    
    @property
    def getMarca(self):
        return self.__marca
        
    def setMarca(self,marca):
        self.__marca = marca


nuevo = vehiculo("nunu","uhiaus")
print(nuevo.getMarca)
nuevo.setMarca("nana")
print(nuevo.getMarca)


