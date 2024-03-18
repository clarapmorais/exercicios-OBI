n, m= [int(i) for i in input().split()]
i, r= [int(j) for j in input().split()]

l=[]
for j in range(1, m+1):

    do_it = False
    rn = input().split(' ')
    rn.pop(0)

    if(j==r):
        for e in rn:
            l.append(e)
    
    for e in rn:
        if(e in l):
            do_it = True
    
    if(do_it):
        for e in rn:
            if(e not in l):
                l.append(e)

print(len(l))