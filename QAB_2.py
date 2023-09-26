#Quebrando a banca

#Definindo a função que buscará o maior saldo possível
def busca_maior(saldo, inicio, fim):
    maior = saldo[inicio]
    maior_idx = inicio
    for i in range(inicio, fim+1):
        if saldo[i] > maior:
            maior = saldo[i]
            maior_idx = i
    return maior_idx

while True:
    
    try:
        entrada = input()

        if entrada:    
            lista_entrada = [int(i) for i in entrada.split()]
            n_digitos_original, n_removidos = lista_entrada
            saldo = [int(i) for i in input()]
            n_digitos = n_digitos_original - n_removidos
            maior_idx = -1
            for i in range(n_digitos):
                inicio = maior_idx + 1
                fim = (n_digitos_original - 1) - (n_digitos - i - 1)
                maior_idx = busca_maior(saldo, inicio, fim)
                print(saldo[maior_idx], end="")
            print()
        else:
            break

    except EOFError:
        break