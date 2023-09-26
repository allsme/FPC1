"""Piloto Automático"""

#Entrada das velocidades dos carros: 
A = int(input())
B = int(input())
C = int(input())
D = int(input())

#Condicional para a aceleração, desaceleração ou manter a velocidade:
if (B - A) < (C - B):
    D = 1
elif (B - A) > (C - B):
    D = -1
else:
    D = 0
print(D)