#Algortimo Cortando Canos - parte 2

#Definindo as entradas, da quantidade e tamanho dos canos
quant_canos, tam_inicial = [int(i) for i in input().split()]

#Armazenando numa lista os tamanhos e valores dos canos
tam_canos = []
valor_canos = []

#Laço para entrada do comprimento e valor dos canos
for i in range(quant_canos):
    comp, valor = [int(i) for i in input().split()]
    tam_canos.append(comp)
    valor_canos.append(valor)

n_itens = len(tam_canos) #Tabela da programação dinâmica

#Caso Base:
T = [[0 for j in range(tam_inicial + 1)] for i in range(n_itens + 1)]

#Chamada recursiva do código:
for j in range(1, tam_inicial + 1):
    for i in range(1, n_itens + 1):
        repet = 0 #Contador para calcular as repetições
     #Se coube, é preciso tomar uma decisão: tadicionar um a mais ou não
    if tam_canos[i-1] > j:
        T[i][j] = T[i - 1][j]
    else:
        T[i][j] == max(T[i - 1][j], T[i - 1][j - tam_canos[i - 1]] + valor_canos[i - 1])
        repet += 1

print(T[n_itens][tam_inicial])