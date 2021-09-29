# -*- coding: UTF-8 -*-
'''
Author: Neto Costa
Description: Sistema faz as perguntas e o usuário responde com uma letra
'''

import random
import configparser

config = configparser.ConfigParser()
config.read('data.ini')
perguntas = config['perguntas']
respostas = config['respostas']
correta = config['correta']

opcoes = ['a', 'b', 'c', 'd', 'e']

acertos = 0
erros = 0

while True:
    sorteado = random.randint(0,len(perguntas)-1)

    questao = perguntas[f'p{sorteado}']
    print(f'Questão: {questao}')

    alternativas = {
        'a': respostas[f'p{sorteado}1'],
        'b': respostas[f'p{sorteado}2'],
        'c': respostas[f'p{sorteado}3'],
        'd': respostas[f'p{sorteado}4'],
        'e': respostas[f'p{sorteado}5'],
    }

    for x in alternativas.keys():
        print(f'{x}) {alternativas[x]}')

    resposta = str(input('Qual a alternativa correta? '))

    if (resposta not in opcoes):
        print('Opção incorreta. Escolha a, b, c, d ou e.')
        resposta = str(input('Qual a alternativa correta? '))
    else:
        respostaValor = alternativas[resposta]

        if respostaValor == correta[f'p{sorteado}']:
            print("\n>>> ACERTOOOOU!!!")
            acertos += 1
        else:
            print("\n>>> ERROOOOUUU!!!")
            erros += 1
        
        inputFinal = str(input("\nDeseja uma nova pergunta? (S ou N): "))
        if (inputFinal == 'N' or inputFinal == 'n'):
            print(f'\nVocê acertou {acertos} questões e errou {erros}.')
            break