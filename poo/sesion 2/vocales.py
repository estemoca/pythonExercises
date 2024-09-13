def vocal_mas_comun(texto):    
    vocales = "aeiou"    
    conteo_vocales = {vocal: 0 for vocal in vocales}
        
    for char in texto.lower():
        if char in vocales:
            conteo_vocales[char] += 1
        
    vocal_comun = max(conteo_vocales, key=conteo_vocales.get)
        
    if conteo_vocales[vocal_comun] == 0:
        return ''
    
    return vocal_comun

texto = "Hola, ¿cómo estás?"
print(vocal_mas_comun(texto))