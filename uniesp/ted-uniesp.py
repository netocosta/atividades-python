'''
Author: Walmirino Neto
Package: Uniesp
Date: 2021-09-28
Project: Calculos de médias aritméticas, ponderadas e harmônicas
'''

def calculaMMC(numeros):
    tamanhoLista = len(numeros)
    incremento = 1
    loop = 0
    while loop < tamanhoLista:
        numMaximo = max(numeros) * incremento
        if (all(numMaximo % valor == 0 for valor in numeros)):
            return numMaximo
            break
        incremento += 1
        loop += 1

def medias(notaUm, notaDois, notaTres, tipo):
    if (tipo == 'A' or tipo == 'a'):
        mediaAritmetica = (notaUm + notaDois + notaTres) / 3
        print(f"\n>>> A média aritmética é {mediaAritmetica}")
    elif (tipo == 'P' or tipo =='p'):
        mediaPonderada = ((notaUm*5) + (notaDois*3) + (notaTres*2)) / (5+3+2)
        print(f"\n>>> A média ponderada é {mediaPonderada}")
    elif (tipo == 'H' or tipo =='h'):
        mmc = calculaMMC([notaUm, notaDois, notaTres])
        mmcFracao = ((mmc/notaUm)*1)+((mmc/notaDois)*1)+((mmc/notaTres)*1)
        mediaHarmonica = (3 * mmc) / mmcFracao
        print(f"\n>>> A média harmonica é {mediaHarmonica}")
    else:
        print("O caractere informado é inválido. Use P, p, A, a, H ou h")

while True:
    print("\n--- Calculos de Média ---\n")

    inputUm = float(input("Informe a primeira nota: "))
    inputDois = float(input("Informe a segunda nota: "))
    inputTres = float(input("Informe a terceira nota: "))
    inputTipo = str(input("Informe o tipo de média desejado (A, P ou H): "))

    medias(inputUm, inputDois, inputTres, inputTipo)  

    inputFinal = str(input("\nDeseja fazer um novo calculo? (S ou N): "))
    if (inputFinal == 'N' or inputFinal == 'n'):
        exit()
        
        
'''
Implemente um script python com:
- uma função que recebe três valores numéricos e um carácter por parâmetro.
- se o carácter passado como argumento for 'A' ou 'a', a função retorna o cálculo
  da média aritmética dos valores númericos;
- se o carácter passado como argumento for 'P' ou 'p', a função retorna o cálculo
  da média ponderada (pesos: 5, 3 e 2) dos valores númericos;
- e se o carácter passado como argumento for 'H' ou 'h', a função retorna a média
  harmônica dos valores númericos.
- este script deve interagir com o usuário consultando os três valores e também qual
  tipo de média o usuário deseja calcular.
- este script deve ser interativo, ou seja, ele deve consultar se o usuário deseja
  realizar um novo cálculo ao final de cada execução e, caso a resposta seja afirmativa,
  repetir o processo.
DICAS:
- consulte as fórmulas das médias na internet
- use laço while e if/elif/else na implementação
FORMULAS:
- Media Aritmetica: (nota1 + nota2 + nota3) / total_de_notas = RESULTADO
- Media Ponderada: (nota1*peso1) + (nota2*peso2) + (nota3*peso3) / (peso1 + peso2 + peso3) = RESULTADO
- Media Harmonica: (qtd de elementos) / (1/nota1) + (1/nota2) + (1/nota3) = 
                   (qtd de elementos) / (((mmc / nota1)*1) + ((mmc / nota2)*1) + ((mmc / nota3)*1)) / mmc) = 
                   (qtd de elementos) / (soma / mmc) = 
                   (qtd de elementos) * (inverso: mmc / soma) =
                   (qtd de elementos * mmc) / (1 * soma) = RESULTADO
'''
