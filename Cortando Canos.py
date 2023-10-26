#Algoritmo Cortando Canos

#Definindo as entradas:
quant_canos, tam_inicial = [int(i) for i in input().split()] #Quantidade  e tamanho de canos solicitados pelo cliente

tam_canos = [] #Armazena o tamanho dos canos
valor_canos = [] #Armazenar os valores do cano

#Laço para entrada do comprimento e valor dos canos
for i in range(quant_canos):
    comp, valor = [int(i) for i in input().split()]
    tam_canos.append(comp)
    valor_canos.append(valor)

n_itens = len(tam_canos) #Tabela da prog dinâmica 

#Caso base
T = [[0 for j in range(tam_inicial + 1)] for i in range(n_itens + 1)]

for j in range(1, tam_inicial + 1): #Começa o range em 1, por causa do caso base
  for i in range(1, n_itens + 1):
    if tam_canos[i-1] > j:
      #Se não coube, volte para o anterior
      T[i][j] = T[i - 1][j] 
    else:
        #Se coube, é preciso tomar uma decisão: tirar e coloca um novo ou ficar com o que tinha
        T[i][j] = max(T[i - 1][j], T[i - 1][j - tam_canos[i - 1]] + valor_canos[i - 1])
print(T[n_itens][tam_inicial])
