import csv
from dis import dis
from email.policy import default
from No import  No

# Abre o csv com os arquivos disponibilizados 
def abre_csv(path):
    arq = open(f'{path}.csv','r')
    arquivo = csv.reader(arq,quoting=csv.QUOTE_NONNUMERIC)
    lista = []
    for it in arquivo:
        lista.append(it)
    return lista

# Acha o menor nó com o custo mais baixo em relação aos nos abertos
def menor_no(nos_abertos:list) -> No:
    
    custo_menor_no = nos_abertos[0].get_peso_no()
    menor_no = nos_abertos[0]

    for no in nos_abertos[1:]:
        if no.get_peso_no() < custo_menor_no:
            custo_menor_no  = no.get_peso_no() 
            menor_no        = no
    return menor_no

# Retorna o proximo nó que deve ser visitado, ou o no do objetivo
def proximo_no(no_atual,dist_real,heuristica,no_final,nos_abertos,no_objetivo):
    
    cont = 1
    # Já visitou retira da lista 
    if no_atual in nos_abertos:
        nos_abertos.remove(no_atual)

    # Adiciona Valores a Lista mediante algumas condições
    for dist,heur in zip(dist_real,heuristica):
            if dist[no_atual.nodo-1]!= 0  and cont != no_atual.nodo and no_atual.nodo != no_final.nodo and no_atual.pai.nodo!=cont:
                no = No(cont,no_atual,dist[no_atual.nodo-1],heur[no_final.nodo-1])
                no.set_custo_ate_aqui(no_atual.custo_ate_aqui + no.custo)
                print(f'*** Custo para estar no NO {no.nodo} eh: {no.custo_ate_aqui} ***')
                nos_abertos.append(no)
                no_atual.adiciona_adjacentes(no)
            cont = cont + 1
    no_atual.exibir_adjacentes()
    
    # Verifica objetivo, para tomada de decisoes
    if no_atual.get_adjacentes()>0 and no_atual.nodo != no_final.nodo:
        p_no = menor_no(nos_abertos)
    elif no_atual.nodo != no_final.nodo:
        # custo = remove_custo(no_atual,p_no,todos_nos_abertos)
        p_no = menor_no(nos_abertos)
    else:
        if no_objetivo.nodo == default:
            no_objetivo = no_atual
        elif no_objetivo.nodo<no_atual.nodo:
            no_objetivo = no_atual
        
        p_no = menor_no(nos_abertos)
        if p_no.get_peso_no() < no_objetivo.get_peso_no():
            return p_no,nos_abertos
        else:
            return no_objetivo,nos_abertos
    

    return p_no,nos_abertos



# ------------------------------------------------------------------------------------------------------------------------------------------

# Leitura do aquivo csv 
heuristica = abre_csv('../bases/heuristics')
dist_real = abre_csv('../bases/real-distances')

# Inicialização dos No's para  criação do Algoritimo
no_pai_default = No()
no_objetivo    = No()
no_anterior    = No()
no_inicial     = No(6,no_pai_default,0,15.2)
no_final       = No(13,no_pai_default,0,0)

# Inicialização das Variaveis que vão ser Utilizadas
nos_abertos = []


# Loop para encontrar o mlehor caminho 
while(no_anterior.nodo==default or no_anterior.nodo!=no_final.nodo or no_anterior!=no_inicial):

    no_inicial,nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,no_objetivo)
    no_anterior = no_inicial

    print(f'No atual : E{no_inicial.nodo}, Custo Atual: {no_inicial.get_peso_no()}')
    print('Nos abertos : ',end='')
    for no_aberto in nos_abertos:
        print(f'E{no_aberto.nodo}',end=' ')
    print('\n-------------------------------------')

no_inicial.get_caminho(no_inicial)
print(f'O Preço total para chegar nesse No foi {no_inicial.get_peso_no()}')