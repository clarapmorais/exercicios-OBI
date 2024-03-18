#FROM https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/fissura/
#NOTA submissão indisponível

e = str(input('')).split()
t = int(e[0])
d = int(e[1])

m = list()
for i in range(t):
    l = str(input(''))

    l2 = list()
    for e in l:
        l2.append(int(e))
    
    m.append(l2)

def contamina(i, j):
    m[i][j] = '*'

    if(i != 0):
        try:
            if(d >= m[i-1][j]):
                contamina(i-1, j)
        except:
            pass

    if(i != t):
        try:
            if(d >= m[i+1][j]):
                contamina(i+1, j)
        except:
            pass

    if(j != 0):
        try:
            if(d >= m[i][j-1]):
                contamina(i, j-1)
        except:
            pass

    if(j != t):
        try:
            if(d >= m[i][j+1]):
                contamina(i, j+1)
        except:
            pass

if(d >= m[0][0]):
    contamina(0, 0)

for i in range(t):
    for j in range(t):
        print(m[i][j], end='')
    print()
        
            