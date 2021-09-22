'''
Author: Neto Costa
Description: Aplicação para somar as notas de uma ou mais atividades
'''

# criação da lista vazia
notas = []
# capturando a quantidade de avaliacoes
avaliacoes = int(input('Quantas avaliações são? '))
# valor inicial do loop
x = 1

# inicio do loop
while x <= avaliacoes:
    # capturando o valor da nota
    valor = float(input(f'Qual a nota da avaliação {x}? '))
    # incluindo a nota na lista
    notas.append(valor)
    # incrementando o valor do loop
    x += 1

# mostra na tela a soma das notas que estão na lista
print(f'Sua nota é: {sum(notas)}')