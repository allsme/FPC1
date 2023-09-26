#Algoritmo Olimpiadas:

# Função de comparação para ordenar os países
def comparar_paises(pais1, pais2):
    # Ordenar por número de medalhas de ouro em ordem decrescente
    if pais1[0] != pais2[0]:
        return pais2[0] - pais1[0]
    
    # Ordenar por número de medalhas de prata em ordem decrescente
    if pais1[1] != pais2[1]:
        return pais2[1] - pais1[1]
    
    # Ordenar por número de medalhas de bronze em ordem decrescente
    if pais1[2] != pais2[2]:
        return pais2[2] - pais1[2]
    
    # Ordenar por número de identificação em ordem crescente
    return pais1[3] - pais2[3]

# Função para realizar o algoritmo counting sort
def cont_sort(arr):
    valr_max = max(arr, key=lambda x: x[0])[0]
    count = [0] * (valr_max + 1)
    saida = [0] * len(arr)

    # Conta a ocorrência de cada valor
    for i in range(len(arr)):
        count[arr[i][0]] += 1

    # Calcula a posição final de cada valor no saida
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Coloca os elementos na posição correta no saida
    for i in range(len(arr) - 1, -1, -1):
        saida[count[arr[i][0]] - 1] = arr[i]
        count[arr[i][0]] -= 1

    return saida

# Leitura da entrada
n_pais, m_modalidade = map(int, input().split())

paises = []
for _ in range(m_modalidade):
    ouro, prata, bronze = map(int, input().split())
    paises.append((ouro, prata, bronze, _ + 1))  # Adiciona o número de identificação do país

# Ordena a lista de países utilizando o counting sort com a função de comparação
paises_ordenados = cont_sort(paises)

# Imprime os países na ordem decrescente de classificação
for pais in paises_ordenados:
    print(pais[3], end=' ')