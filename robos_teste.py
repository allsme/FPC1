#Algoritmo Robos teste

movs = {'N': ['O', 'L'], 'L': ['N', 'S'], 'S': ['L', 'O'], 'O': ['S', 'N']}

def movimentacoes(pos_linha, pos_coluna, orientacao):
    movimentos = {'N': (-1, 0), 'L': (0, 1), 'S': (1, 0), 'O': (0, -1)}
    deslocamento = movimentos[orientacao]
    nova_pos_linha = pos_linha + deslocamento[0]
    nova_pos_coluna = pos_coluna + deslocamento[1]
    return nova_pos_linha, nova_pos_coluna

while True:
    linhas, colunas, s_instrucoes = map(int, input().split())
    
    if linhas == 0 and colunas == 0 and s_instrucoes == 0:
        break
    
    arena = [input() for _ in range(linhas)]
    pos_linha, pos_coluna, orientacao = None, None, None

    for linha_a, linha in enumerate(arena):
        direc_index = [linha.find(direc) for direc in movs.keys()]
        direc_index = [(i, col) for i, col in enumerate(direc_index) if col != -1]

        if direc_index:
            pos_linha, pos_coluna = linha_a, direc_index[0][1]
            orientacao = list(movs.keys())[direc_index[0][0]]

    instrucoes = input()
    figurinhas = 0

    for caracter in instrucoes:
        if caracter == 'D':
            orientacao = movs[orientacao][1]
        elif caracter == 'E':
            orientacao = movs[orientacao][0]
        else:
            nova_pos_linha, nova_pos_coluna = movimentacoes(pos_linha, pos_coluna, orientacao)
            if 0 <= nova_pos_linha < linhas and 0 <= nova_pos_coluna < colunas and arena[nova_pos_linha][nova_pos_coluna] != '#':
                pos_linha, pos_coluna = nova_pos_linha, nova_pos_coluna

            if arena[pos_linha][pos_coluna] == '*':
                figurinhas += 1
                arena[pos_linha] = arena[pos_linha][:pos_coluna] + '.' + arena[pos_linha][pos_coluna+1:]

    print(figurinhas)
