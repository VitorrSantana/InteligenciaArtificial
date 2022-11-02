from email.policy import default
from xmlrpc.client import Boolean


class No:
    
    def __init__(self,nodo=default,pai=default,custo=default,heuristica=default,morto = False) -> None:
        self.nodo  = nodo
        self.pai   = pai
        self.custo = custo
        self.heuristica = heuristica
        self.morto = morto
        self.custo_ate_aqui = 0
        self.adjacentes = []
        self.caminho = []

    def get_peso_no(self) -> float:
        return self.heuristica + self.custo_ate_aqui

    def adiciona_adjacentes(self,adjacente):
        self.adjacentes.append(adjacente)
    
    def exibir_adjacentes(self) -> None:
        for adjacente in self.adjacentes:
            print(f'Adjacentes: E{adjacente.nodo} Custo: {adjacente.custo}')

    def get_adjacentes(self):
        return len(self.adjacentes)
    
    def set_custo_ate_aqui(self,custo_aqui):
        self.custo_ate_aqui = custo_aqui
    
    def get_caminho(self,no):
        caminho = []
        caminho.append(no.nodo)
        while(no.pai!=default):
            if type(no.pai.nodo)==int:
                caminho.append(no.pai.nodo)
            no = no.pai
        print('O caminho para chegar nesse no foi: ',end='')
        for cam in reversed(caminho):
            print(f'{chr(cam+64)}',end = ' ')
        print()