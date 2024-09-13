try:
    archivo = open("C:\wamp642\www\phytonejercicios\poo\sesion 2\datos.txt","r")
    contenido = archivo.read()
    
except FileNotFoundError:
    print("no se encontro el archivo")
else:
    print("el archivo fue leido")
    print(contenido)
finally:
    print("se termino la lectura")