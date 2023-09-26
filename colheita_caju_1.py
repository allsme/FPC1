#Algoritmo Colheita de Cajús

# Definindo as entradas:
linhas, colunas, area_linha, area_coluna = map(int, input().split())

# Definindo a matriz
mapa = []
for i in range(linhas):
    linha = list(map(int, input().split()))
    mapa.append(linha)

#Definindo uma função para calcular as somas dos elementos da matriz
def soma_matriz(area_linha, area_coluna, mapa):
    matriz_soma = []
    for i in range(len(mapa) - area_linha + 1):
        linha_soma = []
        for j in range(len(mapa[0])):
            soma = 0
            for m in range(i, i + area_linha):
                soma += mapa[m][j]
            linha_soma.append(soma)
        matriz_soma.append(linha_soma)
    return matriz_soma

def busca(matriz):
    melhor_valor = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > melhor_valor:
                melhor_valor = matriz[i][j]
    return melhor_valor

resultado_atual = soma_matriz(area_linha, area_coluna, mapa)
melhor_resultado = busca(resultado_atual)

print(melhor_resultado)