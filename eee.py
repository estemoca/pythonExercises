lista=[20.1, 21.3, 22.5, 23.2, 21.8, 20.7, 22.1,  
    19.8, 20.4, 21.2, 22.0, 21.0, 20.3, 21.7,  
    18.7, 19.5, 20.3, 21.1, 20.0, 19.2, 20.8,  
    20.3, 21.0, 22.1, 23.0, 22.2, 21.1, 22.9,  
    19.9, 20.7, 21.6, 22.4, 21.5, 20.9, 22.2,  
    18.9, 19.8, 20.7, 21.5, 20.6, 19.9, 21.3,  
    20.5, 21.6, 22.8, 23.5, 22.7, 21.5, 23.1]   

def nuevafuncion(listaaa):
    nueva_lista=[]
    for i in listaaa:
        potencia = i**2
        nueva_lista.append(potencia)
    return nueva_lista


print(nuevafuncion(lista))