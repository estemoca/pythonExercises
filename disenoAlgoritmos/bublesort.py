def factorial(n): 
    # Caso Base: Si n es 0 o 1, el resultado es 1    
    if n <= 1:        
        return 1    # Paso Recursivo: Llama a sí misma con entrada más pequeña    else:        return n * factorial(n - 1)# Traza de ejecución:# factorial(3) -> 3 * factorial(2)# -> 3 * (2 * factorial(1))# -> 3 * (2 * 1) -> 6
