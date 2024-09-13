contaGry =0
contaHal =0
contaRev =0
contaSly =0
questions = ["\n¿Como te definirias?:\n1.Valiente\n2.Leal\n3.Sabio\n4.Ambisioso\nRespuesta:", 
                "\n¿Cual es tu clase favorita?:\n1.Vuelo\n2.Pociones\n3.Defensa contra las artes oscuras\n4.Animales fantasticos\nRespuesta:", 
                "\n¿Donde pasarias mas tiempo ?:\n1.Invernadero\n2.Biblioteca\n3.En la sala común\n4.Explorando\nRespuesta:", 
                "\n¿Cual es tu color favorito?:\n1.Rojo\n2.Azul\n3.Verde\n4.Amarillo\nRespuesta:", 
                "\n¿Cual es tu mascota?\n1.Sapo\n2.Lechuza\n3.Gato\n4.Serpiente\nRespuesta:"]

def contador(casa):
    if(casa=="g"):
        global contaGry
        contaGry+=1
    elif (casa=="h"):
        global contaHal
        contaHal+=1
    elif (casa=="r"):
        global contaRev
        contaRev+=1
    else :
        global contaSly
        contaSly+=1

def evalQuestion(response,nPregunta):
    if(nPregunta ==0):
        if(response == 1): 
            contador("g")
        elif(response == 2):
            contador("h")
        elif(response == 3):
            contador("r")
        elif(response == 4):
            contador("s")        
    elif(nPregunta ==1 or nPregunta ==3):
        if(response == 1): 
            contador("g")
        elif(response == 2):
            contador("r")
        elif(response == 3):
            contador("s")
        elif(response == 4):
            contador("h")        
    elif(nPregunta ==2):
        if(response == 1): 
            contador("h")
        elif(response == 2):
            contador("r")
        elif(response == 3):
            contador("s")
        elif(response == 4):
            contador("g")        
    elif(nPregunta ==4):
        if(response == 1): 
            contador("r")
        elif(response == 2):
            contador("g")
        elif(response == 3):
            contador("h")
        elif(response == 4):
            contador("s")        
    else:
        print("respuesta invalida no sera contada")

def showQuestion (nPregunta):     
    print(questions[nPregunta])   
    response =int(input())
    evalQuestion(response,nPregunta)    
    return questions[nPregunta]

def evaluarCasa():   
    max_valor = max(contaGry, contaHal, contaRev, contaSly)    
    iguales = ((contaGry == contaHal and contaGry !=0 and contaHal!=0) or (contaGry == contaRev and contaGry !=0 and contaRev!=0) or (contaGry == contaSly and contaGry !=0 and contaSly!=0) or(contaHal == contaRev and contaHal !=0 and contaRev!=0) or (contaHal == contaSly and contaHal !=0 and contaSly!=0) or (contaRev == contaSly and contaRev !=0 and contaSly!=0))
    casa=''
    print(contaGry, contaHal, contaRev, contaSly)
    print(iguales)
    if iguales and max_valor:
        casa =input("Jummm, es muy dificil te dare la posibilidad de escojer tu casa, ¿Cual te gustaria?")        
        return "Ok , Bienvenido a " + casa
    else:            
        max_valor = max(contaGry, contaHal, contaRev, contaSly)
        if max_valor == contaGry:
           casa= "Gryffindor"
        elif max_valor == contaHal:
            casa= "Hufflepuff"
        elif max_valor == contaRev:
            casa= "Ravenclaw"
        else:
            casa= "Slytherin"            
        return "Jummm, creo que te pondre en "+ casa

def main():
    print("🎩:¡Bienvenido al programa del Sombrero Seleccionador de Hogwarts! Para determinar en qué casa de Hogwarts pertenecerás, te haré algunas preguntas.")

    for i in range(len(questions)):
        print(showQuestion(i))
    print(evaluarCasa())
        

main()
