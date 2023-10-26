#Algoritmo Contagem de Pares de Botas

pares = 0 #Contador de pares de botas
dicio_tamanhos = {} #Dicionário dos tamanhos das botas

#Definindo as entradas
n_botas = int(input())
if n_botas <= 0 or n_botas >= 10000:
    ValueError

for _ in range(n_botas):
    tam_bota, lado_bota = input().split()
    tam_bota = int(tam_bota)

    #Condicional para verificar se o tamanho da bota é válido
    if tam_bota < 30 or tam_bota > 61:
        ValueError
    
    #Condicional para verificar o pé da bota
    if tam_bota not in dicio_tamanhos:
        dicio_tamanhos[tam_bota] = {'D': 0, 'E': 0}
    dicio_tamanhos[tam_bota][lado_bota] += 1

#Contando os pares de botas
for tam_bota, lado_bota in dicio_tamanhos.items():
    pares += min(dicio_tamanhos[tam_bota]['D'], dicio_tamanhos[tam_bota]['E'])

print(pares)