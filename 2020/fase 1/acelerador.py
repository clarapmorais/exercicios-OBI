#FROM https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/acelerador/
#NOTA 5/5

d = int(input(""))
d=d-3

r=d%8

if(r == 3):
    print(1)
elif(r == 4):
    print(2)
else:
    print(3)