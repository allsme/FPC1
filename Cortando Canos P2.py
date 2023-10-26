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

#Caso Base
T = [[0 for j in range(tam_inicial + 1)] for i in range(n_itens + 1)]

for j in range(1, tam_inicial + 1): #Começa o range em 1, por causa do caso base
    for i in range(1, n_itens + 1):
        T[i][j] = T[i - 1][j] #Operação sem o cano atual 
        #Contador
        repet = 1
        while repet * tam_canos[i - 1] <= j:
            T[i][j] = max(T[i][j], T[i - 1][j - repet * tam_canos[i - 1]] + repet * valor_canos[i - 1])
            repet += 1
        
print(T[n_itens][tam_inicial])