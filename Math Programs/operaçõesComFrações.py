def somarFraçãoEMostrar(numerador1, denominador1, numerador2, denominador2):
    novoNumerador = ((denominador1 * numerador2) + (denominador2 * numerador1))
    novoDenominador = denominador1 * denominador2

    return mostrarFração(novoNumerador, novoDenominador)
    
def mostrarFração(numerador, denominador):
    return f"{numerador} / {denominador}"

print("Soma de duas frações")

numerador1 = int(input("Dê o numerador da fração 1 "))
denominador1 = int(input("Dê o denominador da fração 1 "))

print("Esta é sua fração", mostrarFração(numerador1, denominador1))

numerador2 = int(input("Dê o numerador da fração 2 "))
denominador2 = int(input("Dê o denominador da fração 2 "))

print("Esta é sua fração", mostrarFração(numerador2, denominador2))


print(somarFraçãoEMostrar(numerador1, denominador1, numerador2, denominador2))


