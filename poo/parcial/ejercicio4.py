class calificacionProducto():
    def __init__(self):
        self.calificacionTotal=0
        self.numeroCalificaciones=0
    
    def ingresarCalificacion(self,nota):
        if nota>=1 and nota <=5:
            self.calificacionTotal+=nota
            self.numeroCalificaciones+=1
            print("se ha ingresado la nota")
        else:
            print("nota no valida")

    def mostrarPromedio(self):
        if self.numeroCalificaciones>0:
            return self.calificacionTotal / self.numeroCalificaciones
        else:
            return  False

def menu():
    print("Bienvenidos al promedio de calificaciones")
    calificaciones = calificacionProducto()
    while True:
        opcion = int(input("1 ingresar calificacion\n 2 rmostrar promedio \n 3 salir"))
        if opcion ==1 :
            nota =  float(input("ingrese la nota"))
            calificaciones.ingresarCalificacion(nota)
        elif opcion ==2:  
            promedio =calificaciones.mostrarPromedio()          
            if promedio==False:
                print("promedio no se puede realizar debe tener al menos una nota")
                continue
            else:
                print(f"el resultado del promedio {promedio}")

        elif opcion ==3:
            del calificaciones
            break
        else:
            print("opcion invalida")


menu()
        
        