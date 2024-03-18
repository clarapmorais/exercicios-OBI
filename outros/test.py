#tudo isso só pra pegar as informações
casos = int(input())

saida = []
for i in range(casos):
  entrada = input()

  bufunfa, total_ingredientes, total_bolos = map(int, entrada.split())
  #bufunfa = int(input("Informe o total de dinheiros da Maria:"))
  #total_ingredientes = int(input("Informe o total de ingredientes:"))
  #total_bolos = int(input("Informe o total de bolos:"))

  entrada = map(int, input().split())
  lista_preco_ingredientes = []
  for e in entrada:
    lista_preco_ingredientes.append(e)

  lista_receita_bolo = []
  for j in range(total_bolos):
    entrada = input().split()

    quantidade_itens_receita = int(entrada[0])

    ingredientes_receita = []
    for e in range(1, len(entrada), 2):
      codigo_ingrediente = int(entrada[e])
      medida_ingrediente = int(entrada[e+1])

      ingredientes_receita.append((medida_ingrediente, lista_preco_ingredientes[codigo_ingrediente]))
    
    lista_receita_bolo.append((quantidade_itens_receita, ingredientes_receita))
  
  #calculando quanto "custa" fazer cada bolo (estou dentro do for)
  lista_preço_cada_bolo = []
  for j in lista_receita_bolo:
    soma = 0.0
    for k in j[1]:
      soma += float(k[0] * k[1])
    lista_preço_cada_bolo.append(soma)
  
  #cálculo do máximo de bolos
  lista_total_bolos_consigo_fazer = [0] * total_bolos
  for j in range(total_bolos):
    lista_total_bolos_consigo_fazer[j] = bufunfa // lista_preço_cada_bolo[j]

  #retorna o máximo de bolos que consigo fazer
  saida.append(max(lista_total_bolos_consigo_fazer))

for s in saida:
  print(int(s))