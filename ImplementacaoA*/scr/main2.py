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
    
    custo_menor_no = nos_abertos[0].get_peso_no()
    menor_no = nos_abertos[0]

    for no in nos_abertos[1:]:
        if no.get_peso_no() < custo_menor_no:
            custo_menor_no  = no.get_peso_no() 
            menor_no        = no
    return menor_no,(menor_no.get_peso_no())


# def remove_custo(no_atual,p_no,todos_nos_abertos):

#     print('#############################################')
#     custo = no_atual.custo
#     no = no_atual
#     while(no.pai != p_no.pai):
#         for nos in todos_nos_abertos:
#             if nos.pai == no.pai:
#                 no = nos
#                 break
#         custo = custo + no.custo
#     print(f"Custo para se estar nesse no {custo}")

#     print(f"No atual : {no_atual.nodo}  Pai do atual {no_atual.pai}\
#          e Menor no: {p_no.nodo} Pai do menor no {p_no.pai}")

#     print('#############################################')
#     return custo



def proximo_no(no_atual,dist_real,heuristica,no_final,nos_abertos,custo_atual,todos_nos_abertos):
    
    cont = 1
    if no_atual in nos_abertos:
        print('Yes')
        nos_abertos.remove(no_atual)

    for dist,heur in zip(dist_real,heuristica):
            if dist[no_atual.nodo-1]!= 0  and cont != no_atual.nodo and no_atual.nodo != no_final.nodo and no_atual.pai!=cont:
                # print(dist[no_atual-1],heur[E_final-1],cont) #Lembrar de passar o E_FINAL como parametro
                # print(f'{cont},{no_atual.nodo-1},{dist[no_atual.nodo-1]},{heur[E_final-1]}')
                no = No(cont,no_atual.nodo,dist[no_atual.nodo-1],heur[E_final-1])
                no.set_custo_ate_aqui(no_atual.custo_ate_aqui + no.custo)
                print(f'### Custo para estar no NO {no.nodo} eh: {no.custo_ate_aqui} ###')
                todos_nos_abertos.append(no)
                nos_abertos.append(no)
                no_atual.adiciona_adjacentes(no)
                # qtd_abertos = qtd_abertos + 1
            cont = cont + 1
    no_atual.exibir_adjacentes()
    

    if no_atual.get_adjacentes()>0 :
        p_no , custo_atual = menor_no(nos_abertos,custo_atual)
    elif no_atual.nodo != no_final.nodo:
        # custo = remove_custo(no_atual,p_no,todos_nos_abertos)
        p_no , custo_atual = menor_no(nos_abertos,custo_atual)
    else:
        print('Pensar no ultimo passo')
        

    return p_no,custo_atual,nos_abertos,todos_nos_abertos
# ------------------------------------------------------------------------------------------------------------------------------------------
heuristica = abre_csv('../bases/heuristics')
dist_real = abre_csv('../bases/real-distances')
E_inicial = 6
E_final = 13

no_inicial = No(6,-1,0,15.2)
no_final   = No(13,-2,0,0)

nos_abertos = []
todos_nos_abertos = []
custo_atual = 0

no_inicial,custo_atual,nos_abertos,todos_nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,custo_atual,todos_nos_abertos)
print(f'No atual : E{no_inicial.nodo}, Custo Atual: {custo_atual}')
print('Nos abertos : ',end='')
for no_aberto in nos_abertos:
    print(f'E{no_aberto.nodo}',end=' ')
print('\n-------------------------------------')

no_inicial,custo_atual,nos_abertos,todos_nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,custo_atual,todos_nos_abertos)
print(f'No atual : E{no_inicial.nodo}, Custo Atual: {custo_atual}')
print('Nos abertos : ',end='')
for no_aberto in nos_abertos:
    print(f'E{no_aberto.nodo}',end=' ')    
print('\n-------------------------------------')

no_inicial,custo_atual,nos_abertos,todos_nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,custo_atual,todos_nos_abertos)
print(f'No atual : E{no_inicial.nodo}, Custo Atual: {custo_atual}')
print('Nos abertos : ',end='')
for no_aberto in nos_abertos:
    print(f'E{no_aberto.nodo}',end=' ')
print('\n-------------------------------------')

no_inicial,custo_atual,nos_abertos,todos_nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,custo_atual,todos_nos_abertos)
print(f'No atual : E{no_inicial.nodo}, Custo Atual: {custo_atual}')
print('Nos abertos : ',end='')
for no_aberto in nos_abertos:
    print(f'E{no_aberto.nodo}',end=' ')
print('\n-------------------------------------')

no_inicial,custo_atual,nos_abertos,todos_nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,custo_atual,todos_nos_abertos)
print(f'No atual : E{no_inicial.nodo}, Custo Atual: {custo_atual}')
print('Nos abertos : ',end='')
for no_aberto in nos_abertos:
    print(f'E{no_aberto.nodo}',end=' ')
print('\n-------------------------------------')




# cont = 0

# while(no_inicial==E_final):

#     no_inicial,custo_atual,nos_abertos,todos_nos_abertos = proximo_no(no_inicial,dist_real,heuristica,no_final,nos_abertos,custo_atual,todos_nos_abertos)
#     print(f'No atual : E{no_inicial.nodo}, Custo Atual: {custo_atual}')
#     print('Nos abertos : ',end='')
#     for no_aberto in nos_abertos:
#         print(f'E{no_aberto.nodo}',end=' ')
#     print('\n-------------------------------------')