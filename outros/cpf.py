#FROM https://www.urionlinejudge.com.br/judge/en/problems/view/1769

cpf = input()

part1, part2 = cpf.split('-')
part1 = list(part1.replace('.', ''))
part2 = list(part2)

validez1 = False
soma_b1 = 0
for e in range(1, 10):
    soma_b1 += int(part1[e-1]) * e

if (soma_b1 % 11 == int(part2[0])) or (soma_b1 % 11 == 10 and int(part2[0]) == 0):
    validez1 = True

validez2 = False
soma_b2 = 0
for e in range(1, 10):
    soma_b2 += int(part1[e-1]) * (10 - e)

if (soma_b2 % 11 == int(part2[1])) or (soma_b2 % 11 == 10 and int(part2[1]) == 0):
    validez2 = True

if(validez1==True and validez2==True):
    print("CPF valido")
else:
    print("CPF invalido")