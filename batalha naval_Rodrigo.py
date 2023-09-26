"""Batalha Naval:"""
def descobrir_navio(tabuleiro, i, j, id_navio, tamanhos_navio, n_linhas, n_colunas):
    if i < 0 or i >= n_linhas or j < 0 or j >= n_colunas:#Caso base, para não passar do tabuleiro
        return False
    if tabuleiro[i][j] != '#':
        return False
    # descobrimos um novo navio
    tabuleiro[i][j] = id_navio
    if id_navio in tamanhos_navio.keys():
        tamanhos_navio[id_navio] += 1
    else:
         tamanhos_navio = 1
    #para cima
    descobrir_navio(tabuleiro, i - 1, j, id_navio, n_linhas, n_colunas, tamanhos_navio)
    #para direita
    descobrir_navio(tabuleiro, i, j + 1, id_navio, n_linhas, n_colunas, tamanhos_navio)
    #para baixo
    descobrir_navio(tabuleiro, i + 1, j, id_navio, n_linhas, n_colunas, tamanhos_navio)
    #para esquerda
    descobrir_navio(tabuleiro, i, j - 1, id_navio, n_linhas, n_colunas, tamanhos_navio)
    return True

#Leitura da entrada
n_linhas, n_colunas = [int(i) for i in input().split()]
tabuleiro = [None] * n_linhas
tamanhos_navio = {} #dicionário
"""dicionário cada elemento de seus dados é identificado por uma chave, não tem ordem, tem como add várias coisas"""
id_navio = 0
for i in range(n_linhas):
	tabuleiro[i] = []
n_tiros = int(input())
for tiro in range(n_tiros):
    i,j = [int(i) for i in input().split()]
    descobriu = descobrir_navio(tabuleiro, i - 1, j - 1, id_navio, n_linhas, n_colunas, tamanhos_navio)
    if descobriu:
        tamanhos_navio[id_navio] -= 1
        id_navio += 1
n_destruidos = 0
for id_, tamanho in tamanhos_navio:
    if tamanho == 0:
        n_destruidos += 1

print(n_destruidos)