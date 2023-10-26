"""Entrega das Caixas"""

#Entrada dos tamanhos das caixas:
A = int(input("Tamanho da Caixa A: "))
B = int(input("Tamanho da Caixa B: "))
C = int(input("Tamanho da Caixa C: "))

#Condicionais para as viajens:
if (A + B) < C:
    D = 1
elif A < B:
    D = 2
elif A > B > C:
    D = 3
print("Quantidade de viajens feitas pelo drone: ", D)