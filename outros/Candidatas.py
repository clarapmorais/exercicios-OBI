n = str(input()).split()
m = int(n[1])
n = int(n[0])

s = str(input()).split()

for c in range(0, m):
    o = str(input()).split()
    t = int(o[0])
    stt = int(o[1])
    end = int(o[2])

    if(t == 1):
        s[stt-1] = end

    if(t == 2):
        mdcs = 0
        for i in range(stt-1, end):
            for j in range(i, end):

                min_s = 9999999
                for k  in range(i, j):
                    if(int(s[k]) <= min_s):
                        min_s = int(s[k])
                        print("hm")
                
                founds = 0
                for k  in range(i, j):
                    if(min_s == 1):
                        founds=0
                        break

                    if (int(s[k]) % min_s == 0):
                        founds+=1
                
                mdcs+=founds
        print(mdcs)

print(s)
print(min_s)