"""Refaça o exercício 5 alterando-o de modo que a base e a altura do
triângulo sejam lidas do teclado. Considere-as números reais."""



print()
print("Iniciando o Script...")
print("Atribuindo os valores...")

base = float(input("base = "))
altura = float(input("altura = "))

area = base * altura / 2

print("Triangula com base = {0} cm e altura {1} cm resulta em area {2} cm".format(base, altura, area))
print()
print("Encerrando o script...")