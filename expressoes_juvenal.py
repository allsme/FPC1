#Algoritmo de Expressões Juvenal

class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
        self.ant = None

class Pilha:
    def __init__(self):
        self.itens = None
    
    def e_vazia(self):
        return self.itens is None
    
    def push(self, item):
        novo_no = No(item)
        if self.itens is None:
            self.itens = novo_no
        else:
            novo_no.ant = self.itens
            self.itens.prox = novo_no
            self.itens = novo_no
    
    def pop(self):
        if self.itens is None:
            return None
        no_removido = self.itens
        self.itens = no_removido.ant
        return no_removido.dado
    
    def peek(self):
        if self.itens is None:
            return None
        return self.itens.dado
    
    def tam(self):
        tamanho = 0
        tam_atual = self.itens
        while tam_atual is not None:
            tamanho += 1
            tam_atual = tam_atual.ant
        return tamanho

#Definindo as entradas
n_expressoes = int(input())
if n_expressoes > 20:
    ValueError

for i in range(n_expressoes):
    cadeia_caracteres = input()
    
    pilha_caracteres = Pilha() #Para armazenar os caracteres numa pilha

    expressao_definida = True
    for caractere in cadeia_caracteres:
        if caractere == "(" or caractere == "[" or caractere == "{":
            pilha_caracteres.push(caractere)
        elif caractere == ")":
            if pilha_caracteres.peek() == "(":
                pilha_caracteres.pop()
            else:
                expressao_definida = False
                break
        elif caractere == "]":
            if pilha_caracteres.peek() == "[":
                pilha_caracteres.pop()
            else:
                expressao_definida = False
                break
        elif caractere == "}":
            if pilha_caracteres.peek() == "{":
                pilha_caracteres.pop()
            else:
                expressao_definida = False
                break

    if not pilha_caracteres.e_vazia():
        expressao_definida = False
    
    if expressao_definida:
        print("S")
    else:
        print("N")
