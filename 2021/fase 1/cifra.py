s = str(input())

a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
v = [0, 4, 8, 14, 20]

r = []
for e in s:
    r.append(e)

    if(e not in "aeiou"):
        for l in range(0, len(a)):
            if(a[l] == e):
                idx = l
                break
        
        min_vogal = 35
        min_soma = 35
        for i in v:
            if(idx > i):
                if(idx - i <= min_soma):
                    min_soma = idx-i
                    min_vogal = i
            else:
                if(i - idx < min_soma):
                    min_soma = i-idx
                    min_vogal = i
        
        r.append(a[min_vogal])

        if (e == 'z'):
            r.append('b')
        else:
            if(a[idx+1] not in "aeiou"):
                r.append(a[idx+1])
            else:
                r.append(a[idx+2])
            

for e in r:
    print(e, end='')