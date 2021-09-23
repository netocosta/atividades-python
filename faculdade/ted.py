'''
Implemente um script phyton com:
OK - uma função que recebe três valores numéricos e um carácter por parâmetro.
OK - se o carácter passado como argumento for 'A' ou 'a', a função retorna o cálculo
  da média aritmética dos valores númericos;
OK - se o carácter passado como argumento for 'P' ou 'p', a função retorna o cálculo
  da média ponderada (pesos: 5, 3 e 2) dos valores númericos;
OK - e se o carácter passado como argumento for 'H' ou 'h', a função retorna a média
  harmônica dos valores númericos.
- este script deve interagir com o usuário consultando os três valores e também qual
  tipo de média o usuário deseja calcular.
- este script deve ser interativo, ou seja, ele deve consultar se o usuário deseja
  realizar um novo cálculo ao final de cada execução e, caso a resposta seja afirmativa,
  repetir o processo.

DICAS:
- consulte as fórmulas das médias na internet
- use laço while e if/elif/else na implementação
'''

print("\n--- Calculos de Média ---\n")

def mmc(lista):
    x = 1
    while True:
        calc = max(lista) * x
        if all((calc % num) == 0 for num in lista):
            return calc
        x += 1
        
def medias(notaUm, notaDois, notaTres, tipo):
    # media_aritmetica
    if (tipo == 'A' or tipo == 'a'):
        # formula: (nota1 + nota2 + nota3) / total_de_notas
        calculo = (notaUm + notaDois + notaTres) / 3
        print(f"\nA média aritmética é {calculo}")
    # media_ponderada
    elif (tipo == 'P' or tipo =='p'):
        # formula: (nota1*peso1) + (nota2*peso2) + (nota3*peso3) / (peso1 + peso2 + peso3)
        pesoUm = 5
        pesoDois = 3
        pesoTres = 2
        calculo = ((notaUm*pesoUm) + (notaDois*pesoDois) + (notaTres*pesoTres)) / (pesoUm+pesoDois+pesoTres)
        print(f"\nA média ponderada é {calculo}")
    # media_harmonica
    elif (tipo == 'H' or tipo =='h'):
        # formula: (qtd de elementos) / (1/nota1) + (1/nota2) + (1/nota3) [OBS: soma de fracoes, tirar mmc]
        parte1 = 3
        parte2 = notaUm+notaDois+notaTres
        parte3 = mmc([notaUm, notaDois, notaTres])
        parte4 = parte1 * parte3
        parte5 = parte1 = parte2
        calc = parte4 / parte5 #corrigir
        print(calc)
    else:
        print("O caractere informado é inválido. Use P, p, A, a, H ou h")

inputUm = float(input("Informe a primeira nota: "))
inputDois = float(input("Informe a segunda nota: "))
inputTres = float(input("Informe a terceira nota: "))
inputTipo = str(input("Informe o tipo de média desejado (A, P ou H): "))

medias(inputUm, inputDois, inputTres, inputTipo)
