#Algortimo Linhas Cruzadas:

#Definindo as entradas
numeros = int(input()) #Quantidade de números
ord_horizontal = list(map(int, input().split())) #Ordem dos pregos na horizontal

#Definindo uma função para contar os cruzamentos:
def cont_cruzamentos(ord_vertical):
    quant_cruzamentos = 0 #Contador dos cruzamentos
    
    #Loop para encontrar os cruzamentos
    for i in range(len(ord_vertical)):
        for j in range(i):
            if ord_vertical[j] > ord_vertical[i]:
                quant_cruzamentos += 1
    return quant_cruzamentos

#Calculo da quantidade total de cruzamentos:
total_cruz = cont_cruzamentos(ord_horizontal)

print(total_cruz)
