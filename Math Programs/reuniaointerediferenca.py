import random
q = []
g = []
a = set([])
b = set([])
    
for i in range(3):  
    random1 = random.randint(0, 10)
    q.append(random1)
    
for i in range(3):  
    random1 = random.randint(0, 10)
    g.append(random1)
    
for i in q:
    a.add(i)
for i in g:
    b.add(i)
    
print("Reunião entre a e b: ", a.union(b))
print("a inter b: ", a.intersection(b))
print("diferença entre a e b:", a.difference(b))

# -- Nicolas Guilherme -- 
# Programa que gera números aleatórios, organiza-os em dois conjuntos e calcula a união, interseção e diferença entre eles. Estou aplicando conhecimentos básicos de matemática para aprimorar minha compreensão sobre requisições em um banco de dados, como ao realizar um INNER JOIN entre duas tabelas.