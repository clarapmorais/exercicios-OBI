qnts = int(input("quantidade: "))

botas = list()
lados = list()
pares = 0

for i in range(0,qnts):
    enter = list(input())
    bota = int(input()) #numero
    lado = str(input()) #lado

    botas.append(bota)
    lados.append(lado)

    for j in range(0,len(botas)-1,2):

        if((bota == botas[j]) & (lado != lados[j])):
            pares+=1

            botas.pop(j)
            lados.pop(j)

            botas.pop(len(botas)-1)
            lados.pop(len(lados)-1)
    

print(pares)