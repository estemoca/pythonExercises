def calcular_IMC(peso:float, altura:float)->float:    
    imc = peso / ((altura) ** 2)
    return imc        
    # return round(imc, 2)

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):    
    imc = peso / (altura ** 2)        
    porcentaje_grasa = 1.20 * imc + 0.23 * edad - 5.4 - valor_genero    
    return round(porcentaje_grasa, 2)

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):    
    tmb = 10 * peso + 6.25 * altura * 100 - 5 * edad + valor_genero    
    return tmb

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):    
    tmb_actividad = calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad    
    return tmb_actividad

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):        
    tmb = 10 * peso + 6.25 * altura * 100 - 5 * edad + valor_genero        
    rango_inferior = tmb * 0.8
    rango_superior = tmb * 0.9        
    resultado = f"Para adelgazar es recomendado que consumas entre: {int(rango_inferior)} y {int(rango_superior)} calorías al día."    
    return resultado

