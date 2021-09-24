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

def calcMMC(lista):
    x = 1
    while True:
        calc = max(lista) * x
        if all((calc % num) == 0 for num in lista):
            return calc
        x += 1

def mediaAritmetica(um, dois, tres, qtd):
    return (um + dois + tres) / qtd

def mediaPonderada(um, dois, tres, pesoUm, pesoDois, pesoTres):
    return ((um*pesoUm) + (dois*pesoDois) + (tres*pesoTres)) / (pesoUm+pesoDois+pesoTres)

def mediaHarmonica(um, dois, tres, qtd):
    mmc = calcMMC([um, dois, tres])
    mmcFracao = ((mmc/um)*1)+((mmc/dois)*1)+((mmc/tres)*1)
    return (qtd * mmc) / mmcFracao

def medias(notaUm, notaDois, notaTres, tipo):
    if (tipo == 'A' or tipo == 'a'):
        print(f"\n>>> A média aritmética é {mediaAritmetica(notaUm, notaDois, notaTres, 3)}")
    elif (tipo == 'P' or tipo =='p'):
        print(f"\n>>> A média ponderada é {mediaPonderada(notaUm, notaDois, notaTres, 5, 3, 2)}")
    elif (tipo == 'H' or tipo =='h'):
        print(f"\n>>> A média harmonica é {mediaHarmonica(notaUm, notaDois, notaTres, 3)}")
    else:
        print("O caractere informado é inválido. Use P, p, A, a, H ou h")

def calcula():
    print("\n--- Calculos de Média ---\n")

    inputUm = float(input("Informe a primeira nota: "))
    inputDois = float(input("Informe a segunda nota: "))
    inputTres = float(input("Informe a terceira nota: "))
    inputTipo = str(input("Informe o tipo de média desejado (A, P ou H): "))

    medias(inputUm, inputDois, inputTres, inputTipo)  

while True:
    calcula()
    inputFinal = str(input("\nDeseja fazer um novo calculo? (S ou N): "))
    if (inputFinal == 'N' or inputFinal == 'n'):
        exit()
