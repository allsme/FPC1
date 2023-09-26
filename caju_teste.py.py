#Algoritmo teste otimização da colheita de cajus

# Definindo as entradas:
linhas, colunas, area_linha, area_coluna = map(int, input().split())

# Definindo a matriz
mapa = []
for i in range(linhas):
    linha = list(map(int, input().split()))
    mapa.append(linha)

# Pré-cálculo das somas acumuladas
soma_acumulada = [[0] * (colunas + 1) for _ in range(linhas + 1)]
for i in range(1, linhas + 1):
    for j in range(1, colunas + 1):
        soma_acumulada[i][j] = soma_acumulada[i-1][j] + soma_acumulada[i][j-1] - soma_acumulada[i-1][j-1] + mapa[i-1][j-1]

def calcular_soma_submatriz(canto_sup_esq, canto_inf_dir):
    i1, j1 = canto_sup_esq
    i2, j2 = canto_inf_dir
    return soma_acumulada[i2][j2] - soma_acumulada[i1][j2] - soma_acumulada[i2][j1] + soma_acumulada[i1][j1]

melhor_resultado = 0
for i in range(linhas - area_linha + 1):
    for j in range(colunas - area_coluna + 1):
        canto_sup_esq = (i, j)
        canto_inf_dir = (i + area_linha, j + area_coluna)
        soma_submatriz = calcular_soma_submatriz(canto_sup_esq, canto_inf_dir)
        melhor_resultado = max(melhor_resultado, soma_submatriz)

print(melhor_resultado)
