#Algoritmo da fila de compras dos ingressos da copa

class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.prox = None
        self.ant = None
    
    def __str__(self):
        return f"Meu querido Dado: {self.dado}"

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def is_vazia(self):
        return self.inicio is None and self.fim is None
    
    def inserir(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.ant = self.fim
            self.fim.prox = novo_no
            self.fim = novo_no
            
    def remover(self):
        if self.is_vazia():
            return None
        no_removido = self.inicio
        proximo = self.inicio.prox
        if proximo is not None:
            proximo.ant = None
        if no_removido == self.fim:
            self.fim = None
        self.inicio = proximo
        return no_removido.dado

    
    def __str__(self):
        i = self.inicio
        s = ""
        while i is not None:
            s += f"{i}|"
            i = i.prox
        return s
    
    def inserir_em_lote(self, lista):
        for i in lista:
            self.inserir(i)

#Definindo a entrada
n_pessoas = int(input())
fila_inicial = [int(i) for i in input().split()]
m_sairam = int(input())
lista_sairam = [int(i) for i in input().split()]

fila = Fila()

#Inserindo e removendo as pessoas na fila
fila.inserir_em_lote(fila_inicial)

for pessoa in lista_sairam:
    if pessoa in fila_inicial:
        fila_inicial.remove(pessoa)

for pessoa in fila_inicial:
    print(pessoa, end=' ')
