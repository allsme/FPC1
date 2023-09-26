# Algoritmo do Lobo Mau:

matriz = []  # Lista para armazenamento da matriz
ovelhas = 0
lobos = 0
id_animais = 0

# Definindo a função para a inserção da matriz
def inicio():
    #Definição da matriz, ou inicio
    # do problema
    linhas, colunas = map(int, input())
    for i in range(linhas):
        linha = list(input())
        matriz.append(linha)
        
        
    cont_ovelhas, cont_lobos = confronto_animais()
    print(cont_ovelhas, cont_lobos)

#Verificar o confronto entre ovelhas e lobos
def confronto_animais(ovelhas, lobos):
     #Se tiver mais ovelhas do que lobos, as ovelhas matam os lobos
    if ovelhas > lobos:
        lobos = 0
    #Se tiver mais lobos que ovelhas, os lobos matam as ovelhas
    elif lobos > ovelhas:
        ovelhas = 0
    #Se tiver a mesma quantidade para os dois, as ovelhas morrem
    else:
        lobos = ovelhas
        return lobos

# Definindo a função para verificar se existe lobo ou ovelha na posição:
def encontrar_animais(matriz, i, j, id_animais, tamanhos_animais, linhas, colunas):
    if i < 0 or i >= linhas or j < 0 or j >= colunas:#Caso base, para não passar do matriz
        return False
    if matriz[i][j] == 'v':
        ovelhas += 1
    elif matriz[i][j] == 'k':
        lobos += 1
        
    # descobrimos um novo navio
    matriz[i][j] = id_animais
    if id_animais in tamanhos_animais.keys():
        tamanhos_animais[id_animais] += 1
    else:
         tamanhos_animais = 1
    #para cima
    encontrar_animais(matriz, i - 1, j, id_animais, tamanhos_animais, linhas, colunas)
    #para direita
    encontrar_animais(matriz, i, j + 1, id_animais, tamanhos_animais, linhas, colunas)
    #para baixo
    encontrar_animais(matriz, i + 1, j, id_animais, tamanhos_animais, linhas, colunas)
    #para esquerda
    encontrar_animais(matriz, i, j - 1, id_animais, tamanhos_animais, linhas, colunas)
    return True


# Chamando a função principal
inicio()