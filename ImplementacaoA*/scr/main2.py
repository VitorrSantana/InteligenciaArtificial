import csv
from dis import dis
from No import  No

def abre_csv(path):
    arq = open(f'{path}.csv','r')
    arquivo = csv.reader(arq,quoting=csv.QUOTE_NONNUMERIC)
    lista = []
    for it in arquivo:
        lista.append(it)
    return lista

def menor_no(nos_abertos:list,custo_atual:float) -> No:
    custo_menor_no = nos_abertos[0].get_peso_no() + custo_atual
    menor_no = nos_abertos[0]

    for no in nos_abertos[1:]:
        if no.get_peso_no() + custo_atual < custo_menor_no:
            custo_menor_no  = no.get_peso_no() + custo_atual
            menor_no        = no
    return menor_no,(custo_atual + menor_no.custo)

# def remove_custo(no_atual,p_no):




def proximo_no(no_atual,dist_real,heuristica,no_final,nos_abertos,custo_atual):
    
    cont = 1
    if no_atual in nos_abertos:
        print('Yes')
        nos_abertos.remove(no_atual)

    for dist,heur in zip(dist_real,heuristica):
            if dist[no_atual.nodo-1]!= 0  and cont != no_atual.nodo and no_atual.nodo != no_final.nodo and no_atual.pai!=cont:
                # print(dist[no_atual-1],heur[E_final-1],cont) #Lembrar de passar o E_FINAL como parametro
                # print(f'{cont},{no_atual.nodo-1},{dist[no_atual.nodo-1]},{heur[E_final-1]}')
                no = No(cont,no_atual.nodo,dist[no_atual.nodo-1],heur[E_final-1])
                nos_abertos.append(no)
                no_atual.adiciona_adjacentes(no)
                # qtd_abertos = qtd_abertos + 1
            cont = cont + 1
    no_atual.exibir_adjacentes()
    

    if no_atual.get_adjacentes()>0 :
        p_no , custo_atual = menor_no(nos_abertos,custo_atual)
    else:
        print('Voltar no custo até achar')
        p_no , custo_atual = menor_no(nos_abertos,custo_atual)
        # custo_atual = remove_custo(no_atual,p_no)
    
    return p_no,custo_atual,nos_abertos
# ------------------------------------------------------------------------------------------------------------------------------------------
heuristica = abre_csv('../bases/heuristics')
dist_real = abre_csv('../bases/real-distances')
E_inicial = 6
E_final = 13

no_inicial = No(6,-1,0,15.2)
no_final   = No(13,-2,0,0)

nos_abertos = []
custo_atual = 0

no_inicial,custo_atual,nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,custo_atual)
print(f'No atual : E{no_inicial.nodo}, Custo Atual: {custo_atual}')
print('Nos abertos : ',end='')
for no_aberto in nos_abertos:
    print(f'E{no_aberto.nodo}',end=' ')
print('\n-------------------------------------')

no_inicial,custo_atual,nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,custo_atual)
print(f'No atual : E{no_inicial.nodo}, Custo Atual: {custo_atual}')
print('Nos abertos : ',end='')
for no_aberto in nos_abertos:
    print(f'E{no_aberto.nodo}',end=' ')    
print('\n-------------------------------------')

no_inicial,custo_atual,nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,custo_atual)
print(f'No atual : E{no_inicial.nodo}, Custo Atual: {custo_atual}')
print('Nos abertos : ',end='')
for no_aberto in nos_abertos:
    print(f'E{no_aberto.nodo}',end=' ')
print()




# cont = 0

# while(no_atual==E_final):
# nos_abertos = []
# no_atual,custo_atual,nos_abertos = proximo_no(no_atual,dist_real,heuristica,nos_abertos,custo_atual,E_final)
# print(f'No atual : E{no_atual.nodo+1}, Custo Atual: {custo_atual}')
# for no_aberto in nos_abertos:
#                 print(no_aberto.nodo)