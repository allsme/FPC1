#Algortimo Hospital

# Função para calcular a prioridade de cada paciente
def calc_prioridade(paciente):
    conj_planos = {"premium": 6, "diamante": 5, "ouro": 4, "prata": 3, "bronze": 2, "resto": 1}
    nome, plano, gravidade = paciente #Agrupando tudo numa lista
    return (-conj_planos[plano], gravidade, nome)

# Número de pacientes (N)
x_pacientes = int(input())

# Lista para armazenar os pacientes
lista_pacientes = []

# Ler as informações dos pacientes
for _ in range(x_pacientes):
    nome, plano, gravidade = input().split()
    gravidade = int(gravidade)
    lista_pacientes.append((nome, plano, gravidade))

# Ordenar a lista de pacientes com base nas prioridades
for i in range(1, x_pacientes):
    chave_atual = lista_pacientes[i]
    j = i - 1
    while j >= 0 and calc_prioridade(chave_atual) < calc_prioridade(lista_pacientes[j]):
        lista_pacientes[j + 1] = lista_pacientes[j]
        j -= 1
    lista_pacientes[j + 1] = chave_atual

# Imprimir os nomes dos pacientes na fila de atendimento do HCSPP
for paciente in lista_pacientes:
    print(paciente[0])