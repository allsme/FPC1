import time
import matplotlib.pyplot as plt

#Definindo da função permutar
def permutar(pontos_de_entrega):
    #Caso base:
    if len(pontos_de_entrega) <= 1:
        return [pontos_de_entrega]

    #Lista vazia para adicionar os pontos que faltam
    permutacoes = []

    #Recursiva para salvar os pontos que já passou
    for i, ponto_atual in enumerate(pontos_de_entrega):
        pontos_restantes = pontos_de_entrega[:i] + pontos_de_entrega[i+1:]
        for permutacao in permutar(pontos_restantes):
            permutacoes.append([ponto_atual] + permutacao)
    return permutacoes

#Definindo a função distância de dois pontos
def distancia(p1,p2):
    dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    return dist

#Função para a distância total
def dist_percurso(percurso):
    d = 0
    for i in range(1,len(percurso)):
        d += distancia(percurso[i-1],percurso[i])
    return d

#Entradas dos valores
num_entradas = int(input("Digite o número de entradas: "))
entradas = ['R'] + list('ABCDEFGHIJKLMNOPQSTUVWXYZ')[:num_entradas-1]
p = []
for entrada in entradas:
    entrada_coordenadas = input(f"Digite as coordenadas para a entrada {entrada} no formato x,y: ")
    coordenadas = entrada_coordenadas.split(",")
    x = int(coordenadas[0])
    y = int(coordenadas[1])
    p.append((x, y))

#Lista para armazenar os tempos de execução dos pontos
lista_tempos = []

#Laço para saber os tempos de execução
for i in range(1, num_entradas+1):
    tic = time.process_time_ns()
    menor = float("inf")
    menores_percursos = []
    for j in permutar(p[1:i]):
        j = [p[0]] + j + [p[0]]
        dist = dist_percurso(j)
        if dist < menor:
            menor = dist
            menores_percursos = [j]
        elif dist == menor:
            menores_percursos.append(j)
    toc = time.process_time_ns()
    lista_tempos.append(toc - tic)

# Criação do dicionário para mapear as coordenadas para as entradas
coordenadas_para_entradas = {}
for i in range(len(entradas)):
    entrada = entradas[i]
    coordenada = p[i]
    coordenadas_para_entradas[coordenada] = entrada

# Imprime apenas as menores rotas para o número total de entradas escolhido pelo usuário
for percurso in menores_percursos:
    # Alteração para exibir os entradas em vez das coordenadas usando o dicionário
    percurso_entradas = [coordenadas_para_entradas[coordenada] for coordenada in percurso]
    print(f"Um dos menores percursos para {num_entradas} entradas foi {percurso_entradas} com a distancia de {menor} dronômetros")

#Criação do gráfico para comparar os tempos de execução
plt.plot(range(1, num_entradas+1), lista_tempos)
plt.xlabel('Número de entradas')
plt.ylabel('Tempo de processamento (ns)')
plt.show()