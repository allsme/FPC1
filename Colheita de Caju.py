# Definindo as entradas:
linhas, colunas, area_linha, area_coluna = map(int, input().split())

# Definindo a matriz
mapa = []
for i in range(linhas):
    linha = list(map(int, input().split()))
    mapa.append(linha)

#Calculo das soma acumuladas
soma = [[0] * (colunas + 1) for _ in range(linhas+1)]
for i in range(1, linhas + 1):
    for j in range(1, colunas + 1):
        soma[i][j] = soma[i-1][j] + soma[i][j-1] - soma[i-1][j-1] + mapa[i-1][j-1]

#Calculo da soma da submatriz
def cal_submatriz(canto_sup_esq, canto_inf_dir):
    i1, j1 = canto_sup_esq
    i2, j2 = canto_inf_dir
    return soma[i2][j2] - soma[i1][j2] - soma[i2][j1] + soma[i1][j1]

melhor_resultado = 0 #Variavel para armazenar o melhor resultado
for i in range(linhas - area_linha + 1):
    for j in range(colunas - area_coluna + 1):
        canto_sup_esq = (i,j)
        canto_inf_dir = (i + area_linha, j + area_coluna)
        soma_submatriz = cal_submatriz(canto_sup_esq, canto_inf_dir)
        melhor_resultado = max(melhor_resultado, soma_submatriz)

print(melhor_resultado)