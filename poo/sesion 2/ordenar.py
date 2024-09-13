def ordenarL(numeros, tipo):
    n = len(numeros)    
    for i in range(n):        
        indexE = i        
        for j in range(i + 1, n):
            if tipo == "Asc":
                if numeros[j] < numeros[indexE]:
                    indexE = j
            elif tipo == "Desc":
                if numeros[j] > numeros[indexE]:
                    indexE = j                
        numeros[i], numeros[indexE] = numeros[indexE], numeros[i]    
    return numeros

numeros = [2, 4, 6, 8, 9]
print(ordenarL(numeros, "Asc"))
print(ordenarL(numeros, "Desc"))