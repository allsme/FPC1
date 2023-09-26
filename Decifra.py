#Decifra o código

alfa_mix = input() #Entrada do alfabeto criptografado
frase_mix = input() #Entrada da frase embaralhada

#Mapeamento das letras do alfabeto por meio do dicionário:
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
dicionario = {}
for i in range(len(alfabeto)):
    dicionario[alfa_mix[i]] = alfabeto[i]

#Definindo a função para discriptografar a frase
def descriptografia(dicio, frase_mix):
    frase_correta = str()
    for j in frase_mix:
        frase_correta = frase_correta + dicio[j]
    return frase_correta
    
print(descriptografia(dicionario, frase_mix))