import csv
from No import  No

def abre_csv(path):
    arq = open(f'{path}.csv','r')
    arquivo = csv.reader(arq,quoting=csv.QUOTE_NONNUMERIC)
    lista = []
    for it in arquivo:
        lista.append(it)
    return lista
    
def abrir_proximo(nos_abertos:list,custo_atual:float) -> No:
    custo_menor_no = nos_abertos[0].get_peso_no() + custo_atual
    menor_no = nos_abertos[0]

    for no in nos_abertos[1:]:
        if no.get_peso_no() + custo_atual < custo_menor_no:
            custo_menor_no = no.get_peso_no() + custo_atual
            menor_no       = no
    return menor_no,(custo_atual + menor_no.custo)


# def caminho_no_inicial(no_inical: int,no:No,dist_real):
#     custo = 0
#     no_verf = no.nodo
#     while(no_verf-1!=no_inical-1):
#         custo = 


def verifica_no(no_atual,nos_abertos):
    i = 0
    while(i<len(nos_abertos)):
        if nos_abertos[i].nodo == no_atual-1:
            return i
        i = i+1
    return -1

def verifica_pai_no(no_atual,nos_abertos,no_aberto):
    i = 0
    while(i<len(nos_abertos)):
        print(f'F: {nos_abertos[i].nodo},{no_atual-1},{nos_abertos[i].pai},{no_aberto}')
        if nos_abertos[i].nodo == no_atual and nos_abertos[i].pai==no_aberto:
            return False
        i = i+1
    return True


def proximo_no(no_atual,dist_real,heuristica,nos_abertos,custo_atual,E_final):
   
    cont = 0
    flag_aberto_no = False
    qtd_abertos = 0
    pos_ver = verifica_no(no_atual,nos_abertos)
    if pos_ver != -1:
        custo_no_saida = nos_abertos[pos_ver].custo
        del nos_abertos[pos_ver]
    falg_pai  = True
    for dist,heur in zip(dist_real,heuristica):
        if dist[no_atual-1]!= 0  and cont!=no_atual and no_atual != E_final:
            # print(dist[no_atual-1],heur[E_final-1],cont) #Lembrar de passar o E_FINAL como parametro
            no = No(cont,no_atual-1,dist[no_atual-1],heur[E_final-1])
            # print(f'Custo {no.get_peso_no()+custo_atual}')
            falg_pai = verifica_pai_no(no_atual,nos_abertos,cont)
            if falg_pai==True:
                nos_abertos.append(no)
            qtd_abertos = qtd_abertos + 1
            flag_aberto_no = True
        cont = cont + 1
    
    if falg_pai == True:
        if no_atual== E_final:
            # print("aquiiiii")
            print(f'Qtd: {qtd_abertos}')
        else:
            a,b = abrir_proximo(nos_abertos,custo_atual)
            print(f'Custo {b+a.heuristica}')
            return a,b,nos_abertos
    elif qtd_abertos == 1:
        a,b = abrir_proximo(nos_abertos,custo_atual-custo_no_saida)
        print(f'Custo {b+a.heuristica}')
        return a,b,nos_abertos
          
    


# --------------------------------------------------------------------------------------
heuristica = abre_csv('../bases/heuristics')
dist_real = abre_csv('../bases/real-distances')
E_inicial = 6
E_final = 13


no_atual = E_inicial
custo_atual = 0
# cont = 0

# while(no_atual==E_final):
nos_abertos = []
no_atual,custo_atual,nos_abertos = proximo_no(no_atual,dist_real,heuristica,nos_abertos,custo_atual,E_final)
print(f'No atual : E{no_atual.nodo+1}, Custo Atual: {custo_atual}')
for no_aberto in nos_abertos:
                print(no_aberto.nodo)

no_atual,custo_atual,nos_abertos = proximo_no(no_atual.nodo+1,dist_real,heuristica,nos_abertos,custo_atual,E_final)
print(f'No atual : E{no_atual.nodo+1}, Custo Atual: {custo_atual}')
for no_aberto in nos_abertos:
                print(no_aberto.nodo)
no_atual,custo_atual,nos_abertos = proximo_no(no_atual.nodo+1,dist_real,heuristica,nos_abertos,custo_atual,E_final)
print(f'No atual : E{no_atual.nodo+1}, Custo Atual: {custo_atual}')
for no_aberto in nos_abertos:
                print(no_aberto.nodo)

no_atual,custo_atual,nos_abertos = proximo_no(no_atual.nodo+1,dist_real,heuristica,nos_abertos,custo_atual,E_final)
print(f'No atual : E{no_atual.nodo+1}, Custo Atual: {custo_atual}')
for no_aberto in nos_abertos:
                print(no_aberto.nodo)

no_atual,custo_atual,nos_abertos = proximo_no(no_atual.nodo+1,dist_real,heuristica,nos_abertos,custo_atual,E_final)
print(f'No atual : E{no_atual.nodo+1}, Custo Atual: {custo_atual}')
for no_aberto in nos_abertos:
                print(no_aberto.nodo)