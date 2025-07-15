import funções

print("Programa ao qual calcula a area das formas")

unidadeDeMedida = input("qual seria a unidade de medida? metros ou centímetros? ")
raio = int(input("Qual seria o raio? "))
altura = int(input("Qual seria a altura? "))
decisao = input("Qual seria o volume do objeto que quer calcular? Temos cilindro, cone, esfera. ")


funções.calcularVolume(raio, altura, decisao, unidadeDeMedida)
