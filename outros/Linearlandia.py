def buscar_caminho(a, e, i, saida, chegada, empresa):
    maior = maior2 = 0
    for j in range(0 , len(saida)):
        if(j == i):
            continue

        if(saida[j] == a and e != empresa[j]):
            return j, "s"
        elif(chegada[j] == a and e != empresa[j]):
            return j, "c"
    return None
#main

s = int(input())

saida = []
chegada = []
empresa = []
for i in range(1, s):
    p = str(input()).split(' ')
    saida.append(p[0])
    chegada.append(p[1])
    empresa.append(p[2])

maior = 0
maior2 = 0
atualP = None
atualE = None
for e in range(0, s-1):
    atualP = saida[e]
    atualE = empresa[e]
    maior2=0
    while(True):
        retorno = buscar_caminho(atualP, atualE, e, saida, chegada, empresa)
        if(retorno==None):
            break
        elif(retorno[1] == "s"):
            atualP = saida[retorno[0]]
            atualE = empresa[retorno[0]]
        elif(retorno[1] == "c"):
            atualP = chegada[retorno[0]]
            atualE = empresa[retorno[0]]
        
        maior2+=1

    if(maior2 > maior):
        maior = maior2
        
for e in range(0, s-1):
    atualP = chegada[e]
    atualE = empresa[e]
    maior2=0
    while(True):
        retorno = buscar_caminho(atualP, atualE, e, saida, chegada, empresa)
        if(retorno==None):
            break
        elif(retorno[1] == "s"):
            atualP = saida[retorno[0]]
            atualE = empresa[retorno[0]]
        elif(retorno[1] == "c"):
            atualP = chegada[retorno[0]]
            atualE = empresa[retorno[0]]
        
        maior2+=1

    if(maior2 > maior):
        maior = maior2
print(maior)