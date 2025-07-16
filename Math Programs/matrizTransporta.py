def mostrarMatriz(matriz):
    for i in range(0, len(matriz)):
        print(matriz[i])

def deixarMatrizTransporta(matriz, matrizTransporta):
    for i in range(0, len(matriz)):
        for e in range(0, len(matriz[i])):
            matrizTransporta[i][e] = matriz[e][i]

matriz =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Esta seria a versão transporta = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

matrizTransporta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Matriz ao qual queremos deixar transporta

print("Matriz sem estar transporta: ")
mostrarMatriz(matriz)

deixarMatrizTransporta(matriz, matrizTransporta) # Função para deixar a matriz transporta

print("Matriz após estar transporta: ")
mostrarMatriz(matrizTransporta)

