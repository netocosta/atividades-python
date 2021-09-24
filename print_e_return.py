# funcao retornando valor
def somar_numeros(numeroUm, numeroDois):
    return numeroUm+numeroDois

# assim nao vai imprimir nada, porque não tem nenhum print
# mas a funcao está funcionando
somar_numeros(1, 2)

# assim eu vou colocar o retorno da funcao, para a variavel resultado
# agora minha variavel tem o resultado da soma de 1 + 2
resultado = somar_numeros(1, 2)

# se eu quiser imprimir na tela, eu tenho que usar o print()
print("Retorno da funcao: ", somar_numeros(1, 2))
print("Variavel resultado: ", resultado)
