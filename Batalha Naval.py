#Batalha Naval

matriz = [] #Lista para armazenamento da matriz
navios = [] #Lista para armazenamento dos navios
navios_encontrados = 0 #Contador dos navios encontrados

#Definindo a função para a inserção da matriz
def inicio_partida():
    linhas, colunas = map(int, input().split())
    for i in range(linhas):
        linha = list(input())
        matriz.append(linha)

    detectar_navios()
    num_disparos = int(input())
    for _ in range(num_disparos):
        x_linha, y_coluna = map(int, input().split())
        navios_destruidos(x_linha - 1, y_coluna - 1)

    cont_destruidos = navios.count(0)
    print(cont_destruidos)

#Definindo a função para verificar se existe navio na posição
def navios_destruidos(linhas, colunas):
    alvo = matriz[linhas][colunas]
    if alvo != ".":
        navios[alvo] -= 1

#Definindo a função para detectar os navios:
def detectar_navios():
    navios_encontrados = 0
    for n in range(len(matriz)):
        for m in range(len(matriz[0])):
            if matriz[n][m] == "#":
                navios.append(0)
                tamanho(n, m, navios_encontrados)
                navios_encontrados += 1

#Definindo a função para calcular o tamanho do navio:
def tamanho(linha, coluna, navios_id):
    if matriz[linha][coluna]  == '#':
        matriz[linha][coluna]  = navios_id
        navios[navios_id] += 1

        if linha - 1 >= 0:
            tamanho(linha - 1, coluna, navios_id)
        if coluna - 1 >= 0:
            tamanho(linha, coluna - 1, navios_id)
        if linha + 1 < len(matriz):
            tamanho(linha + 1, coluna,  navios_id)
        if coluna + 1 < len(matriz[0]):
            tamanho(linha, coluna + 1, navios_id)
        
#Chamando a função principal
inicio_partida()