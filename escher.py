"""Escher"""

#Entrada da quantidade de números da sequência de alturas:
N = int(input())

#Para armazenar numa lista as alturas:
A = []

#Para listar os números em sequência:
for i in range(1, N+1):
    alturas = int(input())
    A.append(alturas)

#Condicionais para saber se é Escher ou não:
if A[0] + A[N-1] == A[1] + A[N-2] == A[2] + A[N-3] == ... == A[N//2] + A[(N//2)-1]:
    print("S")
else:
    print("N")