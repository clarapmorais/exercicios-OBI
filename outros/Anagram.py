a = str(input("String A: "))
b = str(input("String B: "))

blist = []
for i in b:
    blist.append(i)

for e in a:
    try:
        blist.remove(e)
    except:
        print("No")
        break

if(len(blist)==0):
        print("Yes")