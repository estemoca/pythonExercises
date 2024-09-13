def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2!=0 and num1!=0:
        return num1/num2
    else:
        return "operacion invalida division imposible"

def calculadora():
    while True:
        print("---Bienvenidos a nuestra calculadora")
        print("1 para suma ")
        print("2 para resta ")
        print("3 para multiplicacion ")
        print("4 para division ")
        print("5 para salir")
        opc= int(input("Ingrese la opcion"))
        numero1 = int(input("ingrese el primer numero "))
        numero2 = int(input("ingrese el segundo numero "))
        if opc==1:
            print(f"El resultado de la suma es: {suma(numero1,numero2)}")
            print(f"El resultado de la suma es: {suma(numero1,numero2)}")
            print(f"El resultado de la suma es: {suma(numero1,numero2)}")
            print(f"El resultado de la suma es: {suma(numero1,numero2)}")

        elif opc==2:
            print(f"El resultado de la resta es: {resta(numero1,numero2)}")
        elif opc==3:
            print(f"El resultado de la multiplicacion es: {multiplicacion(numero1,numero2)}")
        elif opc==4:
            print(f"El resultado de la division es: {division(numero1,numero2)}")


        elif opc==5:
            print("Adios gracias por usar nuestra calculadora")
            break


        else:
            print("operacion invalida")

calculadora()




        
    


