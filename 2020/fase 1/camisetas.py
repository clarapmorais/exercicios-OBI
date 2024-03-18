#FROM https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/camisetas/
#NOTA: 5/5

n = int(input(''))
t = str(input()).split()

cp = t.count('1')
cm = t.count('2')

p = int(input(''))
m = int(input(''))

if(cp == p and cm == m):
    print("S")
else:
    print("N")