n = int(input("Insira o tamanho do array: "))
s = int(input("Insira a soma buscada: "))

a = []
for i in range(0, n):
    a.append(int(input("Insira um número: ")))

sum=0
should_break = False
for i in range(0, n):
    sum=0
    for j in range(i,n):
        sum+=a[j]
        if(sum==s):
            print("conquistado")
            should_break = True
            break

    if(should_break):
        break

print(f"está da posição {i+1} a {j+1}")