#Algoritmo Escada Perfeita:

# Definindo uma função somarr, para determinar a quantidade de blocos nas colunas
def somar(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

#Definindo as entradas:
quant_colunas = int(input()) #Quantidade de colunas
colunas = [int(i) for i in input().split()] #Quantidade de blocos por coluna encontrados
quant_blocos = somar(colunas) #Chama a função para calcular a soma das colunas
quant_blocos_escada = int((quant_colunas + 1) * quant_colunas / 2) #Fórmula da soma dos n primeiros termos

if ((quant_blocos - quant_blocos_escada) % quant_colunas) != 0:
    print(-1)
else:
    #Para calcular o tamanho da base da escada
    base_escada = int((quant_blocos - quant_blocos_escada) / quant_colunas)
    n_movimentos = 0
    #Loop do movimento das pedras
    for idx, coluna in enumerate(colunas):
        if coluna > (base_escada + idx + 1):
            n_movimentos += coluna - (base_escada + idx + 1)
    print(n_movimentos)