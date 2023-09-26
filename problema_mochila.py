"""problema da Mochila 
p = [4,2,1,3] #Pesos da mochila
v = [500, 400, 300, 450] #Valores dos objetos
n_itens = len(p) #Tabela da prog dinâmica 
capacidade = 5
T = [[0 for j in range(capacidade + 1)] for i in range(n_itens + 1)] #Caso base
for j in range(1, capacidade + 1): #Começa o range em 1 por causa do caso base
  for i in range(1, n_itens + 1):
    if p[i-1] > j:
      #não coube, volta para o anterior
      T[i][j] = T[i - 1][j] 
    else:
        #cabe e precisa tomar uma decisão
        #tira para colocar o novo ou fica com o que tinha
        T[i][j] = max(T[i - 1][j], T[i - 1][j - p[i - 1]] + v[i - 1])
print(T[n_itens][capacidade])"""

def max_value_knapsack_with_repetitions(n, t, canos):
    dp = [0] * (t + 1)
    
    for i in range(1, t + 1):
        for j in range(n):
            if canos[j][0] <= i:
                dp[i] = max(dp[i], dp[i - canos[j][0]] + canos[j][1])
    
    return dp[t]

# Leitura das entradas
n, t = map(int, input().split())
canos = []
for _ in range(n):
    c, v = map(int, input().split())
    canos.append((c, v))

# Chama a função e imprime o resultado
max_value = max_value_knapsack_with_repetitions(n, t, canos)
print(max_value)
