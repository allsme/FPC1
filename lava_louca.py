class no:
    def __init__(self,dado):
        print("construindo um")
        self.dado = dado
        self.prox = None
        self.ant = None
    
    def __str__(self):
        return f"0 dado é {self.dado}"
    
class lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def e_vazia(self):
        if self.inicio == None:
            return True
        return False
    
    def inserir_no_fim(self, dado=None):
        novo_no = no(dado)
        if self.e_vazia():
            self.inicio = self.fim = novo_no
        else:
            novo_no.ant = self._fim
            self.fim.prox = novo_no
            self.fim = novo_no

    def buscar(self, x):
        i = self.inicio
        while i != None:
            if x == self.dado:
                break
            else:
                i = i.prox
        return i

    def remocao_elem(self, x):
        encontrado = self.buscar(x)
        if encontrado != None:
            if encontrado.ant != None:
                encontrado.ant.prox = encontrado.prox
            else:
                self.inicio = encontrado.prox

            if encontrado.prox != None:
                encontrado.prox.ant = encontrado.ant
            else:
                self.fim = encontrado.ant
        
        return encontrado
    
    def remover_do_inicio(self):
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
        self.inserir_no_fim(dado)

    def remover(self):
        return self.remover_do_inicio()
    
    def limpar(self):
        self.inicio = self.fim = None

festas = int(input())

def rodadas():
    mesa = fila()
    convidados = []

    #Leitura da mesa:
    for i in input().split():
        mesa.inserir(int(i))
    
    #Leitura dos convidados:
    while True:
        deck_fila = fila()
        deck_convidado = list(map(int, input().split()))
        #Caso base
        if deck_convidado[0] == -1:
            break
        else:
            for i in deck_fila:
                deck_fila.inserir(i) 
            convidados.append(deck_fila) 

    for i in range(1000):
        carta = mesa.remover() 
        for j in range(len(convidados)):
            jogada = convidados[j].remover()

            if convidados.e_vazia():
                return j+1
            if jogada.dado != carta.dado:
                convidados[j].inserir(jogada.dado)
            
        mesa.inserir(carta)
    return 0 

for i in range(festas):
    print(rodadas())   
