from xmlrpc.client import Boolean


class No:
    
    def __init__(self,nodo,pai,custo,heuristica,morto = False) -> None:
        self.nodo  = nodo
        self.pai   = pai
        self.custo = custo
        self.heuristica = heuristica
        self.morto = morto
        self.adjacentes = []

    def get_peso_no(self) -> float:
        return self.custo+self.heuristica

    def adiciona_adjacentes(self,adjacente):
        self.adjacentes.append(adjacente)
    
    def exibir_adjacentes(self) -> None:
        for adjacente in self.adjacentes:
            print(f'Adjacentes: E{adjacente.nodo} Custo: {adjacente.custo}')

    def get_adjacentes(self):
        return len(self.adjacentes)