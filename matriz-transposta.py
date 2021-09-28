'''
Transpor as colunas de uma matriz para linhas.
'''

matrizA = [
    [2, 3, 5],
    [4, 5, 6],
    [6, 7, 8],
    [8, 9, 8]
    ]

matrizTransposta = []
colunas = range(3)

for i in colunas:
    matrizTemporaria = []
    for linha in matrizA:
        matrizTemporaria.append(linha[i])
    matrizTransposta.append(matrizTemporaria)

print(matrizTransposta)
