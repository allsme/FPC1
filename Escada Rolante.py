#Escada Rolante

#Entrada da quantidade de pessoas que passaram:
N = int(input())

#Aramazenar em uma lista os tempos:
lista_tempos = []

#Para listar os marcos de tempo de cada pessoa:
for _ in range(N):
    tempos = int(input())
    lista_tempos.append(tempos)


#Calculo do tempo
tempo_total = 0 
for i in range(N-1):
    diferenca_tempo = lista_tempos[i+1] - lista_tempos[i]
    tempo_total += diferenca_tempo

#Adicionando os 10s do ultimo intervalo:
tempo_total += 10
print(tempo_total)