#exercicío retirado de: https://www.urionlinejudge.com.br/judge/en/problems/view/1608

t = int(input(''))

respostas=[]
for i in range(t):
    entrada = str(input(''))
    d, i, b = map(int, entrada.split())
    
    ingredientes=str(input('')).split()

    niobizinhos=[]
    for j in range(0, b):
        bd=str(input('')).split()
       
        for k in range(1, len(bd), 2):
            niobizinhos.append(
                int(ingredientes[int(bd[int(k)])])*
                int(bd[int(k+1)])
                )

    maior = d / niobizinhos[0]
    im = 0
    for j in range(1, len(niobizinhos)):
        if(d / niobizinhos[j] > maior):
            maior = d / niobizinhos[j]
            im = j

    respostas.append(im+1)

for i in respostas:
    print(i)
