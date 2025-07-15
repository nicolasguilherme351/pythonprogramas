import math

def calcularVolume(raio, altura, decisao, unidadeDeMedida):

    decisaoAnalisada = False

    area = 0 

    if (decisao == "cilindro"):
 
        area = math.pi * math.pow(raio, 2) * altura
        
        decisaoAnalisada = True

    elif (decisao == "cone"):

        area = 1/3 * math.pi * math.pow(raio, 2) * altura


        decisaoAnalisada = True
    
    elif (decisao == "Esfera"):

        area = 4/3 * math.pi * math.pow(raio, 2)

        decisaoAnalisada = True

    else:
        print("Sua decisão está equivocada. ")
    
    if (decisaoAnalisada == True):
        imprimirArea(area, decisao, unidadeDeMedida)

def imprimirArea(area, decisao, unidadeDeMedida):
    print("A area da", decisao, "é", area, unidadeDeMedida, "cúbicos")

        

