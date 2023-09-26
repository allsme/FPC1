"""Calculadora"""

#Definindo a função sucessor:
def sucessor(x):
    sucessor = x + 1
    return sucessor

#Definição da função soma:
def soma(x, y):
    for i in range(y):
      x = sucessor(x)
    return x

#Definição da função multiplicação:
def multiplicacao(x, y):
    resultado = 0
    for i in range(y):
        resultado = soma(resultado, x)
    return resultado

#Definindo a função exponencial:
def exponencial(x, y):
    resultado = 1
    for i in range(y):
        resultado = multiplicacao(resultado, x)
    return resultado

#Chamando a operação desejada
while True:
    try: 
        entrada = input().split()
    
        if entrada[0] == "Suc":
            x = int(entrada[1])
            resultado = sucessor(x)
        elif entrada[0] == "Soma":
            x = int(entrada[1])
            y = int(entrada[2])
            resultado = soma(x, y)
        elif entrada[0] == "Mult":
            x = int(entrada[1])
            y = int(entrada[2])
            resultado = multiplicacao(x, y)
        elif entrada[0] == "Multi":
            x = int(entrada[1])
            y = int(entrada[2])
            resultado = multiplicacao(x, y)
        elif entrada[0] == "Exp":
            x = int(entrada[1])
            y = int(entrada[2])
            resultado = exponencial(x, y)
        else:
            break
        print(resultado)
    
    except EOFError:
        break