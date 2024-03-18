i1 = int(input())
i2 = int(input())
i3 = int(input())

if((i1>=i2 or i1>=i3) and (i1<=i2 or i1<=i3)):
    print(i1)
elif((i2>=i1 or i2>=i3) and (i2<=i1 or i2<=i3)):
    print(i2)
elif((i3>=i1 or i3>=i2) and (i3<=i1 or i3<=i2)):
    print(i3)
