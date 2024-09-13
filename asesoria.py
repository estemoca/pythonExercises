saldo = 1000000
clave = 123456
cuentaDestinoSaldo = 0
noCuentaDestino= 5555

def retiro():
    retiro = float(input("ingrese el monto a retirar "))
    global saldo      
    if saldo>=retiro:  
        saldo = saldo - retiro
        print(f"Retiro Exitoso su nuevo saldo es : {saldo}")        
    else:
        print("No tiene suficiente fondo para este retiro")                         
    return True

def consignacion():
    consignar = float(input("ingrese el monto a consignar "))
    global saldo  
    if consignar>=0:  
        saldo = saldo + consignar
        print(f"consignacion Exitosa su nuevo saldo es : {saldo}")        
    else:
        print("valor erroneo de consignacion")                         
    return True

def transferencia():
    noCuenta = int(input("solicitar cuenta destino"))    
    if noCuenta==5555:
        valorTran = float(input("ingrese el monto a transferir"))
        global cuentaDestinoSaldo        
        global saldo
        if saldo>=valorTran: 
            saldo-=valorTran
            cuentaDestinoSaldo+=valorTran         
            print("Transferencia exitosa")      
            print(f"El nuevo saldo de la cuenta destino es {cuentaDestinoSaldo}")      
            print(f"El nuevo saldo de la cuenta origen es {saldo}")  
        else:
            print(f"Su saldo es : {saldo}")  
            print("no se puede realizar la transferencia porque no hay suficiente dinero")    
    else:
        print("transferencia invalida cuenta no existe")
    print("transferencia")

def consultaSaldo():
    global saldo
    print(f"su saldo es {saldo}")
    return True

def login():
    global clave
    contra = int(input("Ingrese la contraseña"))
    if clave == contra:
        return True
    else:
        return False
    
# retiro - consignacion - transferencia -consulta saldo 
def cajero():    
    if login():
        while True:
            print("bienvenidos al cajero bancolombia")
            opcion =int(input("1 retiro \n 2 consignacion \n 3 transferencia\n 4 consulta saldo \n 5 salir"))
            if opcion==1:  
                retiro()          
            elif opcion==2:
                consignacion()
            elif opcion==3:
                transferencia()
            elif opcion==4:
                consultaSaldo()
            elif opcion==5:
                print("muchas gracias por usarnos ")
                break
            else:
                print("opcion invalida")
    else:
        print("Clave invalida")

cajero()