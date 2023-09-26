def merge_sort(paises_medalhas):
    if len(paises_medalhas) <= 1:
        return paises_medalhas
    
    mid = len(paises_medalhas) // 2
    left_half = paises_medalhas[:mid]
    right_half = paises_medalhas[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx][0] > right[right_idx][0]:
            result.append(left[left_idx])
            left_idx += 1
        elif left[left_idx][0] < right[right_idx][0]:
            result.append(right[right_idx])
            right_idx += 1
        else:
            if left[left_idx][1] > right[right_idx][1]:
                result.append(left[left_idx])
                left_idx += 1
            elif left[left_idx][1] < right[right_idx][1]:
                result.append(right[right_idx])
                right_idx += 1
            else:
                if left[left_idx][2] > right[right_idx][2]:
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1

    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result

def gerar_classificacao(num_paises, dados_paises):
    paises_medalhas = []
    for i in range(num_paises):
        medalhas = list(map(int, dados_paises[i].split()))
        pais = tuple([medalhas[0], medalhas[1], medalhas[2], i + 1])
        paises_medalhas.append(pais)

    paises_clas = merge_sort(paises_medalhas)
    return paises_clas

# Exemplo de uso:
num_paises, num_modalidades = map(int, input().split())
dados_paises = []
for i in range(num_modalidades):
    dados = input(f"Digite as medalhas (ouro prata bronze) da modalidade {i + 1}: ")
    dados_paises.append(dados)

classificacao = gerar_classificacao(num_paises, dados_paises)

# Imprimir a lista de classificação
for pais in classificacao:
    print(pais[3], end=' ')