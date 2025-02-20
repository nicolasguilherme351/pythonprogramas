print("banana é  lega")

print()
listanumeros = []
numeros = int(input("Digite a quantidade de numeros: "))
nome = input("Digite o nome do seu arquivo: ")
soma = 0

for i in range(numeros):
    print("Fale o numero ", i+1)
    numero = int(input(""))
    listanumeros.append(numero)

with open(f"{nome}.txt", "w") as arquivo:
    for i in listanumeros:
        arquivo.write(f"{i} " + '\n')


# Ler e fazer a soma do arquivo
try:
    with open(f"{nome}.txt", "r") as arquivo:
        arq = open (f"{nome}.txt")
        for i in arq:
            soma += int(i)
        conteudo = arquivo.read()
        print("Numeros do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado")

print("Soma total: ", soma)

print("Arquivo escrito, nome do arquivo: " + f"{nome}.txt")
