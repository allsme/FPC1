#Algoritmo Lavar Louça

class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.ant = None
        self.prox = None

    def __str__(self):
        return "{}".format(self._dado)

class lista():
    def __init__(self):
        self.inicio = None
        self.fim = None

    def e_vazia(self):
        if self.inicio == None:
            return True
        return False

    def insercao_no_final(self, dado=None):
        novo_no = No(dado)
        if self.e_vazia():
            self.inicio = self.fim = novo_no
        else:
            novo_no.ant = self.fim
            self.fim.prox = novo_no
            self.fim = novo_no


    def buscar(self, j):
        i = self.inicio
        while i != None:
            if j == i.dado:
                break
            else:
                i = i.prox
        return i


    def remocao_de_elementos(self, j):
        no_econtrado = self.buscar(j)
        if no_econtrado != None:
            if no_econtrado.ant != None:
                no_econtrado.ant.prox = no_econtrado.prox
            else:
                self.inicio = no_econtrado.prox

            if no_econtrado.prox != None:
                no_econtrado.prox.ant = no_econtrado.ant
            else:
                self.fim = no_econtrado.ant

        return no_econtrado

    def removerDoInicio(self):
        no = self.inicio
        if not self.e_vazia():
            if no.prox == None:
                self.fim = None
            else:
                no.prox.ant = None
            self.inicio = no.prox
        return no

    def __str__(self):
        s = ''
        i = self.inicio
        while i != None:
            s += "{} ".format(str(i))
            i = i.prox
        return s

class fila(lista):
    def inserir(self, dado):
        self.insercao_no_final(dado)

    def remover(self):
        return self.removerDoInicio()

    def limpar(self):
        self.inicio = self.fim = None

festas = int(input())
#Função das jogadas
def rodadas():
    convidados = []
    deck_mesa = fila()
    for i in input().split():
        deck_mesa.inserir(int(i))

    while True:
        fila_mao = fila()
        mao = list(map(int, input().split()))

        if mao[0] == -1:
            break
        else:
            for a in mao:
                fila_mao.inserir(int(a))
            convidados.append(fila_mao)

    for i in range(1000):
        deck_mao = deck_mesa.remover()
        for i in range(len(convidados)):
            jogada_conv = convidados[i].remover()

            if convidados[i].e_vazia() == True:
                return i+1
            if jogada_conv.dado != deck_mao.dado:
                convidados[i].inserir(jogada_conv.dado)

        deck_mesa.inserir(deck_mao)
    return 0

for x in range(festas):
    print(rodadas())