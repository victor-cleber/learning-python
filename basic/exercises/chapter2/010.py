"""Um vendedor ambulante vendeu os produtos indicados na tabela a
seguir. Informe quanto ele faturou com cada produto e quanto ele
faturou no total.
Produto                 Quantidade vendida          Valor unitário R$
Boneco Malandrinho              17                         18,50
Spinner Pequeno                 36                         12,00
Cubo Mágico                      7                          5,90
Todos os dados devem ser lidos do teclado, sendo que o nome do
produto é string, a quantidade vendida é um número inteiro e o valor
unitário é um número real."""


print()
print("Iniciando o Script...")
print("Atribuindo os valores...")
print()
produto1 = input("Informe o nome do produto 1: ")
quantidade_vendida1 = int(input("Informe a quantidade vendida  do produto 1: "))
valor_unitario1 = float(input("Informe o valor unitario  do produto 1: "))

produto2 = input("Informe o nome do produto 2: ")
quantidade_vendida2 = int(input("Informe a quantidade vendida  do produto 2: "))
valor_unitario2 = float(input("Informe o valor unitario  do produto 2: "))

produto3 = input("Informe o nome do produto 3: ")
quantidade_vendida3 = int(input("Informe a quantidade vendida do produto 3: "))
valor_unitario3 = float(input("Informe o valor unitario do produto 3: "))


print()
print("|-----------------------------------------------------------|")
print("| PRODUTO    |   QUANTIDADE VENDIDA   |   VALOR UNITARIO R$ |")
print("| {0}        |      {1}       |   {2}   |".format(produto1, quantidade_vendida1, valor_unitario1))
print("| {0}        |      {1}       |   {2}   |".format(produto2, quantidade_vendida2, valor_unitario2))
print("| {0}        |      {1}       |   {2}   |".format(produto2, quantidade_vendida3, valor_unitario3))
print("|-----------------------------------------------------------|")
print()


print()
print("Encerrando o script...")
print()