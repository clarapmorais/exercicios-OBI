#INFUNCIONAL
n = int(input(""))

td = [*range(0, 100)]
#td[#amigo] = [#status, #tempo total resposta]
#status: sem resposta=0, respondido=1

for i in range(0, n):
    o, z = str(input('')).split(' ')
    z = int(z)

    if(i%2!=0):
        for j in range(0, len(td)):
            if(type(td[j]) == list):
                if(td[j][0] == 0):
                    td[j][1] += 1

    if(o == 'R'):
        try:
            td[z][0] = 0
        except:
            td[z] = [0, 0]

    elif(o == 'E'):
        td[z][0] = 1

    else:
         for j in range(0, len(td)):
            if(type(td[j]) == list):
                if(td[j][0] == 0):
                    td[j][1] += z


for i in range(0, len(td)):
    if(type(td[i]) == list):

        print(i, end=" ")
        
        if(td[i][0] ==  1):
            print(td[i][1])
        else:
            print(-1)