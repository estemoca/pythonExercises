
#funcion para agregar un producto dentro del inventario
def agregar_producto(inventario, nombre, precio, cantidad):
    inventario.append({"nombre":nombre,"precio":precio,"cantidad":cantidad})
    print("Producto agregado al inventario")

def actualizar_inventario(inventario, nombre,precio, cantidad ):
    for producto in inventario:
        if producto["nombre"]==nombre:
            producto["cantidad"]=cantidad
            producto["precio"]=precio
            print(f"Producto {nombre} a sido actualizado")
            return

    print("el producto no ha sido encontrado ")

def eliminar_producto(inventario,nombre):
    for producto in inventario:
        if producto["nombre"]==nombre:
            inventario.remove(producto)
            print(f"Producto {nombre} a sido eliminado")
            return

    print("el producto no ha sido encontrado ")

def mostrar_producto(inventario,nombre):
    for producto in inventario:
        if producto["nombre"]==nombre:            
            print(f"Producto con nombre {nombre}\n tiene un precio de {producto["precio"]}\n  y una cantidad de {producto["cantidad"]}")
            return

    print("el producto no ha sido encontrado ")
 
def main():
    inventario=[]
    while True:
        print("--Bienvenidos al inventario-- ")
        print("1 -- Agregar producto")
        print("2 -- Actualizar producto")
        print("3 -- Eliminar producto")
        print("4 -- Mostrar producto")
        print("5 -- Salir")
        
        opcion= int(input("Ingrese la opcion deseada"))

        if opcion ==1:
            nombre = input("ingrese el nombre del producto")
            precio = float(input("ingrese el precio del producto "))
            cantidad = int(input("ingrese el cantidad del producto "))
            agregar_producto(inventario,nombre,precio,cantidad)
            print(inventario)
        elif opcion ==2:    
            nombre = input("ingrese el nombre del producto")
            precio = float(input("ingrese el precio del producto "))
            cantidad = int(input("ingrese el cantidad del producto "))
            actualizar_inventario(inventario,nombre,precio,cantidad)
            print(inventario)
        elif opcion ==3:  
            nombre = input("ingrese el nombre del producto")
            eliminar_producto(inventario,nombre)
            print(inventario)
        elif opcion ==4:
            nombre = input("ingrese el nombre del producto")
            mostrar_producto(inventario,nombre)
            print(inventario)    
        elif opcion ==5: 
            print("gracias por usarnos")
            break   
        else:
            print("opcion invalida")    


main()