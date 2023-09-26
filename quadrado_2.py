#Quadrado Quase Mágico:

#Definir a matriz:
dimensao = int(input())
matriz = [None] * dimensao
for linha in range(dimensao):
    nova_linha = [int(i) for i in input().split()]
    matriz[linha] = nova_linha

#Definindo as funções para somar as linhas e colunas:
def soma_linha(matriz, linha):
    soma = 0
    for elemento in matriz[linha]:
        soma += elemento
    return soma

def soma_coluna(matriz, coluna):
    soma = 0
    for linha in matriz:
        soma += linha[coluna]
    return soma

#Para percorrer a matriz e encontrar o número que foi alterado:

linha_dif = -1 #Para já iniciar a contagem do índice 0
col_dif = -1

for linha in range(dimensao):
    if soma_linha(matriz, linha) != soma_linha(matriz, 0):
        linha_dif = linha
        break

for coluna in range(dimensao):
    if soma_coluna(matriz, coluna) != soma_coluna(matriz, 0):
        col_dif = coluna
        break


num_alterado = matriz[linha_dif][col_dif]
num_original = num_alterado - (soma_linha(matriz, linha_dif) - soma_coluna(matriz, 0))

print(num_original, num_alterado)