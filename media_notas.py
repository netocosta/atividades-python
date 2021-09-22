'''
Author: Neto Costa
Description: Usuário informa a quantidade de atividades, as notas e o sistema dá a média
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
print(f'Sua média é: {sum(notas)/len(notas)}')