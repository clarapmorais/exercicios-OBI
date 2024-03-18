from typing import Tuple


size, fiss = str(input()).split()

size = int(size)
fiss = int(fiss)
kilaeua = []
addb = []
for i in range(0, size):
    addb.clear()
    adda = str(input())

    for j in adda:
        addb.append(str(j))

    kilaeua.append(list(addb))
    

print(kilaeua)

if(int(kilaeua[0][0]) <= fiss):
    kilaeua[0][0] = "*"

for i in range(0, size):
    top = bot = left = right = False
    for j in range(0, size):
        if(i!=0):
            top = True
        if(i!=size-1):
            bot = True

        if(j!=0):
            left = True
        if(j!=size-1):
            right = True
        if(kilaeua[i][j] == '*'):
            if(top):
                try:
                    if(int(kilaeua[i-1][j]) <= fiss):
                        kilaeua[i-1][j] = '*'
                except:
                    print(end='')       
            if(bot):
                try:
                    if(int(kilaeua[i+1][j]) <= fiss):
                        kilaeua[i+1][j] = '*'
                except:
                    print(end='')    

            if(left):
                try:
                    if(int(kilaeua[i][j+1]) <= fiss):
                        kilaeua[i][j+1] = '*'
                except:
                    print(end='')
            if(left):
                try:
                    if(int(kilaeua[i][j+1]) <= fiss):
                        kilaeua[i][j+1] = '*'
                except:
                    print(end='')


for i in range(0, size):
    for j in range(0, size):
        print(kilaeua[i][j],end=" ")
    print()