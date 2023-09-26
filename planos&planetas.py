#Algoritmo Planos e Planetas

class Hash_Table:
    def __init__(self):
        self.tabela = {}
    
    def inserir(self, chave, valor):
        if chave in self.tabela:
            self.tabela[chave] += valor
        else:
            self.tabela[chave] = valor
    
    def max_regiao(self):
        max_regiao = max(self.tabela.values())
        return max_regiao

def principal():
    #Definindo entrada
    m_planos, n_planetas = map(int, input().split())
    planos = [list(map(int, input().split())) for i in range(m_planos)]
    planetas = [list(map(int, input().split())) for i in range(n_planetas)]

    #Criando tabela hash
    tabela = Hash_Table()

    #Inserindo valores na tabela
    for planeta in planetas:
        regiao = ''
        for plano in planos:
            A, B, C, D = plano
            X, Y, Z = planeta
            if A*X + B*Y + C*Z - D > 0:
                regiao += '1'
            else:
                regiao += '0'
        tabela.inserir(regiao, 1)
    
    max_regiao = tabela.max_regiao()
    print(max_regiao)

if __name__ == '__main__':
    principal()