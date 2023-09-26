# Definindo as entradas: quantidade de canos e tamanho inicial
quant_canos, tam_inicial = map(int, input().split())

# Armazenando os tamanhos e valores dos canos em listas separadas
tam_canos = []
valor_canos = []

# Lendo os comprimentos e valores dos canos
for i in range(quant_canos):
    comp, valor = map(int, input().split())
    tam_canos.append(comp)
    valor_canos.append(valor)

# Tabela da programação dinâmica
T = [0] * (tam_inicial + 1)

# Preenchendo a tabela de programação dinâmica
for j in range(1, tam_inicial + 1):
    max_value = T[j - 1]  # Valor sem adicionar cano de tamanho j
    for i in range(quant_canos):
        if tam_canos[i] <= j:
            max_value = max(max_value, T[j - tam_canos[i]] + valor_canos[i])
    T[j] = max_value

print(T[tam_inicial])
