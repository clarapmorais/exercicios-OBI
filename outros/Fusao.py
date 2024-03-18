bancos =  int(input("bancos: "))
oprcs =  int(input("operacoes: "))

fusoes = list()
for x in range(0, oprcs):
    tipo_opr = str(input("Tipo opr: "))#f or c

    bancoX = int(input("banco x: "))
    bancoY = int(input("banco y: "))

    if(tipo_opr in "Ff"):
        if(bancoX not in fusoes):
            fusoes.append(bancoX)

        if(bancoY not in fusoes):
            fusoes.append(bancoY)
    
    if(tipo_opr in "Cc"):
        if(bancoX in fusoes and bancoY in fusoes):
            print("S")
        else:
            print("N")