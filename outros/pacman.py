#FROM https://www.urionlinejudge.com.br/judge/pt/problems/view/2451

size = int(input(''))

mapa = list()
for i in range(size):
    linha = str(input(''))

    if i%2!=0:
        linha=linha[::-1]

    for e in linha:
            mapa.append(e)

atual = 0
maximo = 0
for c in mapa:

    if c == 'o':
        atual += 1  
    elif c == 'A':
        atual = 0

    if atual > maximo:
        maximo = atual

print(maximo)