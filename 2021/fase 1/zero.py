n = int(input())

l=[]
for i in range(0, n):
    num = int(input())

    if(num==0):
        l.pop()
    else:
        l.append(num)

soma=0
for e in l:
    soma+=e

print(soma)