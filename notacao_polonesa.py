#Algorimo Notação Polonesa

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
        novo_no.prox = self.itens
        self.itens = novo_no
    
    def pop(self):
        if self.itens is None:
            return None
        no_removido = self.itens
        self.itens = no_removido.prox
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

def notacao_polonesa(expressao):
    pilha = Pilha()
    index = len(expressao) - 1

    #Calculando a expressão
    while index >= 0:
        token = expressao[index]
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            pilha.push(int(token))
        elif token in ('+', '-', '*', '/'):
            operando_1 = pilha.pop()
            operando_2 = pilha.pop()

            if token == '+':
                resultado = operando_1 + operando_2
            elif token == '-':
                resultado = operando_1 - operando_2
            elif token == '*':
                resultado = operando_1 * operando_2
            elif token == '/':
                #Condicional para quando o operando for zero
                if operando_2 == 0:
                    return ValueError
                else:
                    resultado = int(operando_1 / operando_2)

            pilha.push(resultado)

        index -= 1

    return pilha.pop()

def main():
    while True:
        entrada = input().split()
        if not entrada:
            break
        solucao = notacao_polonesa(entrada)
        print(solucao)

if __name__ == '__main__':
    main()