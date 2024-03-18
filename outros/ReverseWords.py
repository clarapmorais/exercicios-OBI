s = str(input("Insira strin: "))

s_list = s.split('.')

return_list = []
for i in range(len(s_list)-1,-1,-1):
    if(i==len(s_list)-1):
        return_list.append(s_list[i])
    else:
        return_list.append("." + s_list[i])

for e in return_list:
    print(e, end="")
