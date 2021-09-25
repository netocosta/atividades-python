def calculaMMC(numeros):
    tamanhoLista = len(numeros)
    incremento = 1
    loop = 0
    while loop < tamanhoLista:
        numMaximo = max(numeros) * incremento
        if (all(numMaximo % valor == 0 for valor in numeros)):
            return numMaximo
        incremento += 1
        loop += 1


print(calculaMMC([4, 6, 8]))
