import random

cartasValor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cartasSimbolo = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"]
cartasJogador1 = []

# Sortea a manilha
o = random.randint(1, 10)
manilha = cartasSimbolo[o-1]
manilhaValor = 11
    
for i in range(3):
    o = random.randint(1, 10)
    cartasJogador1.append(cartasSimbolo[o-1])
    
print(cartasJogador1)
print(manilha)