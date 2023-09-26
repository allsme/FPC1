#Algoritmo robô

#Dicionário para armazenar os movimentos
movs = {'N': ['O', 'L'], 'L': ['N', 'S'], 'S': ['L', 'O'], 'O': ['S', 'N']}

while True:
    linhas, colunas, s_instrucoes = [int(i) for i in input().split()]
    
    #Caso base
    if linhas == 0 and colunas == 0 and s_instrucoes == 0:
        break
    
    status_pi, direcao, arena, direcoes = 0, '', [], ['N', 'S', 'O', 'L']
    #status_pi é o status da posição inical
    pos_lin, pos_col, orientacao = None, None, None

    for linha_a in range(0, linhas):
        linha = input()
        #Olha para ver se tem alguma direção na linha
        if status_pi == 0 and any(direc in linha for direc in direcoes):
            pos_col = [linha.find(direc) for direc in direcoes]
            pos_lin = linha_a
            for j in range(0, len(pos_col)):
                if pos_col[j] != -1:
                    orientacao = direcoes[j]
                    pos_col = pos_col[j]
                    break
            status_pi = 1
        arena.append(linha)

    instrucoes = input()
    figurinhas = 0

    for caracter in instrucoes:
        if caracter == 'D':
            orientacao = movs[orientacao][1]
        elif caracter == 'E':
            orientacao = movs[orientacao][0]
        else:
            if orientacao == 'N' and pos_lin > 0:
                if arena[pos_lin-1][pos_col] == '#':
                    pass
                else:
                    pos_lin -= 1
            elif orientacao == 'L' and pos_col < colunas-1:
                if arena[pos_lin][pos_col+1] == '#':
                    pass
                else:
                    pos_col += 1
            elif orientacao == 'S' and pos_lin < linhas-1:
                if arena[pos_lin+1][pos_col] == '#':
                    pass
                else:
                    pos_lin += 1
            elif orientacao == 'O' and pos_col > 0:
                if arena[pos_lin][pos_col-1] == '#':
                    pass
                else:
                    pos_col -= 1

            #Contagem de figurinhas
            if arena[pos_lin][pos_col] == '*':
                figurinhas += 1
                i = pos_col
                arena[pos_lin] = arena[pos_lin][0:i] + '.' + arena[pos_lin][i+1:]

    print(figurinhas)