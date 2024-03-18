casas = int(input("Número de casas: "))
objetivo = int(input("Para onde vai: "))
posicao = int(input("De onde vai: "))

if(objetivo>=posicao):
    movimentacao = objetivo - posicao
else:
    movimentacao = casas - posicao + objetivo

print(movimentacao)